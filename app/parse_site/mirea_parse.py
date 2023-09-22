"""
Check my rating to HSU - модуль для парсинга данных с сайта priem.mirea.ru
"""

import requests
import threading
from bs4 import BeautifulSoup

from fake_useragent import UserAgent

ua = UserAgent()


class SpecMirea(threading.Thread):
    
    def __init__(self,
                 name: str, 
                 url: str, 
                 priority: int,
                 rating: int,
                 total_budget_position: int,
                 passing_points: int
                 ) -> None:
        threading.Thread.__init__(self)
        self.name = name
        self.priority = priority
        self.url = url
        self.rating = rating
        self.total_budget_position = total_budget_position
        self.passing_points = passing_points
        self.rtext = ''
        self.snils = ''
    
    
    def run(self) -> None:
        """
        Метод парсит данные с сайта mirea.ru
        """
        
        # Получаем ответ от mirea
        try:
            self.get_answ_mirea_parse()
        except Exception as e:
            logger.error('Произошла ошибка!')
            logger.error(f'Ошибка: {e}')
            logger.debug('Производится повторный запрос...')
            self.get_answ_mirea_parse()
        
        # Парсим полученные данные
        try:
            self.parse_answ_mirea_parse()
        except Exception as e:
            logger.error('Произошла ошибка!')
            logger.error(f'Ошибка: {e}')
            logger.debug('Производится повторный запрос...')
            self.parse_answ_mirea_parse()
            
    
    
    def get_answ_mirea_parse(self) -> None:
        response = requests.get(
                url=self.url,
                headers={'user-agent': f'{ua.random}'}
            )
        response.encoding = 'utf-8'
        self.rtext = response.text
    
    
    def parse_answ_mirea_parse(self) -> None:    
        soup = BeautifulSoup(self.rtext, 'html.parser')
        self.passing_points = soup.find_all('p')[2].text.split()[-1]
        self.total_budget_position = soup.find_all('p')[1].text.split()[-1]
        target_abit = soup.find('tr', id='1771028852693276311')
        
        self.rating = int(target_abit.find_all('td')[0].text)


def get_full_data_mirea_for_parse() -> list:
    """
    Функция генерирует данные для создания классов со специальностями
    """
    url_get_urls = 'https://priem.mirea.ru/accepted-entrants-list/'
    full_data_mirea = {
        '09.03.02 Информационные системы и технологии - Фулстек разработка (ИПТИП)': {
          'priority': 1,
          'uniq_number': 14897,
          'url_parse': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205436693126454',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
        '09.03.02 Информационные системы и технологии (ИРИ)': {
          'priority': 2,
          'uniq_number': 14897,
          'url_parse': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205448598658358',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
        '27.03.03 Системный анализ и управление (ИИИ)': {
          'priority': 3,
          'uniq_number': 14897,
          'url_parse': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205659639258422',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
        '09.03.02 Информационные системы и технологии (ИКБ)': {
          'priority': 4,
          'uniq_number': 14897,
          'url_parse': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205454286134582',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
        '09.03.03 Прикладная информатика (ИИТ)': {
          'priority': 5,
          'uniq_number': 14897,
          'url_parse': 'https://priem.mirea.ru/accepted-entrants-list/personal_code_rating.php?competition=1748205428624334134',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
    }
    
    return full_data_mirea


if __name__ == '__main__':
    from logger.logger import logger
    get_full_data_mirea_for_parse()
    
else:
    from app.logger.logger import logger
