"""
Check my rating to HSU - модуль для парсинга данных с сайтов
ВУЗов
"""
import time


def get_data_spbpu_parse(debug=False):
    """
    Функция парсит данные с сайта СПбПУ и возвращает
    массив данных со специальностями и местами
    """
    
    logger.debug(f"Пользователь начал парсинг мест с сайта enroll.spbstu.ru")
    
    initial_data = get_full_data_spbpu_for_parse()
    
    threads = [ SpecSPbPU(
        name=spec,
        url=initial_data[spec]['url_parse'],
        priority=initial_data[spec]['priority'],
        rating=initial_data[spec]['rating'],
        total_budget_position=initial_data[spec]['total_budget_position'],
        passing_points=initial_data[spec]['passing_points']
    ) for spec in initial_data]
    
    data_req = []
    
    logger.debug(f"Парсинг в процессе!")
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    for thread in threads:
        data_req.append((
            thread.priority,
            thread.rating,
            thread.name,
            thread.total_budget_position,
            thread.passing_points,
        ))
    
    logger.info(f"Парсинг сайта enroll.spbstu.ru прошёл успешно!")
    
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
    logger.debug(f"Пользователь начал парсинг мест с сайта mirea.ru")
    
    initial_data = get_full_data_mirea_for_parse()
    
    threads = [ SpecMirea(
        name=spec,
        url=initial_data[spec]['url_parse'],
        priority=initial_data[spec]['priority'],
        rating=initial_data[spec]['rating'],
        total_budget_position=initial_data[spec]['total_budget_position'],
        passing_points=initial_data[spec]['passing_points']
    ) for spec in initial_data]
    
    data_req = []
    
    logger.debug(f"Парсинг в процессе!")
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    for thread in threads:
        data_req.append((
            thread.priority,
            thread.rating,
            thread.name,
            thread.total_budget_position,
            thread.passing_points,
        ))
    
    logger.info(f"Парсинг сайта mirea.ru прошёл успешно!")
    
    return data_req


def get_data_urfu_parse(debug=False) -> dict:
    """
    Функция парсит данные с сайта УРФУ и возвращает
    массив данных со специальностями и местами
    """
    
    logger.debug(f"Пользователь начал парсинг мест с сайта urfu.ru")

    initial_data = [
        ('https://urfu.ru/api/ratings/info/50/636',
         636, 'Институт новых материалов и технологий',
         {
            '09.03.02 Информационные системы и технологии': {
                'rating': 0,
                'priority': 4,
                'budget_places': 29,
            },
         }),
        ('https://urfu.ru/api/ratings/info/50/642',
         642, 'Институт радиоэлектроники и информационных технологий - РтФ',
         {
            '09.03.01 Информатика и вычислительная техника': {
                'rating': 0,
                'priority': 3,
                'budget_places': 78,
            },
            '09.03.03 Прикладная информатика': {
                'rating': 0,
                'priority': 6,
                'budget_places': 140,
            },
            '09.03.04 Программная инженерия': {
                'rating': 0,
                'priority': 1,
                'budget_places': 161,
            }, 
         }),
        ('https://urfu.ru/api/ratings/info/50/648',
         648, 'Институт экономики и управления',
         {
            '38.03.05 Бизнес-информатика': {
                'rating': 0,
                'priority': 2,
                'budget_places': 14,
            },
         }),
        ('https://urfu.ru/api/ratings/info/50/644',
         644, 'Физико-технологический институт',
         {
            '09.03.02 Информационные системы и технологии': {
                'rating': 0,
                'priority': 5,
                'budget_places': 34,
            },
         }),
    ]
    
    logger.debug(f"Подготовка к парсингу...")
    
    threads = [ SpecUrfu(
        url=data[0],
        number_spec=data[1],
        name_institute=data[2],
        data_rating=data[3]
    )  for data in initial_data ]
    
    data_req = []
    
    logger.debug(f"Парсинг в процессе!")
    
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
    for thread in threads:
        for spec in thread.data_rating:
            data_req.append((
                thread.data_rating[spec]['priority'],
                thread.data_rating[spec]['rating'],
                spec,
                thread.data_rating[spec]['budget_places']
            ))
    
    logger.info(f"Парсинг сайта urfu.ru прошёл успешно!")
    
    return data_req


def get_data_agtu_parse(debug=False):
    """
    Функция парсит данные с сайта АГТУ и возвращает
    массив данных со специальностями и местами
    """
    ...
    

if __name__ == '__main__':
    from parse_site.urfu_parse import *
    from parse_site.mirea_parse import *
    from parse_site.spbpu_parse import *
    
    st = time.time()
    get_data_mirea_parse()
    print(f'Секунд: {round(time.time() - st, 2)}')
else:
    from app.parse_site.urfu_parse import *
    from app.parse_site.mirea_parse import *
    from app.parse_site.spbpu_parse import *