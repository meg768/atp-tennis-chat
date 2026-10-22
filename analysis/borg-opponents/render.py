from PIL import Image,ImageDraw,ImageFont
import json
from pathlib import Path
P=Path(__file__).parent
im=Image.new('RGB',(1440,1120),'#fafbf9');d=ImageDraw.Draw(im)
ink='#183c42';mut='#587174';teal='#087e73'
def text(x,y,s,size=25,color=ink,bold=False):
 f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',size)
 d.text((x,y),s,font=f,fill=color)
def line(y):d.line((45,y,1395,y),fill='#cfdbd8',width=2)
text(45,30,'Vilka hade Björn Borg svårast för?',44,bold=True)
text(45,89,'McEnroe i de stora finalerna. Newcombe i inbördes vinstprocent.',29,teal,True)
text(45,137,'Borgs sju lägsta vinstprocenter mot motståndare med minst fem registrerade möten.',23,mut)
d.rounded_rectangle((45,188,1395,239),radius=8,fill='#e0efe9')
for x,s in [(62,'Motståndare'),(520,'Borgs V–F'),(755,'Vinstandel'),(1090,'Antal möten')]:text(x,200,s,24,bold=True)
r=json.load(open(P/'results.json'));r=sorted([x for x in r if int(x['matches'])>=5],key=lambda x:(int(x['wins'])/int(x['matches']),-int(x['matches'])))[:7]
for i,a in enumerate(r):
 y=244+i*57
 if i%2==0:d.rectangle((45,y,1395,y+55),fill='#eef2f0')
 pc=int(a['wins'])/int(a['matches'])*100
 text(62,y+12,a['name'],27,bold=i<2)
 text(544,y+12,f"{a['wins']}–{a['losses']}",27,bold=True)
 text(755,y+12,f'{pc:.1f} %'.replace('.',','),26)
 d.rounded_rectangle((875,y+19,1045,y+35),radius=5,fill='#dce5e1')
 d.rounded_rectangle((875,y+19,875+170*pc/100,y+35),radius=5,fill=teal)
 text(1165,y+12,str(a['matches']),26)
line(661)
text(45,682,'McEnroe: finalernas svåraste hinder',27,teal,True)
text(45,724,'7–7 totalt, men 1–3 i Grand Slam-finaler.',25,bold=True)
text(45,762,'Borg vann Wimbledon 1980. McEnroe vann',24)
text(45,795,'US Open 1980 och 1981 samt Wimbledon 1981.',24)
text(770,682,'Panatta: ett särskilt grusproblem',27,teal,True)
text(770,724,'Slog Borg i Roland Garros 1973 och 1976.',24)
text(770,762,'Borg ledde ändå deras grusmöten med 8–5',24)
text(770,795,'och vann semifinalen i Paris 1975.',24)
line(846)
text(45,868,'Flest förluster: Connors och Ashe, åtta var.',26,bold=True)
text(45,907,'Ashe pressade Borg till 9–8. Mot Connors hade Borg ett tydligare övertag: 15–8.',25)
line(961)
text(45,981,'Urval och tolkning',23,bold=True)
text(45,1014,'Alla tävlingstyper i databasen. Spelade och avbrutna matcher ingår; walkover utesluts.',21,mut)
text(45,1043,'Sorterat efter Borgs vinstandel, minst fem möten. Newcombes fem matcher är ett litet underlag.',21,mut)
text(45,1076,'Källa: tennis.egelberg.se · direkt SQL · 19 okt 2026 · Databasens historiska täckning kan vara ofullständig.',20,mut)
im.save(P/'borg-opponents.png')
