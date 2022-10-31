from threading import Event, Thread
from typing import Union

import pyautogui
from pynput import keyboard
from pynput.keyboard import KeyCode, Key

spam_e_event = Event()


def spam_e_task():
    while True:
        if spam_e_event.is_set():
            pyautogui.press("e")


def on_press(key: Union[Key, KeyCode]):
    if key == Key.page_up:
        print("holding e..")
        pyautogui.keyUp("e")
        pyautogui.keyDown("e")
    elif key == Key.page_down:
        spam_e_event.clear() if spam_e_event.is_set() else spam_e_event.set()
    elif key == Key.pause:
        print("holding right click..")
        pyautogui.mouseUp(button="right")
        pyautogui.mouseDown(button="right")


if __name__ == "__main__":
    spam_e_thread = Thread(target=spam_e_task)
    listener = keyboard.Listener(on_press=on_press)

    listener.start()
    spam_e_thread.start()

    listener.join()
    spam_e_thread.join()
