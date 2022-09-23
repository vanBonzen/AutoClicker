# imports
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# delay of clicks
delay = 0.045  # 22.22 cps
# mouse button to be clicked
button = Button.left
# key to start / pause clicking
start_stop_key = KeyCode(char='a')
# key to end autoclicking
stop_key = KeyCode(char='b')


class ClickMouse(threading.Thread):
    '''ClickMouse class'''
    # constructor

    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # start clicking
    def start_clicking(self):
        self.running = True

    # stop clicking
    def stop_clicking(self):
        self.running = False

    # exit function
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # run function
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# initialize mouse from pynput
mouse = Controller()
# create new thread
click_thread = ClickMouse(delay, button)
# start thread
click_thread.start()


def on_press(key):
    '''key listener function'''
    # start / stop clicking
    if key == start_stop_key:
        # stop clicking
        if click_thread.running:
            click_thread.stop_clicking()
        # start clicking
        else:
            click_thread.start_clicking()
    # end clicking
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


# key listener
with Listener(on_press=on_press) as listener:
    listener.join()
