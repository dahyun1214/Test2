from bs4 import BeautifulSoup

with open("temp.html", "r", encoding="utf-8") as file:
   html = file.read()

soup = BeautifulSoup(html, "html.parser")

pp = soup.select(".tow")

for p in pp:
   print( p.text)