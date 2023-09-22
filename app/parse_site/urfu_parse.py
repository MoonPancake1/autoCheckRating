"""
Check my rating to HSU - модуль для парсинга данных с сайта urfu.ru
"""

import requests
import threading
from bs4 import BeautifulSoup

from fake_useragent import UserAgent
from app.logger.logger import logger

ua = UserAgent()


class SpecUrfu(threading.Thread):
    
    def __init__(self, url: str, number_spec: int,
                 name_institute: str,
                 data_rating: dict) -> None:
        threading.Thread.__init__(self)
        self.number_spec = number_spec
        self.url_get_data = url
        self.url_done = ''
        self.upd = ''
        self.rtext = ''
        self.name_institute = name_institute
        self.data_rating = data_rating
        self.snils = ''
    
    
    def run(self) -> None:
        """
        Метод парсит данные с сайта urfu.ru
        """
        # Получаем ссылку для получения ответа
        
        try:
            self.get_url_urfu_parse()
        except Exception as e:
            logger.error(f"В процессе получения urls с сайта urfu.ru произошла ошибка!")
            logger.error(f"Ошибка: {e}")
            logger.error(f"Производится ещё одна попытка...")
            self.get_url_urfu_parse()
        
        # Делаем запрос по выданному url
        
        try:
            self.get_answ_urfu_parse()
        except Exception as e:
            logger.error(f"В процессе получения ответа с данными с сайта urfu.ru произошла ошибка!")
            logger.error(f"Ошибка: {e}")
            logger.error(f"Производится ещё одна попытка...")
            self.get_answ_urfu_parse()
        
        # Парсим ответ с помощью bs4
        
        try:
            self.parse_answ_urfu_parse()
        except Exception as e:
            logger.error(f"В процессе парсинга данных с сайта urfu.ru произошла ошибка!")
            logger.error(f"Ошибка: {e}")
            logger.error(f"Производится ещё одна попытка...")
            self.parse_answ_urfu_parse()
    
    
    def get_url_urfu_parse(self) -> None:
        response = requests.get(
                url=self.url_get_data,
                headers={'user-agent': f'{ua.random}'}
            ).json()
        self.url_done = f'https://urfu.ru{response["url"]}'
        self.upd = response["updatedAt"]
    
    
    def get_answ_urfu_parse(self) -> None:
        response = requests.get(
                url=self.url_done,
                headers={'user-agent': f'{ua.random}'}
            )
        response.encoding = 'utf-8'
        self.rtext = response.text
    
    
    def parse_answ_urfu_parse(self) -> None:
        soup = BeautifulSoup(self.rtext, 'html.parser')
        abits_all = soup.find_all('tr', class_='tr-odd') + \
            soup.find_all('tr', class_='tr-even')
        for abit in abits_all:
            abit_temp_data = []
            for elem in abit.descendants:
                if elem.name is not None:
                    abit_temp_data.append(elem.text)
            
            if abit_temp_data[1] == self.snils:
                for spec in self.data_rating:
                    if int(self.data_rating[spec]['priority']) \
                        == int(abit_temp_data[3]):
                            self.data_rating[spec]['rating'] = \
                                int(abit_temp_data[0])
