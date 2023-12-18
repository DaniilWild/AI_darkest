from get_screen import capture_window, clear_caсhe
from mouse_input import get_window_param, mouse_click
from get_area import get_string_from_img, convert_special_string

import cv2
import time
from pynput.mouse import Button, Controller

buffer_filename = 'venv/buffer.jpg'

# обьекты на которые нужно кликнуть прежде чем считывать информацию
dinamic_coord_values_in_game = {
    'teammates_hp_stress': {
        'type': 'repeated',
        'img_coord': [200, 690, 150, 60],
        'mouse_coord': [270, 765],
        'count_repeated': 4,
        'step_repeated': 170
    },
}

def get_teammates(game_montior_params):
    area_name = 'teammates_hp_stress'

    # считаем параметры области
    x_img, y_img, weight_img, height_img = dinamic_coord_values_in_game[area_name]['img_coord'][:]
    x_mouse, y_mouse = dinamic_coord_values_in_game[area_name]['mouse_coord'][:]

    count_repeated = dinamic_coord_values_in_game[area_name]['count_repeated']
    x_step = dinamic_coord_values_in_game[area_name]['step_repeated']

    teammates_status = {}

    mouse_click(game_montior_params, mouse_obj, x_mouse, y_mouse)
    mouse_click(game_montior_params, mouse_obj, x_mouse, y_mouse)
    for i in range(count_repeated):
        mouse_click(game_montior_params, mouse_obj, x_mouse, y_mouse)
        cv2.waitKey(50)

        succes, img = capture_window()
        crop_img = img[y_img: y_img + height_img, x_img: x_img + weight_img]
        clear_string = get_string_from_img(crop_img)

        try:
            person_status = {}
            for status in clear_string.split('\n')[:2]:
                status = status.replace('%', '').replace(':', '')
                status_name, value = status.replace('%', '').split()[:2]
                person_status[status_name] = convert_special_string('fraction', value)
            teammates_status[f'person_{i}'] = person_status

        except:

            cv2.namedWindow('111')
            cv2.moveWindow('111', 100, 100)
            cv2.imshow('111', crop_img)
            cv2.waitKey(0)


        x_img += x_step
        x_mouse += x_step
    return teammates_status



class Group:


class Player:
    def __init__(self, HP, stress,
                 class_person,
                 teammates_status):

        # главные параметры
        self.HP = HP
        self.stress = stress

        self.class_person = class_person

        # второстепенные показатели
        self.status = teammates_status
        self.def_level = 1
        self.attack_level = 1

        # что нужно нам в моменте
        self.action_point = True
        self.active = False





game_montior_params = get_window_param()
mouse_obj = Controller()




prev = time.time()
if __name__ == "__main__":
    clear_caсhe()

    fps = 10

    while True:
        time_elapsed = time.time() - prev



        if time_elapsed > 1.0 / fps:
            prev = time.time()

            print(get_teammates(game_montior_params))

        key = cv2.waitKey(200)
        if key == 27:
            break