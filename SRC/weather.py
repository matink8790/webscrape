import requests
from bs4 import BeautifulSoup

response = requests.get("https://torob.com/p/b7fe3c1c-0d74-4a3a-bed3-7e29e92f3fda/%DA%AF%D9%88%D8%B4%DB%8C-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%D9%88%DB%8C%D8%AA%D9%86%D8%A7%D9%85-s24-ultra-5g-%D8%AD%D8%A7%D9%81%D8%B8%D9%87-256-%D8%B1%D9%85-12-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA/")

soup = BeautifulSoup(response.text, 'html.parser')

items = soup.find_all('div', attrs={'class' : "Showcase_cheapest_seller__TJpf9 Showcase_online_seller__PpZcm"})
if len(items) == 0:
    print("not found")
else:
    titles = items[0].find_all('div', attrs={'class' : 'Showcase_buy_box_text__otYW_ Showcase_ellipsis__FxqVh'})

    for item in titles:
        print(item.getText())
