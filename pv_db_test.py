pv_db_txt = open('pv_db.txt','rb').read().decode('utf-8')
pv_db = dict()
plist = open('!tags.m3u','wb')
en = False

for i in pv_db_txt.split('\n'):
 if i.startswith('pv_'):
  key,value = i.split('=',1)
  pv,info = key.split('.',1)
  if not pv in pv_db: pv_db[pv] = {}
  pv_db[pv][info] = value

for i in pv_db:
 pv = pv_db[i]
 data = dict()
 if 'song_name' in pv or 'song_name_en' in pv: data['TITLE'] = (pv['song_name_en'] if 'song_name_en' in pv else pv['song_name']) if en else (pv['song_name'] if 'song_name' in pv else pv['song_name_en'])
 if 'songinfo.music' in pv: data['ARTIST'] = pv['songinfo.music']
 if 'date' in pv: data['DATE'] = pv['date']
 if 'performer.num' in pv:
  data['NUM_PERFORMERS'] = pv['performer.num']
  num_performers = int(pv['performer.num'])
  performers = list()
  for a in range(0,num_performers):
   if pv[f'performer.{a}.type'] == 'VOCAL': performers.append(pv[f'performer.{a}.chara'])
   else: performers.append(pv[f'performer.{a}.type'])
  if bool(performers): data['PERFORMERS'] = ','.join(performers)
 if 'song_file_name' in pv:
  for a in data:
   plist.write(bytes(f'# %{a}% {data[a]}\n','utf-8'))
  plist.write(bytes(pv['song_file_name'] + '.txtp\n\n','utf-8'))
