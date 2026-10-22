import json
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).resolve().parent;r=json.loads((p/'comparison.json').read_text())[:8]
W,H=1460,965;im=Image.new('RGB',(W,H),'#fafbf9');d=ImageDraw.Draw(im)
def f(n,b=False):return ImageFont.truetype('/System/Library/Fonts/Supplemental/'+('Arial Bold.ttf' if b else 'Arial.ttf'),n)
def t(x,y,s,n=21,b=False,c='#183c42',right=False):
 if right:x-=d.textlength(s,font=f(n,b))
 box=d.textbbox((x,y),s,font=f(n,b));assert box[2]<W-15 and box[3]<H,(s,box)
 d.text((x,y),s,font=f(n,b),fill=c)
def para(x,y,s,width,n=20):
 line=''
 for word in s.split():
  a=(line+' '+word).strip()
  if d.textlength(a,font=f(n))>width:t(x,y,line,n);y+=27;line=word
  else:line=a
 if line:t(x,y,line,n)
def num(v):return f'{v:.2f}'.replace('.',',')
t(24,16,'Var skiljer sig din modell mest från Svenska Spel?',34,True)
t(24,70,'Tisdag 20 oktober • 15 ATP-matcher jämförda • din modell = tjänstens GPT-odds',22)
d.rectangle((18,115,W-18,184),fill='#e0efe9')
t(34,129,'Störst gap: Shimabukuro 5,40 hos Svenska Spel mot 3,18 i modellen',26,True)
for x,s in [(24,'Tid / ort'),(215,'Spelare'),(600,'Motståndare'),(1040,'Sv. Spel'),(1168,'Din modell'),(1282,'TA¹'),(1435,'Skillnad²')]:t(x,211,s,19,True,right=x>=1040)
for i,x in enumerate(r):
 y=250+i*49
 if i%2==0:d.rectangle((18,y-5,W-18,y+40),fill='#eff3f0')
 tm=datetime.fromisoformat(x['start'].replace('Z','+00:00')).astimezone(ZoneInfo('Europe/Stockholm')).strftime('%H.%M')
 t(24,y,tm,21,True);t(24,y+24,x['event'],16,c='#587174')
 t(215,y+8,x['player'],22,i<3);t(600,y+8,x['opponent'],21)
 for xx,k in [(1040,'ss'),(1168,'gpt'),(1282,'ta')]:t(xx,y+8,num(x[k]),22,k=='ss',right=True)
 t(1435,y+8,f"+{x['diff']:.1f} %".replace('.',','),22,True,'#087e73',True)
d.line((24,656,W-24,656),fill='#bdcdc8')
t(24,675,'Stora gap – men olika signaler',23,True)
para(24,715,'Shimabukuro har störst gap, men är tydlig outsider hos båda modellerna. Samuel: 2,90 mot 1,93; GPT ser ett nästan jämnt möte, medan TA gör honom till favorit.',450,19)
t(510,675,'Två matcher med omvänd favorit',23,True)
para(510,715,'Collignon och Gaston är outsiders hos Svenska Spel men favoriter i både GPT och TA. Där handlar skillnaden även om vem som bör vara favorit.',440,19)
t(990,675,'Kovacevic delar modellerna',23,True)
para(990,715,'4,20 ligger över GPT:s 3,51 men strax under TA:s 4,25. Gapet får alltså inte stöd av båda modellerna.',440,19)
d.line((24,833,W-24,833),fill='#bdcdc8')
for i,s in enumerate([
'¹ TA = Tennis Abstract-odds från tennistjänsten. ² Skillnad = (Svenska Spels odds / GPT-odds − 1) × 100; inte förväntad avkastning.',
'Urval: åtta största positiva skillnader bland 30 spelarsidor i 15 kommande matcher den 20 oktober, svensk tid. Underlag: Hard.',
'Källor: Svenska Spels externa Oddset-flöde via tennis.egelberg.se/api/oddset; beräkningar via /api/odds/matches. Inga lagrade DB-odds.',
'Modellernas inversa odds summerar till cirka 105 %. Tider och spelodds är preliminära. Uttag 19 oktober 2026 • ATP-20261019-06.'
]):t(24,850+i*27,s,17,c='#587174')
im.save(p/'oddsskillnader-imorgon.png')
