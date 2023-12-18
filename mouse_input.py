#import mouse  # неподдерживается в системе MacOS
from pynput.mouse import Button, Controller
from screeninfo import get_monitors
import cv2



# положение вторго монитора
def get_window_param(monitor_orientation_x = 'down', monitor_number_activ = 1):

    # получение параметров всех мониторов
    monitor_params, monitor_number = {}, 0
    for monitor in get_monitors():
        monitor_params[monitor_number] = {'x': monitor.x, 'y': monitor.y,
                                          'width': monitor.width, 'height': monitor.height}
        monitor_number += 1
    game_montior_params = monitor_params[monitor_number_activ]

    # если монитор снизу то координаты верха будет равна длине монитора
    if monitor_orientation_x == 'down':
        game_montior_params['y'] = -game_montior_params['height']

    return game_montior_params

def mouse_click(game_montior_params, mouse,
                x_coords, y_coords):
    # если быстро двигать мышкой и нажимать игра не вспринимает
    click_timer = 5

    mouse_x = game_montior_params['x'] + x_coords
    mouse_y = game_montior_params['y'] + y_coords
    mouse.position = (mouse_x, mouse_y)

    cv2.waitKey(click_timer)
    mouse.press(Button.left)
    mouse.release(Button.left)


if __name__ == "__main__":
    # два обьекта монитор и мышка
    game_montior_params = get_window_param()
    mouse_obj = Controller()


    x_start = 270
    x_step = 170

    for i in range(4):
        mouse_click(game_montior_params, mouse_obj, x_start, 765)
        cv2.waitKey(500)

        x_start += x_step

    print('Now we have moved it to {0}'.format(
        mouse_obj.position))