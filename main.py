import urllib.request
import time
import os
import random

CONTROL_URL = "https://raw.githubusercontent.com/Nadota-cmd/Gemini_telegrambor_constructor/main/trigger.txt"

def run_troll():
    if os.name == 'nt':
        os.system('chcp 65001 > nul')
        os.system('cls')
    else:
        os.system('clear')

    logo = r'''
⣿⣿⣿⠟⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢋⣩⣉⢻⣿⣿
⣿⣿⣿⠀⣿⣶⣕⣈⠹⠿⠿⠿⠿⠟⠛⣛⢋⣰⠣⣿⣿⠀⣿⣿
⣿⣿⣿⡀⣿⣿⣿⣧⢻⣿⣶⣷⣿⣿⣿⣿⣿⣿⠿⠶⡝⠀⣿⣿
⣿⣿⣿⣷⠘⣿⣿⣿⢏⣿⣿⣋⣀⣈⣻⣿⣿⣷⣤⣤⣿⡐⢿⣿
⣿⣿⣿⣿⣆⢩⣝⣫⣾⣿⣿⣿⣿⡟⠿⠿⠦⠀⠸⠿⣻⣿⡄⢻
⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⠇⣼
⣿⣿⣿⣿⣿⣿⡄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣰⣿
⣿⣿⣿⣿⣿⣿⠇⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿
⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿
⣿⣿⣿⣿⠟⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿
⣿⣿⣿⠋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿
⣿⣿⠋⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿
⣿⠏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⢸⣿
⡏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢸⣿
    '''
    # В Windows CMD цвета работают не всегда, поэтому добавим проверку
    if os.name != 'nt':
        print('\033[92m' + logo + '\033[0m')
    else:
        print(logo)
        
    print("\n[ СИСТЕМНОЕ УВЕДОМЛЕНИЕ ]")
    print("Привет от Дарына! Твой комп официально прошел проверку на чувство юмора.")

print("Агент Pando запущен и ждет команды...")

while True:
    try:
        # Добавляем случайное число к ссылке, чтобы GitHub отдавал свежий файл
        no_cache_url = f"{CONTROL_URL}?t={random.random()}"
        with urllib.request.urlopen(no_cache_url) as response:
            status = response.read().decode('utf-8').strip()
            
        if status == "1":
            run_troll()
            break 
    except Exception as e:
        # Если что-то пошло не так (нет инета), просто тихо спим
        pass

    time.sleep(120) # Можно даже раз в 30 сек проверять, на SSD это незаметно
