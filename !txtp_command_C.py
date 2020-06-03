from glob import glob
import math

EXTENSION = input('Input file extension: '.rjust(32)).lstrip('.')
FILE_LIST = glob(f'*.{EXTENSION}')
if len(FILE_LIST) == 0:
 print('No files with this extension found.')
 quit()
OFFSET = int(input('Input offset of channel count: '.rjust(32)),0)
LENGTH = int(input('Input length of channel count: '.rjust(32)),0)
if LENGTH == 1:
 ENDIANNESS = 'little'
else:
 ENDIANNESS = input('Input endianness of channel count: '.rjust(32))
SPLIT = int(input('Input channels per TXTP: '.rjust(32)),0)
MAX_CHANNELS = 16

txtp_list = list()

def create_bat():
 bat_name = f'!del_txtp_{SPLIT}.bat'
 if len(txtp_list) > 0:
  bat = open(bat_name,'w')
  for i,txtp in enumerate(txtp_list):
   bat.write(f'DEL \'{txtp_list[i]}\'\n')
  bat.write(f'DEL \'{bat_name}\'')
  print(f'{bat_name} created. ')
  bat.close()
 else:
  print('No items were created. ')

def command():
 command = list()
 for i in range(SPLIT):
  if len(channel_nums) > 0:
   command.append(channel_nums.pop(0))
 return command

try:
 for file in FILE_LIST:
  strm = open(file,'rb')
  strm.seek(OFFSET)
  num_channels = min(int.from_bytes(strm.read(LENGTH),ENDIANNESS),MAX_CHANNELS)
  strm.close()
  if num_channels > SPLIT:
   channel_nums = list(range(1, num_channels + 1))
   for i in range(math.ceil(num_channels / SPLIT)):
    txtp_name = f'{file}#C{",".join(str(num) for num in command())}.txtp'
    txtp_list.append(txtp_name)
    txtp = open((txtp_name),'wb')
    txtp.close()
    print(f'{txtp_name} created. ')

except KeyboardInterrupt:
 create_bat()
 quit()

else:
 create_bat()