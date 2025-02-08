import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.ventusky.com/isfahan")

soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('div', attrs={'class' : 'info_table'})

if len(items) == 0:
    print("not found")
else:
    titles = items[0].find_all('td', attrs={'class' : 'temperature'})

    for item in titles:
        print(item.getText())
