from glob import glob

RATE_MULTIPLIER = float(input('Input rate multiplier (recommended value 1.2): '))
brstm_list = glob('*_n.brstm')

for file in brstm_list:
 brstm_n = open(file,'rb')
 brstm_f = open(f'{file.rstrip("_n.brstm")}_f.brstm','wb')
 brstm_f.write(brstm_n.read(0x64))
 rate_old = int.from_bytes(brstm_n.read(2),byteorder='big')
 rate_new = int(rate_old * RATE_MULTIPLIER)
 brstm_f.write(rate_new.to_bytes(2,byteorder='big'))
 brstm_f.write(brstm_n.read())
 print(f'{file}: old rate {rate_old}Hz, new rate {rate_new}Hz. ')