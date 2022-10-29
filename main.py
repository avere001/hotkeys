import pyautogui

from pynput import keyboard


def on_press(key):
    try:
        k = key.char  # single-char keys
    except AttributeError:
        k = key.name  # other keys

    if k == 'page_up':
        print("holding e..")
        pyautogui.keyUp("e")
        pyautogui.keyDown("e")
    elif k == 'pause':
        print("holding right click..")
        pyautogui.mouseUp(button='right')
        pyautogui.mouseDown(button='right')


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
