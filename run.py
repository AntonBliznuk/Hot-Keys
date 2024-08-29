from pynput import keyboard

from app.Browser import open_my_url
from app.dbManage import insert_url, select_url, show_urls
from app.show_hot_keys import show
from app.YouTubeDownloader import downloader

current_keys = set()
command_limit = 0


def on_press(key):
    """
    This function is called every time a key is pressed.
    It updates the set of currently pressed keys and performs actions
    based on specific key combinations.

    Arguments:
    key -- the key that was pressed
    """
    global command_limit
    current_keys.add(key)

    # Check for the combination: Cmd + '0'
    if all(k in current_keys for k in [keyboard.KeyCode.from_char('0'), keyboard.Key.cmd]) and command_limit < 1:
        print("Binds is offline")
        command_limit += 1
        return False

    # Check for the combination: Ctrl + 's'
    elif all(k in current_keys for k in [keyboard.KeyCode.from_char('j'), keyboard.Key.ctrl]) and command_limit < 1:
        # Show the hotkey management interface
        show()
        command_limit += 1
        return

    # Check for the combination: Ctrl + 'd'
    elif all(k in current_keys for k in [keyboard.KeyCode.from_char('d'), keyboard.Key.ctrl]) and command_limit < 1:
        # Trigger the YouTube downloader
        downloader()
        command_limit += 1
        return

    # Check for the combination: Alt + Ctrl
    elif all(k in current_keys for k in [keyboard.Key.alt, keyboard.Key.ctrl]) and command_limit < 1:
        # Show the list of URLs
        show_urls()
        command_limit += 1
        return

    # Define useful URL shortcuts
    useful_urls = {
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('1')): 'https://chatgpt.com/',
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('2')): 'https://music.youtube.com/playlist?list=LM',
        (keyboard.Key.cmd, keyboard.KeyCode.from_char('3')): 'https://www.deepl.com/ru/translator',
        (keyboard.Key.cmd,
         keyboard.KeyCode.from_char('4')): 'https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl'
    }

    # Check for URL shortcuts and open the corresponding URL
    for keys, url in useful_urls.items():
        if all(k in current_keys for k in keys) and command_limit < 1 and len(current_keys) == 2:
            open_my_url(url)
            command_limit += 1
            return

    # Define shortcuts for inserting URLs into the database
    remember_combs = {
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('1')): 1,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('2')): 2,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('3')): 3,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('4')): 4,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('r'), keyboard.KeyCode.from_char('5')): 5
    }

    # Check for insert URL shortcuts and add the URL to the database
    for keys, index in remember_combs.items():
        if all(k in current_keys for k in keys) and command_limit < 1:
            insert_url(index)
            command_limit += 1
            return

    # Define shortcuts for selecting URLs from the database
    open_combs = {
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('1')): 1,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('2')): 2,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('3')): 3,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('4')): 4,
        (keyboard.Key.ctrl, keyboard.KeyCode.from_char('m'), keyboard.KeyCode.from_char('5')): 5
    }

    # Check for select URL shortcuts and retrieve the corresponding URL from the database
    for keys, index in open_combs.items():
        if all(k in current_keys for k in keys) and command_limit < 1:
            select_url(index)
            command_limit += 1
            return


def on_release(key):
    """
    This function is called every time a key is released.
    It resets the state of the pressed keys and command limit.

    Arguments:
    key -- the key that was released
    """
    global command_limit
    global current_keys

    current_keys = set()
    command_limit = 0


# Start listening for keyboard events
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
print("Press ---> ctrl + j")
listener.run()

