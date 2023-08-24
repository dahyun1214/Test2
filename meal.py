from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

url = "http://jeju-s.jje.hs.kr/&quot;"

r = requests.get(url, headers=headers)

print(r.raise_for_status)

html = r.text

soup = BeautifulSoup(html, "html.parser")

context = soup.select(".meal_menu")

print(context)

print("-"*50)

t = context[0].select_one("p")
print(t.text)
