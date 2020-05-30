from glob import glob

RATE_MULTIPLIER = float(input('Input rate multiplier (recommended value 1.2): '))
brstm_list = glob('*_n.brstm')

for i,file in enumerate(brstm_list,1):
 brstm_n = open(file,'rb')
 if brstm_n.read(6) == b'RSTM\xfe\xff':
  endianness = 'big'
 elif brstm_n.read(6) == b'RSTM\xff\xfe':
  endianness = 'little'
 else:
  print('Invalid file.  ')
  quit()
 brstm_n.seek(0)
 brstm_f = open(f'{file.rstrip("_n.brstm").rstrip("_N.brstm")}_f.brstm','wb')
 brstm_f.write(brstm_n.read(0x64))
 rate_old = int.from_bytes(brstm_n.read(2),byteorder=endianness)
 rate_new = int(rate_old * RATE_MULTIPLIER)
 brstm_f.write(rate_new.to_bytes(2,byteorder=endianness))
 brstm_f.write(brstm_n.read())
 brstm_n.close()
 brstm_f.close()
 print(f'{i}: {file}: endianness {endianness}, original rate {rate_old}Hz, new rate {rate_new}Hz. ')
