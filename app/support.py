import time
from pynput.keyboard import Controller, Key
import pyperclip


def copy_current_link():
    """
    Simulates keyboard shortcuts to copy the current URL from the address bar,
    then returns the copied URL from the clipboard.

    Steps:
    1. Presses Cmd + 'l' to focus on the address bar.
    2. Presses Cmd + 'c' to copy the URL to the clipboard.
    3. Presses 'Esc' twice to exit the address bar.
    4. Returns the copied URL from the clipboard.
    """
    controller = Controller()

    # Focus on the address bar by simulating Cmd + 'l'
    controller.press(Key.cmd)
    time.sleep(0.01)
    controller.press('l')
    time.sleep(0.1)
    controller.release(Key.cmd)
    time.sleep(0.01)
    controller.release('l')

    # Copy the URL to the clipboard by simulating Cmd + 'c'
    controller.press(Key.cmd)
    time.sleep(0.01)
    controller.press('c')
    time.sleep(0.2)
    controller.release(Key.cmd)
    time.sleep(0.01)
    controller.release('c')

    # Close the address bar by simulating 'Esc' twice
    time.sleep(0.2)
    controller.press(Key.esc)
    time.sleep(0.01)
    controller.release(Key.esc)
    time.sleep(0.01)
    controller.press(Key.esc)
    controller.release(Key.esc)

    # Return the copied URL from the clipboard
    return pyperclip.paste()


def search_in_string(s, h):
    """
       Searches for the substring 'h' in the string 's'.

       Arguments:
       s -- the string to search in
       h -- the substring to search for

       Returns:
       True if 'h' is found in 's', False otherwise.
       """
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
    # Test the search_in_string function
    print(search_in_string("ddddddrezka", 'rezkad'))