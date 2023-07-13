"""
Check my rating to HSU - модуль для парсинга данных с сайтов
ВУЗов
"""
import time 
import requests
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua = UserAgent()


def get_data_spbpu_parse(debug=False):
    """
    Функция парсит данные с сайта СПбПУ и возвращает
    массив данных со специальностями и местами
    """
    
    url = 'https://enroll.spbstu.ru/applicants/bachelor-specialist/rating'
    
    if not debug:
        data_req = []
    else:
        data_req = [('ПМИ', 1000), ('МАиКН', 250), ('Инноватика', 300)]
    
    return data_req


def get_data_spbgut_parse(debug=False):
    """
    Функция парсит данные с сайта СПбГУТ и возвращает
    массив данных со специальностями и местами
    """
    ...


def get_data_mirea_parse(debug=False):
    """
    Функция парсит данные с сайта МИРЭА и возвращает
    массив данных со специальностями и местами
    """
    ...


def get_data_urfu_parse(debug=False) -> dict:
    """
    Функция парсит данные с сайта УРФУ и возвращает
    массив данных со специальностями и местами
    """
    snils = '15832352164'
    data_nap = {
        '636': {
            'url_get_data': f'https://urfu.ru/api/ratings/info/50/636',
            'url_done': '',
            'upd': '',
            'rtext': '',
            'name_institute': 'Институт новых материалов и технологий',
            'data_rating': {
                '09.03.02 Информационные системы и технологии': {
                    'rating': 0,
                    'priority': 4,
                },
            }
        },
        '642': {
            'url_get_data': f'https://urfu.ru/api/ratings/info/50/642',
            'url_done': '',
            'upd': '',
            'rtext': '',
            'name_institute': 'Институт радиоэлектроники и информационных технологий - РтФ',
            'data_rating': {
                '09.03.01 Информатика и вычислительная техника': {
                    'rating': 0,
                    'priority': 3,
                },
                '09.03.03 Прикладная информатика': {
                    'rating': 0,
                    'priority': 6,
                },
                '09.03.04 Программная инженерия': {
                    'rating': 0,
                    'priority': 1,
                },
            }
        },
        '648': {
            'url_get_data': f'https://urfu.ru/api/ratings/info/50/648',
            'url_done': '',
            'upd': '',
            'rtext': '',
            'name_institute': 'Институт экономики и управления',
            'data_rating': {
                '38.03.05 Бизнес-информатика': {
                    'rating': 0,
                    'priority': 2,
                },
            }
        },
        '644': {
            'url_get_data': f'https://urfu.ru/api/ratings/info/50/644',
            'url_done': '',
            'upd': '',
            'rtext': '',
            'name_institute': 'Физико-технологический институт',
            'data_rating': {
                '09.03.02 Информационные системы и технологии': {
                    'rating': 0,
                    'priority': 5,
                },
            }
        },
    }
    
    # Получаем готовые ссылки и ответ в виде html разметки
    for inst in data_nap:
        response = requests.get(
            url=data_nap[inst]['url_get_data'],
            headers={'user-agent': f'{ua.random}'}
        ).json()
        data_nap[inst]['url_done'] = f'https://urfu.ru{response["url"]}'
        data_nap[inst]['upd'] = response["updatedAt"]
        response = requests.get(
            url=data_nap[inst]['url_done'],
            headers={'user-agent': f'{ua.random}'}
        )
        response.encoding = 'utf-8'
        data_nap[inst]['rtext'] = response.text
    
    # Парсим html разметку с помощью bs4
    for inst in data_nap:
        soup = BeautifulSoup(data_nap[inst]['rtext'], 'html.parser')
        abits_all = soup.find_all('tr', class_='tr-odd') + \
            soup.find_all('tr', class_='tr-even')
        for abit in abits_all:
            abit_temp_data = []
            for elem in abit.descendants:
                if elem.name is not None:
                    abit_temp_data.append(elem.text)
            try:
                if abit_temp_data[1] == snils:
                    for spec in data_nap[inst]['data_rating']:
                        if int(data_nap[inst]['data_rating'][spec]['priority']) \
                            == int(abit_temp_data[3]):
                                data_nap[inst]['data_rating'][spec]['rating'] = int(abit_temp_data[0])
            except Exception as e:
                print(e)
    
    return data_nap


def get_data_agtu_parse(debug=False):
    """
    Функция парсит данные с сайта АГТУ и возвращает
    массив данных со специальностями и местами
    """
    ...
    

if __name__ == '__main__':
    st = time.time()
    get_data_urfu_parse()
    print(f'Секунд: {round(time.time() - st, 2)}')