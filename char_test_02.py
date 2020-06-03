def fullwidth(TXT_IN,FULLWIDTH_SP_COUNT,SEPARATOR='',out=[]):
 for item in TXT_IN:
  if ord(item) in range(0x21,0x7f):
   item = ord(item) + 0xfee0
   out.append(chr(item))
  elif ord(item) in range(0x2985,2987):
   item = ord(item) + 0xd5da
   out.append(chr(item))
  elif ord(item) == 0x20:
   item *= FULLWIDTH_SP_COUNT
   out.append(item)
  else:
   out.append(item)
 return f'{SEPARATOR}'.join(out)

def negative_circled(TXT_IN,SEPARATOR='',out=[]):
 for item in TXT_IN:
  if ord(item) in range(0x41,0x5b):
   item = chr(ord(item) + 0x1f10f)
   out.append(item)
  elif ord(item) in range(0x61,0x7b):
   item = chr(ord(item) + 0x1f0ef)
   out.append(item)
  else:
   out.append(item)
 return f'{SEPARATOR}'.join(out)
 
def negative_squared(TXT_IN,SEPARATOR='',out=[]):
 for item in TXT_IN:
  if ord(item) in range(0x41,0x5b):
   item = chr(ord(item) + 0x1f12f)
   out.append(item)
  elif ord(item) in range(0x61,0x7b):
   item = chr(ord(item) + 0x1f10f)
   out.append(item)
  else:
   out.append(item)
 return f'{SEPARATOR}'.join(out)

def regional_indicator(TXT_IN,SEPARATOR='',out=[]):
 for item in TXT_IN:
  if ord(item) in range(0x41,0x5b):
   item = chr(ord(item) + 0x1f1a5)
   out.append(item)
  elif ord(item) in range(0x61,0x7b):
   item = chr(ord(item) + 0x1f185)
   out.append(item)
  else:
   out.append(item)
 return f'{SEPARATOR}'.join(out)

