from glob import glob

RATE_MULTIPLIER = float(input('Input rate multiplier (recommended value 1.06): '))
brstm_list = list(dict.fromkeys(glob('*_n.brstm') + glob('*_N.brstm')))

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
 rate_old = int.from_bytes(brstm_n.read(2),endianness)
 rate_new = int(rate_old * RATE_MULTIPLIER)
 brstm_f.write(rate_new.to_bytes(2,endianness))
 brstm_f.write(brstm_n.read())
 brstm_n.close()
 brstm_f.close()
 print(f'{str(i).zfill(3)}: {file.rjust(32)}: endianness {endianness}, original rate {str(rate_old).zfill(5)}Hz, new rate {str(rate_new).zfill(5)}Hz. ')
