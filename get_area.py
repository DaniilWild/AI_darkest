import cv2
import pytesseract
import pandas
from pytesseract import Output


img = cv2.imread('person_hp.jpg')
img = cv2.imread('enemy_hp.jpg')

coord_values_in_game = {
    'character_class': {
        'type': 'string',
        'coord': [640, 1570, 300, 60]
    },
    'character_hp': {
        'type': 'fraction',
        'coord': [600, 1700, 250, 50]
    },
    'character_stress': {
        'type': 'fraction',
        'coord': [600, 1750, 250, 50]
    },

    'enemy_class': {
        'type': 'string',
        'coord': [1800, 1500, 800, 120]
    },
    'enemy_hp': {
        'type': 'fraction',
        'coord': [2710, 1530, 170, 50]
    },
    'enemy_status': {
        'type': 'group_status',
        'coord': [1910, 1830, 400, 200]
    },

    'battle_step': {
       'type': 'small_value',
       'coord': [1690, 330, 70, 70]
    },

}
coord_values_in_game = {
    'character_class': {
        'type': 'string',
        'coord': [360, 856, 160, 40]
    },
    'character_status': {
        'type': 'group_status',
        'coord': [290, 990, 175, 230]
    },

    'enemy_class': {
        'type': 'string',
        'coord': [1000, 830, 280, 40]
    },
    'enemy_hp': {
        'type': 'fraction',
        'coord': [1506, 830, 100, 40]
    },
    'enemy_status': {
        'type': 'group_status',
        'coord': [1060, 1000, 200, 120]
    },

    'battle_step': {
       'type': 'small_value',
       'coord': [945, 165, 35, 40]
    },

}


def convert_special_string(string_type, sting):
    clear_string = sting.rstrip().strip()



    # в зависимости от строки будем по разному ее обрабатывать
    if string_type == 'small_value':
        return_string = int(clear_string)
    elif string_type == 'value':
        return_string = float(clear_string)
    elif string_type == 'string':
        return_string = clear_string.lower()
    elif string_type == 'group_status':
        return_string = {}
        for status in clear_string.split('\n'):
            status = status.replace('%', '').replace(':', '')
            status_name, value = status.split()[:2]

            try:
                if '.' in value:
                    return_string[status_name] = int(value.replace('.',''))/10
                else:
                    return_string[status_name] = int(value)
            except:
                print(f'{status_name} - error read')
    else:
        assert "Незнакомый тип данных для чтения"

    return return_string

def get_string_from_img(crop_img):
    # настройки считывания строки
    custom_oem_psm_config = r'--oem 3 --psm 6'
    read_string = pytesseract.image_to_string(crop_img, lang='eng', config=custom_oem_psm_config)
    return read_string


def image_to_text(img, area_name):
    # считаем параметры области
    string_type = coord_values_in_game[area_name]['type']
    x, y, weight, height = coord_values_in_game[area_name]['coord'][:]


    # вырежим область и прочитаем информацию в ней
    crop_img = img[y: y+height, x: x+weight]
    read_string = get_string_from_img(crop_img)

    # уникальный тип с двумя числами
    if string_type == 'fraction':
        curr_value, max_value = read_string.split('/')[:2]
        return int(curr_value), int(max_value)

    print(read_string)
    return_string = convert_special_string(string_type, read_string)

    return return_string

if __name__ == "__main__":
    # тип где написано два числа через дробь
    for area_name in ['enemy_hp']: # 'character_hp', 'character_stress',
        a, b = image_to_text(img, area_name)
        print(area_name, a, 'из', b)

    # тип где одна текстовая строка
    for area_name in ['enemy_class', 'character_class']:
        string = image_to_text(img, area_name)
        print(area_name, 'это', string)

    # тип где только одно число
    for area_name in ['battle_step']:
        string = image_to_text(img, area_name)
        print(area_name, 'это', string)

    # коомбинированный тип где есть несколько строчек с текстом и числами
    for area_name in ['enemy_status', 'character_status']:
        string = image_to_text(img, area_name)
        print('\n',area_name)
        for key, value in string.items():
            print("{0}: {1}".format(key, value))