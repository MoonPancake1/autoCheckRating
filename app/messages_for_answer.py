"""
Check my rate to HSU - Модуль для объявления всех сообщений в боте
"""

START_MESSAGE = """
Доброго времени суток, Владислав!
"""

MENU_MESSAGE = """
Какой ВУЗ проверить?
"""

def generate_spbpu_message(data_parse: list = [('test', 281), ('test2', 190)]):
    spbpu_message = '\n'.join([f"{i[0]}: {i[1]} место" for i in data_parse])
    return spbpu_message


def generate_urfu_message(data_parse: dict) -> str:
    
    temp_answ = []
    
    for inst in data_parse:
        for spec in data_parse[inst]['data_rating']:
            prior = data_parse[inst]['data_rating'][spec]['priority']
            rating = data_parse[inst]['data_rating'][spec]['rating']
            temp_answ.append((prior, rating, spec))
    
    temp_answ = sorted(temp_answ, key=lambda x: x[0])
    
    temp_answ = [f"*{data[0]}.* {data[2]}: _{data[1]}_ место 🔥" 
                 for data in temp_answ]
    
    urfu_message = 'Вот все направления: \n\n'
    urfu_message += '\n'.join(temp_answ)
                
    return urfu_message


if __name__ == '__main__':
    print(generate_spbpu_message())