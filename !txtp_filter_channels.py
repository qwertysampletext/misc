import glob
import math
import os

ext = input("Input file extension (w/o full stop): ")
offset = int(input("Input offset of channel count: "),0)
endianness = input("Input endianness of channel count: ")
length = int(input("Input length of channel count: "),0)
split = int(input("Input channels per TXTP: "))

file_list = glob.glob("*.{}".format(ext))
txtp_list = []

def create_bat():
 bat_name = "!del_txtp_{}.bat".format(split)
 bat = open(bat_name.format(split),'w')
 count = 0
 for i in txtp_list:
  bat.write("DEL \"{}\"\n".format(txtp_list[count]))
  count += 1
 bat.write("DEL \"{}\"".format(bat_name))

def test01():
 count = 0
 while count < math.ceil(num_channels / split):
  txtp_name = "{}#C{}.txtp".format(file,','.join(str(x) for x in test02()))
  txtp_list.append(txtp_name)
  txtp = open((txtp_name),'wb')
  txtp.close()
  print("{} created. ".format(txtp_name))
  count += 1

def test02():
 count = 0
 command = []
 while count < split:
  try:
   command.append(channel_nums.pop(0))
  except IndexError:
   pass
  count += 1
 return command

try:
 for file in file_list:
  strm = open(file,'rb')
  strm.seek(offset)
  num_channels = int.from_bytes(strm.read(length),byteorder=endianness)
  strm.close()
  if num_channels > split:
   channel_nums = list(range(1, num_channels + 1))
   test01()
except KeyboardInterrupt:
 create_bat()
 quit()
  
create_bat()