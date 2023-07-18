"""
Check my rating to HSU - модуль для парсинга 
данных с сайта enroll.spbstu.ru
"""

import requests
import threading

from fake_useragent import UserAgent

ua = UserAgent()


class SpecSPbPU(threading.Thread):
    
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
        self.url = url,
        self.priority = priority
        self.rating = rating
        self.total_budget_position = total_budget_position
        self.passing_points = passing_points
        self.rjson = {}
        self.snils = '158-323-521 64'
    
    def run(self) -> None:
        """
        Метод парсит данные с сайта spbpu.ru
        """
        
        # Получаем ответ от spbpu
        try:
            self.get_answ_spbpu_parse()
        except Exception as e:
            logger.error('Произошла ошибка!')
            logger.error(f'Ошибка: {e}')
            logger.debug('Производится повторный запрос...')
            self.get_answ_spbpu_parse()
        
        # Парсим полученные данные
        try:
            self.parse_answ_spbpu_parse()
        except Exception as e:
            logger.error('Произошла ошибка!')
            logger.error(f'Ошибка: {e}')
            logger.debug('Производится повторный запрос...')
            self.parse_answ_spbpu_parse()
    
    
    def get_answ_spbpu_parse(self) -> None:
        response = requests.get(
                url=self.url[0],
                headers={'user-agent': f'{ua.random}'}
            )
        self.rjson = response.json()
    
    
    def parse_answ_spbpu_parse(self) -> None:    
        self.total_budget_position = self.rjson['directionCapacity']
        abits_has_Original = []
        
        for ind, abit in enumerate(self.rjson['list']):
            if abit['userSnils'] == '158-323-521 64':
                self.rating = ind + 2
            if abit['hasOriginalDocuments'] and \
                (len(abits_has_Original) < \
                    self.total_budget_position):
                abits_has_Original.append(abit)
        
        self.passing_points = get_passing_points(abits_has_Original)
                    

def get_passing_points(abits_has_Original: list) -> int:
    """
    Функция парсит абитуриентов, которые подали оригинал документа
    и высчитывает проходной балл на эту специальность
    """
    
    return abits_has_Original[-1]['fullScore']
        


def get_full_data_spbpu_for_parse() -> list:
    """
    Функция генерирует данные для создания классов со специальностями
    """
    
    full_data_spbpu = {
        '01.03.02 Прикладная математика и информатика': {
          'priority': 1,
          'uniq_number': '23-26191',
          'url_parse': 'https://enroll.spbstu.ru/applications-manager/api/v1/admission-list/form-rating?applicationEducationLevel=BACHELOR&directionEducationFormId=2&directionId=569',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
        '02.03.01 Математика и компьютерные науки': {
          'priority': 2,
          'uniq_number': '23-26191',
          'url_parse': 'https://enroll.spbstu.ru/applications-manager/api/v1/admission-list/form-rating?applicationEducationLevel=BACHELOR&directionEducationFormId=2&directionId=604',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
        '27.03.05 Инноватика': {
          'priority': 3,
          'uniq_number': '23-26191',
          'url_parse': 'https://enroll.spbstu.ru/applications-manager/api/v1/admission-list/form-rating?applicationEducationLevel=BACHELOR&directionEducationFormId=2&directionId=1369',
          'rating': 0,
          'total_budget_position': 0,
          'passing_points': 0,
        },
    }
    
    return full_data_spbpu


if __name__ == '__main__':
    from logger.logger import logger
    get_full_data_spbpu_for_parse()
    
else:
    from app.logger.logger import logger