from os.path import exists

def clipboard_access():
 from sys import argv
 if  '-i' in argv: return False
 try:
  from clipboard import paste
  paste()
 except:
  return False
 else:
  return True



UNICODE_DATA_PATH = 'UnicodeData.txt'
UNICODE_DATA_URL = 'https://unicode.org/Public/UNIDATA/UnicodeData.txt'

def download_unicode_data():
 try:
  from requests import get
  UNICODE_DATA = open(UNICODE_DATA_PATH,'w')
  UNICODE_DATA.write(get(UNICODE_DATA_URL).text)
  UNICODE_DATA.close
 except:
  print(f'Failed to download {UNICODE_DATA_URL} to {UNICODE_DATA_PATH}. ')
  print(f'Deleting {UNICODE_DATA_PATH}…')
  UNICODE_DATA.close()
  try:
   from os import remove
   remove(UNICODE_DATA_PATH)
  except:
   print(f'Failed to delete {UNICODE_DATA_PATH}. ')
  else:
   print(f'Successfully deleted {UNICODE_DATA_PATH}. ')
  quit()
 else:
  print(f'Successfully downloaded {UNICODE_DATA_URL} to {UNICODE_DATA_PATH}. ')

if not exists(UNICODE_DATA_PATH):
 print(f'{UNICODE_DATA_PATH} not found, downloading from {UNICODE_DATA_URL}. ')
 download_unicode_data()
 
if len(open(UNICODE_DATA_PATH,'rb').read()) == 0:
 open(UNICODE_DATA_PATH,'rb').close()
 print(f'{UNICODE_DATA_PATH} is empty, redownloading… ')
 download_unicode_data()
else:
 open(UNICODE_DATA_PATH,'rb').close()

UNICODE_DATA = open(UNICODE_DATA_PATH,'r')

data = list()

for line in UNICODE_DATA:
 data.append(line.split(';'))

UNICODE_DATA.close()

if clipboard_access():
 from clipboard import paste
 TXT_IN = paste()
else: TXT_IN = input('Input text: ')

name_max_length = 32

JUSTIFY = [12,name_max_length,8]

print('CODEPOINT'.rjust(JUSTIFY[0]),'NAME'.rjust(JUSTIFY[1]),'GLYPH'.rjust(JUSTIFY[2]))
for char in TXT_IN:
 code = f'U+{data[ord(char)][0].zfill(6)}'
 name = data[ord(char)][1]
 name_alt_0 = f'= {data[ord(char)][10]}' if len(data[ord(char)][10]) else ''
 print(code.rjust(JUSTIFY[0]),name.rjust(JUSTIFY[1]),char.rjust(JUSTIFY[2]))
 print(''.rjust(JUSTIFY[0]),name_alt_0.rjust(JUSTIFY[1]))