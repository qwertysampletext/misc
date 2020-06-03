import char_test_02

try:
 import clipboard
except ModuleNotFoundError:
 print('Clipboard module not found, use pip install clipboard. ')
 CLIPBOARD_MODULE = False
 CLIPBOARD_ACCESS = False
else:
 CLIPBOARD_MODULE = True
FULLWIDTH_SP_COUNT = 2

if CLIPBOARD_MODULE:
 try:
  TXT_IN = clipboard.paste()
 except PermissionError:
  TXT_IN = input('Failed to read clipboard, input text: ')
  CLIPBOARD_ACCESS = False
 else:
  CLIPBOARD_ACCESS = True
else:
 TXT_IN = input('Input text: ')

if CLIPBOARD_ACCESS:
 if clipboard.paste() == '':
  print('This tool uses clipboard contents as base text. Clipboard is empty or contents are invalid. ')
  TXT_IN = input('Input text: ')
MODE = input('Select mode: ')
while MODE not in ['fw','nc','ns','re','re_',]:
 MODE = input('Invalid mode. Select mode: ')
if MODE == 'fw':
 OUT = char_test_02.fullwidth(TXT_IN,FULLWIDTH_SP_COUNT)
elif MODE == 'nc':
 OUT = char_test_02.negative_circled(TXT_IN)
elif MODE == 'ns':
 OUT = char_test_02.negative_squared(TXT_IN)
elif MODE == 're':
 OUT = char_test_02.regional_indicator(TXT_IN)
elif MODE == 're_':
 OUT = char_test_02.regional_indicator(TXT_IN,chr(0x200c))

if CLIPBOARD_ACCESS:
 clipboard.copy(OUT)
else:
 print(OUT)