from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).resolve().parent
W,H=1340,1075;im=Image.new('RGB',(W,H),'#fafbf9');d=ImageDraw.Draw(im)
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
t(24,17,'Safiullin har formen – Shimabukuro har det höga oddset',32,True)
t(24,67,'Almaty • 20 oktober 2026, preliminärt 08.30 svensk tid • herrsingel på hardcourt',21)
t(24,116,'Jämförelse',20,True);t(790,116,'Sho Shimabukuro',23,True,right=True);t(1314,116,'Roman Safiullin',23,True,right=True)
rows=[('Ranking / karriärbästa','109 / 87','79 / 36'),('Senaste 10 huvudturneringsmatcher','0–10','5–5'),('Hardcourt 2026, huvudturnering','1–12','5–5'),('Alla underlag 2026, huvudturnering','4–15','8–8'),('Svenska Spels odds¹','5,40','1,15'),('Din GPT-modell²','3,18','1,36'),('Tennis Abstract via tjänsten²','3,80','1,27')]
for i,(label,a,b) in enumerate(rows):
 y=156+i*37
 if i%2==0:d.rectangle((18,y-4,W-18,y+30),fill='#eff3f0')
 t(24,y,label,21);t(790,y,a,23,i in (1,4),right=True);t(1314,y,b,23,i in (1,4),right=True)
t(24,435,'Senaste tio på touren',22,True)
t(24,470,'Shimabukuro',20);t(700,470,'Safiullin',20)
for x0,seq in [(205,'FFFFFFFFFF'),(865,'FFVVVFVFVF')]:
 for j,ch in enumerate(seq):
  x=x0+j*40;d.rounded_rectangle((x,467,x+31,497),radius=4,fill='#d9ece5' if ch=='V' else '#f3ded9');t(x+8,470,ch,19,True,c='#087e73' if ch=='V' else '#b44f48')
t(24,513,'V = vinst, F = förlust • äldre → nyare • kval, Challenger och Davis Cup ingår inte här',17,c='#587174')
d.line((24,546,W-24,546),fill='#bdcdc8')
t(24,565,'Varför Safiullin är favorit',24,True)
para(24,604,'Semifinal i Hangzhou och seger över dåvarande världssjuan Cobolli i Beijing, 6–3, 6–2. Han har dessutom vunnit två kvalmatcher i Almaty. Shimabukuro har förlorat sina tre senaste tourmatcher i raka set mot Gaston, Shapovalov och Kecmanovic.',620,20)
t(705,565,'Varför oddsgapet måste granskas',24,True)
para(705,604,'5,40 kräver en vinstchans över 18,5 % för positiv förväntad avkastning. Om modellernas cirka 5 % överrundning normaliseras proportionellt blir Shimabukuros andel cirka 30 % i GPT och 25 % i TA. Det är modellskattningar, inte verifierade vinstchanser.',610,20)
d.rectangle((18,758,W-18,881),fill='#e0efe9')
t(34,773,'Min bedömning',24,True)
para(34,812,'Safiullin är det tydliga vinnarvalet utifrån resultaten. Shimabukuro är en modellavvikelse att undersöka vidare, men hans svaga tourform gör att jag inte skulle kalla 5,40 ett starkt spel enbart på oddsgapet. Modellernas hantering av aktuell form och tävlingsnivå behöver granskas.',1265,20)
for i,s in enumerate([
'Underlag: databasens Completed/Aborted-matcher. Huvudturnering = ATP 250/500, Masters, Grand Slam och ATP Finals; inga kval.',
'Årsfacit: turneringsstart 1 jan–19 okt 2026. Senaste tio ordnas efter turneringsstart, omgång och match-ID. Inga inbördes möten hittades.',
'Hardcourt är databasens underlag; ingen separat inomhusstatistik används. Skador och dagsfysik är inte verifierade.',
'¹ Externt Oddset-flöde via /api/oddset. ² Beräknade odds från /api/odds, Hard; modellerna är inte oberoende bevis.',
'Källa: tennis.egelberg.se, direkt SQL + angivna API-flöden • uttag 19 oktober 2026 • sparat underlag: ATP-20261019-07.'
]):t(24,915+i*29,s,17,c='#587174')
im.save(p/'shimabukuro-safiullin-analys.png')
