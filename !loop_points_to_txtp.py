#Originally written for use with https://pastebin.com/raw/KNLvDr9i​, format must be as follows:
#[filename (with extension)] - [loop start] [loop end]

list_file = open('!list.txt','r')
ADDITIONAL_COMMANDS = '#m0x2.5'

for i,line in enumerate(list_file,1):
 data = line[line.rfind('/') + 1:].rstrip("\n").split(" - ")
 points = data[1].split(' ')
 if int(points[1],10) != 0:
  txtp_name = f'{data[0][:data[0].rfind(".")]}.txtp'
  txtp_contents = f'{data[0]}\n\ncommands = #I{points[0]} {points[1]}{ADDITIONAL_COMMANDS}'
  txtp = open(txtp_name,'w')
  txtp.write(txtp_contents)
  txtp.close()