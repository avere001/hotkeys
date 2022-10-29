from typing import Union

import pyautogui

from pynput import keyboard
from pynput.keyboard import KeyCode, Key


def on_press(key: Union[Key, KeyCode]):
    if key == Key.page_up:
        print("holding e..")
        pyautogui.keyUp("e")
        pyautogui.keyDown("e")
    elif key == Key.pause:
        print("holding right click..")
        pyautogui.mouseUp(button="right")
        pyautogui.mouseDown(button="right")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
