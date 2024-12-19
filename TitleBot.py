import cv2
import pyautogui as ptg
import numpy as np
import time

# Пороговое значение для поиска совпадения
threshold = 0.8

# Загружаем шаблоны изображений
scientist_template = cv2.imread(r'C:\Users\rusbo\PycharmProjects\titlebot\img\scientist.png', cv2.IMREAD_GRAYSCALE)
justice_template = cv2.imread(r'C:\Users\rusbo\PycharmProjects\titlebot\img\justice.png', cv2.IMREAD_GRAYSCALE)
duke_template = cv2.imread(r'C:\Users\rusbo\PycharmProjects\titlebot\img\duke.png', cv2.IMREAD_GRAYSCALE)
architect_template = cv2.imread(r'C:\Users\rusbo\PycharmProjects\titlebot\img\architech.png', cv2.IMREAD_GRAYSCALE)
chat_icon_template = cv2.imread(r'C:\Users\rusbo\PycharmProjects\titlebot\img\msg.png', cv2.IMREAD_GRAYSCALE)
title_icon_template = cv2.imread(r'C:\Users\rusbo\PycharmProjects\titlebot\img\titl.png', cv2.IMREAD_GRAYSCALE)

# Функция для поиска изображения на экране
def find_on_screen(template):
    try:
        screenshot = ptg.screenshot()
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= threshold:
            return max_loc  # Возвращаем координаты найденного изображения
        else:
            return None  # Если изображение не найдено
    except Exception as err:
        print(f"Ошибка при поиске изображения: {err}")
        return None

# Функция 1
def perform_actions():
    found_any = False  # Флаг для отслеживания, найден ли элемент

    # Открытие чата при необходимости
    chat_position = find_on_screen(chat_icon_template)
    if chat_position:
        print(f"Чат найден по координатам: {chat_position}")
        ptg.click(chat_position[0] + chat_icon_template.shape[1] // 2,
                  chat_position[1] + chat_icon_template.shape[0] // 2)
        print(f"Клик по иконке чата выполнен.")
        found_any = True
        time.sleep(0.5)
    else:
        print("Иконка чата не найдена.")

    # Поиск титула "duke"
    duke_position = find_on_screen(duke_template)
    if duke_position:
        print(f"Титул 'duke' найден по координатам: {duke_position}")
        ptg.click(duke_position[0] + duke_template.shape[1] // 2,
                  duke_position[1] + duke_template.shape[0] // 2)
        print(f"Клик по титулу 'duke' выполнен.")
        found_any = True
        time.sleep(1)
        ptg.click(432, 277)
        time.sleep(3)
    else:
        print("Титул 'duke' не найден.")

    # Поиск иконки титула
    title_icon_position = find_on_screen(title_icon_template)
    if title_icon_position:
        print(f"Иконка титула найдена по координатам: {title_icon_position}")
        ptg.click(title_icon_position[0] + title_icon_template.shape[1] // 2,
                  title_icon_position[1] + title_icon_template.shape[0] // 2)
        found_any = True
        time.sleep(1)
        ptg.click(350, 300)
        time.sleep(1)
        ptg.click(430, 460)
    else:
        print("Иконка титула не найдена.")

    return found_any  # Возвращаем результат

# Функция 2
def perform_actions_2():
    found_any = False

    chat_position = find_on_screen(chat_icon_template)
    if chat_position:
        print(f"Чат найден по координатам: {chat_position}")
        ptg.click(chat_position[0] + chat_icon_template.shape[1] // 2,
                  chat_position[1] + chat_icon_template.shape[0] // 2)
        print(f"Клик по иконке чата выполнен.")
        found_any = True
        time.sleep(0.5)
    else:
        print("Иконка чата не найдена.")

    justice_position = find_on_screen(justice_template)
    if justice_position:
        print(f"Титул 'justice' найден по координатам: {justice_position}")
        ptg.click(justice_position[0] + justice_template.shape[1] // 2,
                  justice_position[1] + justice_template.shape[0] // 2)
        print(f"Клик по титулу 'justice' выполнен.")
        found_any = True
        time.sleep(1)
        ptg.click(432, 277)
        time.sleep(3)
    else:
        print("Титул 'justice' не найден.")

    title_icon_position = find_on_screen(title_icon_template)
    if title_icon_position:
        print(f"Иконка титула найдена по координатам: {title_icon_position}")
        ptg.click(title_icon_position[0] + title_icon_template.shape[1] // 2,
                  title_icon_position[1] + title_icon_template.shape[0] // 2)
        found_any = True
        time.sleep(1)
        ptg.click(200, 300)
        time.sleep(1)
        ptg.click(430, 460)
    else:
        print("Иконка титула не найдена.")

    return found_any

# Функция 3
def perform_actions_3():
    found_any = False

    chat_position = find_on_screen(chat_icon_template)
    if chat_position:
        print(f"Чат найден по координатам: {chat_position}")
        ptg.click(chat_position[0] + chat_icon_template.shape[1] // 2,
                  chat_position[1] + chat_icon_template.shape[0] // 2)
        print(f"Клик по иконке чата выполнен.")
        found_any = True
        time.sleep(0.5)
    else:
        print("Иконка чата не найдена.")

    scientist_position = find_on_screen(scientist_template)
    if scientist_position:
        print(f"Титул 'scientist' найден по координатам: {scientist_position}")
        ptg.click(scientist_position[0] + scientist_template.shape[1] // 2,
                  scientist_position[1] + scientist_template.shape[0] // 2)
        print(f"Клик по титулу 'scientist' выполнен.")
        found_any = True
        time.sleep(1)
        ptg.click(432, 277)
        time.sleep(3)
    else:
        print("Титул 'scientist' не найден.")

    title_icon_position = find_on_screen(title_icon_template)
    if title_icon_position:
        print(f"Иконка титула найдена по координатам: {title_icon_position}")
        ptg.click(title_icon_position[0] + title_icon_template.shape[1] // 2,
                  title_icon_position[1] + title_icon_template.shape[0] // 2)
        found_any = True
        time.sleep(1)
        ptg.click(660, 300)
        time.sleep(1)
        ptg.click(430, 460)
    else:
        print("Иконка титула не найдена.")

    return found_any

# Функция 4
def perform_actions_4():
    found_any = False

    chat_position = find_on_screen(chat_icon_template)
    if chat_position:
        print(f"Чат найден по координатам: {chat_position}")
        ptg.click(chat_position[0] + chat_icon_template.shape[1] // 2,
                  chat_position[1] + chat_icon_template.shape[0] // 2)
        print(f"Клик по иконке чата выполнен.")
        found_any = True
        time.sleep(0.5)
    else:
        print("Иконка чата не найдена.")

    architect_position = find_on_screen(architect_template)
    if architect_position:
        print(f"Титул 'architect' найден по координатам: {architect_position}")
        ptg.click(architect_position[0] + architect_template.shape[1] // 2,
                  architect_position[1] + architect_template.shape[0] // 2)
        print(f"Клик по титулу 'architect' выполнен.")
        found_any = True
        time.sleep(1)
        ptg.click(432, 277)
        time.sleep(3)
    else:
        print("Титул 'architect' не найден.")

    title_icon_position = find_on_screen(title_icon_template)
    if title_icon_position:
        print(f"Иконка титула найдена по координатам: {title_icon_position}")
        ptg.click(title_icon_position[0] + title_icon_template.shape[1] // 2,
                  title_icon_position[1] + title_icon_template.shape[0] // 2)
        found_any = True
        time.sleep(1)
        ptg.click(510, 300)
        time.sleep(1)
        ptg.click(430, 460)
    else:
        print("Иконка титула не найдена.")

    return found_any

# Главный цикл
if __name__ == "__main__":
    while True:
        found_any_in_all = False  # Общий флаг

        try:
            if perform_actions():
                found_any_in_all = True
            time.sleep(10)

            if perform_actions_2():
                found_any_in_all = True
            time.sleep(10)

            if perform_actions_3():
                found_any_in_all = True
            time.sleep(10)

            if perform_actions_4():
                found_any_in_all = True
            time.sleep(10)

            if not found_any_in_all:
                print("Ни один элемент не найден, возвращаемся в начало.")
                continue  # Продолжаем главный цикл

            print("Пауза перед следующим циклом.")
            time.sleep(80)  # Пауза, если было найдено совпадение

        except Exception as er:
            print(f"Общая ошибка программы: {er}")
            time.sleep(1)  # Небольшая пауза перед попыткой снова
