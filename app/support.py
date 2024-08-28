import time
from pynput.keyboard import Controller, Key
import pyperclip

def copy_current_link():
    controller = Controller()
    ###
    controller.press(Key.cmd)
    time.sleep(0.01)
    controller.press('l')

    time.sleep(0.1)

    controller.release(Key.cmd)
    time.sleep(0.01)
    controller.release('l')
    ###
    controller.press(Key.cmd)
    time.sleep(0.01)
    controller.press('c')

    time.sleep(0.2)

    controller.release(Key.cmd)
    time.sleep(0.01)
    controller.release('c')
    ###

    time.sleep(0.2)

    controller.press(Key.esc)
    time.sleep(0.01)
    controller.release(Key.esc)

    time.sleep(0.01)

    controller.press(Key.esc)
    controller.release(Key.esc)

    ###

    return pyperclip.paste()

def search_in_string(s, h):
    for i in range(0, len(s) - len(h) + 1, 1):

        text = ''

        for j in range(i, len(h) + i, 1):
            text += s[j]

        is_find = True

        for k in range(0, len(h), 1):
            if text[k] != h[k]:
                is_find = False
                break
            else:
                continue

        if is_find:
            return True
        else:
            continue


if __name__ == '__main__':
    print(search_in_string("ddddddrezka", 'rezkad'))