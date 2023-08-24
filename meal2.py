from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://jeju-s.jje.hs.kr/jeju-s")
soup = BeautifulSoup(html, "html.parser")

bap = soup.select(".meal_menu ul li")
print("="*50)
print( bap)
print("-"*50)

for m in bap:
   print( m.text.strip()) 
   menu=m.text

print("="*50)

menu=menu.split(" ")
print(menu)

i=0


for m in menu:
   i+=1
   if m!="":
     print(i,m)