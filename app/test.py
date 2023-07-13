import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua = UserAgent()

url_before = 'https://urfu.ru/api/ratings/info/50/636'
url = requests.get(
    url=url_before,
    headers={'user-agent': f'{ua.random}'}
).json()['url']
response = requests.get(
    url=f'https://urfu.ru{url}',
    headers={'user-agent': f'{ua.random}'}
)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# with open('test.html', 'w') as f:
#     f.write(soup.prettify())
snils = '15832352164'
abits_all = soup.find_all('tr', class_='tr-odd') + \
    soup.find_all('tr', class_='tr-even')
for abit in abits_all:
    abit_temp_data = []
    for elem in abit.descendants:
        if elem.name is not None:
            abit_temp_data.append(elem.text)
    try:
        if abit_temp_data[0] == '176':
            if abit_temp_data[1] == snils:
                print(abit_temp_data)
    except Exception as e:
        print(e)
