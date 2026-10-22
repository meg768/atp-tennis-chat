import json
from pathlib import Path
from datetime import date
from PIL import Image,ImageDraw,ImageFont
r=json.loads((Path(__file__).resolve().parent/'results.json').read_text())
im=Image.new('RGB',(1100,1030),'#f5f8f9');d=ImageDraw.Draw(im)
def font(n,b=False):return ImageFont.truetype('/System/Library/Fonts/Supplemental/'+('Arial Bold.ttf' if b else 'Arial.ttf'),n)
def t(x,y,s,n=20,b=False,c='#193341',right=False):
 if right:x-=d.textlength(s,font=font(n,b))
 box=d.textbbox((x,y),s,font=font(n,b));assert box[2]<1090 and box[3]<1030,(s,box)
 d.text((x,y),s,font=font(n,b),fill=c)
def age(s):
 b=date.fromisoformat(s);months=(2026-b.year)*12+10-b.month-(19<b.day);return f'{months//12} år {months%12} mån'
d.rectangle((0,0,1100,83),fill='#153746')
t(18,11,'Unga rankingklättrare – vilka har stigit mest?',29,True,'white')
t(18,52,'Under 23 år • topp 100 nu • uppskattad förändring senaste året',20,c='#d7e8ec')
for x,s in [(18,'#'),(53,'Spelare'),(430,'Ålder nu'),(666,'Ranking då → nu'),(827,'Klättring'),(1080,'Historisk observation')]:t(x,103,s,18,True,right=x>=666)
for i,p in enumerate(r[:10]):
 y=139+i*31
 d.rectangle((10,y-3,1090,y+26),fill='#d5eee7' if i==0 else ('#eaf0f3' if i%2==0 else '#f5f8f9'))
 t(18,y,str(i+1));t(53,y,p['name'],21,i==0);t(430,y,age(p['birthdate']),19)
 t(666,y,f"{p['old_rank']} → {p['rank']}",21,right=True);t(827,y,f"+{p['gain']}",21,True,'#12695f',True)
 t(1080,y,p['observed_date'],19,right=True)
t(18,461,'Grönt: Jodar är både yngst av de 17 i urvalet och den som klättrat flest platser.',18,c='#526b78')
d.line((18,492,1082,492),fill='#cad7df')
t(18,506,'TVÅ SÄTT ATT HITTA DE UNGA GENOMBROTTEN',21,True)
for i,s in enumerate([
'Jodar: 20 år, från 283 till 13 – en klättring på 270 platser. Sex spelare har klättrat minst 100 platser.',
'De tre yngsta i hela urvalet: Jodar (+270), Joao Fonseca (+16, nu 29) och Martin Landaluce (+37, nu 73).',
'Alla tre är 20 år. Fonseca når inte denna topp 10-lista eftersom han redan låg på plats 45 för ett år sedan.'
]):t(18,537+i*23,s,18)
t(18,621,'URVAL, METOD OCH BEGRÄNSNINGAR',21,True)
for i,s in enumerate([
'10 största lyften bland 17 spelare under 23 år med aktuell profilranking 1–100. Ålder per 19 oktober 2026.',
'”Då” = senaste positiva matchranking vid turneringsstart senast 19 oktober 2025, alla tävlingstyper/statusar.',
'”Nu” = spelarprofilens ranking vid uttaget. Skillnaden är en uppskattning, inte två verifierade veckolistor.',
'Historiska observationer i listan är 6–20 dagar äldre än jämförelsedatumet. Dataluckor kan påverka ordningen.',
'Antal klättrade platser gynnar en låg startposition. Spelare utanför dagens topp 100 ingår inte i jämförelsen.'
]):t(18,651+i*22,s,17)
d.rectangle((10,779,1090,992),fill='#e5edf1')
t(18,790,'ÅTERSKAPA URVALET • ATP-20261019-01',20,True)
for i,s in enumerate([
'Urval: herrsingel, under 23 år den 19 okt 2026, profilranking 1–100 vid uttaget. Inga manuella undantag.',
'Baslinje: senaste positiva matchranking med turneringsstart senast 19 okt 2025; alla typer/statusar.',
'Vid flera observationer samma datum: högsta match-ID. Saknad historik ger inget beräknat lyft.',
'Klättring = historisk ranking minus profilranking. Sortera störst lyft först, därefter senaste födelsedatum.',
'Visa de 10 första. Ålder beräknas från födelsedatum per 19 okt 2026.',
'SQL + samtliga 17 resultatrader är sparade under analys-ID:t. Bilden återger det sparade uttaget.',
'Samma regler kan köras igen; identiska siffror kräver sparat resultat eftersom databasen kan ändras.'
]):t(18,824+i*23,s,17)
t(18,1006,'Källa: endast tennis.egelberg.se-databasen • direkt SQL • uttag 19 oktober 2026',17,c='#526b78')
p=Path(__file__).resolve().parent/'unga-rankingklattrare.png';im.save(p);print(p)
