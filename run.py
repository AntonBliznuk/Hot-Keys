from pynput import keyboard

from app.Browser import open_my_url
from app.dbManage import insert_url, select_url, show_urls
from app.show_hot_keys import show
from app.YouTubeDownloader import downloader

current_keys = set()
comand_limit = 0


def on_press(key):
    """
       Основная функция которая вызывается каждый раз при нажатии любой клавиши,
       сохраняет все нажатые клавиши в current_keys и исходя из комбинаций нажатых
       клавиш выполняет определенное действие. 
    """

    global comand_limit
    current_keys.add(key)

    if all(k in current_keys for k in [keyboard.KeyCode.from_char('0'), keyboard.Key.cmd]) and comand_limit < 1:
        print("Binds is offline")
        comand_limit += 1
        return False

    elif all(k in current_keys for k in [keyboard.KeyCode.from_char('s'), keyboard.Key.ctrl]) and comand_limit < 1:
        # Функция которая покажет управление
        show()
        comand_limit += 1
        return
    
    elif all(k in current_keys for k in [keyboard.KeyCode.from_char('d'), keyboard.Key.ctrl]) and comand_limit < 1:
        downloader()
        comand_limit += 1
        return
    
    elif all(k in current_keys for k in [keyboard.Key.alt, keyboard.Key.ctrl]) and comand_limit < 1:
        show_urls()
        comand_limit += 1
        return
        

    useful_urls = {
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('1')): 'https://chatgpt.com/',
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('2')): 'https://music.youtube.com/playlist?list=LM',
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('3')): 'https://www.deepl.com/ru/translator',
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('4')): 'https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl'
    }

    for keys, vals in useful_urls.items():
        if all(k in current_keys for k in keys) and comand_limit < 1 and len(current_keys) == 2:
            open_my_url(vals)
            comand_limit += 1
            return
    
    
    remember_combs = {
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('1')): 1,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('2')): 2,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('3')): 3,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('4')): 4,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('5')): 5
    }

    for keys, vals in remember_combs.items():
        if all(k in current_keys for k in keys) and comand_limit < 1:
            insert_url(vals)
            comand_limit += 1
            return
        
    open_combs = {
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('1')): 1,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('2')): 2,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('3')): 3,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('4')): 4,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('5')): 5
    }

    for keys, vals in open_combs.items():
        if all(k in current_keys for k in keys) and comand_limit < 1:
            select_url(vals)
            comand_limit += 1
            return




def on_release(key):
    """
       Функция которая вызывается каждый раз когда пользователь отжимает любую
       клавиши и збрасывает все пареметры. 
    """

    global comand_limit
    global current_keys

    current_keys = set()
    comand_limit = 0


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
print("Press ---> ctrl + s")
listener.run()
