# import requests
# from bs4 import BeautifulSoup

# from fake_useragent import UserAgent

# ua = UserAgent()

# url_before = 'https://urfu.ru/api/ratings/info/50/636'
# url = requests.get(
#     url=url_before,
#     headers={'user-agent': f'{ua.random}'}
# ).json()['url']
# response = requests.get(
#     url=f'https://urfu.ru{url}',
#     headers={'user-agent': f'{ua.random}'}
# )
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text, 'html.parser')
# # with open('test.html', 'w') as f:
# #     f.write(soup.prettify())
# snils = '15832352164'
# abits_all = soup.find_all('tr', class_='tr-odd') + \
#     soup.find_all('tr', class_='tr-even')
# for abit in abits_all:
#     abit_temp_data = []
#     for elem in abit.descendants:
#         if elem.name is not None:
#             abit_temp_data.append(elem.text)
#     try:
#         if abit_temp_data[0] == '176':
#             if abit_temp_data[1] == snils:
#                 print(abit_temp_data)
#     except Exception as e:
#         print(e)


# Chapter05/example3.py

# import threading
# import requests
# import time

# def ping(url):
#     res = requests.get(url)
#     print(f'{url}: {res.text}')

# urls = [
#     'http://httpstat.us/200',
#     'http://httpstat.us/400',
#     'http://httpstat.us/404',
#     'http://httpstat.us/408',
#     'http://httpstat.us/500',
#     'http://httpstat.us/524'
# ]

# start = time.time()
# for url in urls:
#     ping(url)
# print(f'Sequential: {time.time() - start : .2f} seconds')

# print()

# start = time.time()
# threads = []
# for url in urls:
#     thread = threading.Thread(target=ping, args=(url,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()

# print(f'Threading: {time.time() - start : .2f} seconds')

import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua = UserAgent()

url = 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205436693126454'

response = requests.get(
    url=url,
    headers={'user-agent': f'{ua.random}'}
)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# with open('test.html', 'w') as f:
#     f.write(soup.prettify())
snils = '158-323-521-64'
passing_points = soup.find_all('p')[1].text.split()[-1]
target_abit = soup.find('tr', id='1771028852693276311')

print(passing_points)
[print(data) for data in target_abit.find_all('td')]

# for abit in abits_all:
#     abit_temp_data = []
#     for elem in abit.descendants:
#         if elem.name is not None:
#             abit_temp_data.append(elem.text)
#     try:
#         if abit_temp_data[0] == '176':
#             if abit_temp_data[1] == snils:
#                 print(abit_temp_data)
#     except Exception as e:
#         print(e)