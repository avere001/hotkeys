import pyautogui

from pynput import keyboard


def on_press(key):
    try:
        k = key.char  # single-char keys
    except AttributeError:
        k = key.name  # other keys

    print(f"pressed {k=}")
    if k == 'page_up':
        pyautogui.keyDown("e")
    elif k == 'pause':
        pyautogui.mouseDown(button='right')


if __name__ == '__main__':
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
