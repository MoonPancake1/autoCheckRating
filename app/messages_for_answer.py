"""
Check my rate to HSU - Модуль для объявления всех сообщений в боте
"""

START_MESSAGE = """
Доброго времени суток, Владислав!
"""

MENU_MESSAGE = """
Какой ВУЗ проверить?
"""

IN_DEVELOPMENT = """
К сожелению эта функция недоступна, вот возможные причины:

1. *ВУЗ* пока не опубликовал списки
2. *ВУЗ* ещё не рассмотрел документы
3. *Функция в процессе разработки*
"""

def generate_spbpu_message(data_parse: list = [('test', 281), ('test2', 190)]):
    spbpu_message = '\n'.join([f"{i[0]}: {i[1]} место" for i in data_parse])
    return spbpu_message


def generate_mirea_message(data_parse: list) -> str:
    
    temp_answ = sorted(data_parse, key=lambda x: x[0])
    
    temp_answ = [f"*{data[0]}.* {data[2]}: _{data[1]}_ место (_Всего_ *{data[3]}* _мест_)🔥" 
                 for data in temp_answ]

    mirea_message = '\n\n'.join(temp_answ)
                
    return mirea_message


def generate_urfu_message(data_parse: list) -> str:
    
    temp_answ = sorted(data_parse, key=lambda x: x[0])
    
    temp_answ = [f"*{data[0]}.* {data[2]}: _{data[1]}_ место (_Всего_ *{data[3]}* _мест_)🔥" 
                 for data in temp_answ]

    urfu_message = '\n\n'.join(temp_answ)
                
    return urfu_message


if __name__ == '__main__':
    print(generate_spbpu_message())