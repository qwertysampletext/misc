from glob import glob

FIRST_STREAM_NUM = 0
EXTENSION = '_aac.aac'
SEARCH_PATTERN = '_ch'
FILE_LIST = glob(f'*{SEARCH_PATTERN}{FIRST_STREAM_NUM}{EXTENSION}')

for i in FILE_LIST:
 first_stream_name = i
 stream_name = i[:i.index(SEARCH_PATTERN)]
 stream_count = len(glob(f'{stream_name}{SEARCH_PATTERN}*{EXTENSION}'))
 txtp_contents = []
 for i in range(0,stream_count):
  txtp_contents.append(f'{stream_name}{SEARCH_PATTERN}{i}{EXTENSION}')
 txtp_contents.append('\nmode = layers')
 for i in open('!list.txt','r'):
  if first_stream_name in i:
   line = i[i.rfind('/') + 1:].rstrip("\n").split(" - ")
   points = line[1].split(' ')
   print(line[0],points)
   break
 additional_commands = f'#I{points[0]} {points[1]}'
 if 'additional_commands' in vars(): txtp_contents.append(f'commands = {additional_commands}')
 txtp_name = stream_name + '.txtp'
 txtp_contents = '\n'.join(txtp_contents)
 txtp = open(txtp_name,'wb')
 txtp.write(bytes(txtp_contents,'ascii') + (b'\x00' * (0xff - len(txtp_contents))))
 txtp.close()