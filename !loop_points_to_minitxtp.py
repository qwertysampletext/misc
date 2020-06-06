#Originally written for use with https://pastebin.com/raw/KNLvDr9i​, format must be as follows:
#[filename (with extension)] - [loop start] [loop end]

list_file = open('!list.txt','r')

for i,line in enumerate(list_file,1):
 data = line[line.rfind('/') + 1:].rstrip("\n").split(" - ")
 points = data[1].split(' ')
 if int(points[1],10) != 0:
  txtp_name = f'{data[0]}#I{points[0]} {points[1]}.txtp'
  print(f'{str(i).zfill(4)}: {txtp_name}')
  open(txtp_name,'wb').close()