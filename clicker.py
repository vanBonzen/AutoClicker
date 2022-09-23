# imports
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# delay of clicks
delay = 0.045  # 0.055 = 18.18 cps | 0.05 = 20 cps  | 0.045 = 22.22 cps | 0.04 = 25 cps
# mouse button to be clicked
button = Button.left
# key to start / pause clicking
start_stop_key = KeyCode(char='a')
# key to end autoclicking
stop_key = KeyCode(char='b')


class ClickMouse(threading.Thread):
    '''ClickMouse class'''

    def __init__(self, delay, button):
        '''constructor'''
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        '''start clicking'''
        self.running = True

    def stop_clicking(self):
        '''stop clicking'''
        self.running = False

    def exit(self):
        '''exit programm'''
        self.stop_clicking()
        self.program_running = False

    def run(self):
        '''run programm'''
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
    if key == start_stop_key:
        # start / stop clicking
        if click_thread.running:
            # stop clicking
            click_thread.stop_clicking()
        else:
            # start clicking
            click_thread.start_clicking()
    elif key == stop_key:
        # end programm
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    '''key listener'''
    listener.join()
