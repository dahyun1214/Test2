from bs4 import BeautifulSoup
import requests

url = "http://jeju-s.jje.hs.kr/&quot;"

r = requests.get(url)
#container > div.main_content > div.meal_menu > ul > li
print(r.raise_for_status)

html = r.text

soup = BeautifulSoup(html, "html.parser")

context = soup.select(".meal_menu")

print(context)

print("-"*50)

t = context[0].select_one("p")
print(t.text)

