import queue
import random

import graphics
import threading
from time import sleep
import ctypes

# queue class for work with methods that should be called from main thread
class displayController:
    que = []
    def addToQ(self, item, args, **kwargs):
        self.que.append([item, args, kwargs])

    def loop(self):
        if (len(self.que)>0):
            item = self.que.pop()
            item[0](item[1])

# Blinking window class
class Blink:
    dc: displayController = None
    frame: graphics.GraphWin = None
    delta: int = 5
    isBraked: bool = False
    isPaused: bool = False

    def __init__(self, dc):
        screensize = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
        self.frame = graphics.GraphWin("Mind fucker", screensize[0], screensize[1], autoflush=False)
        self.frame.setBackground(graphics.color_rgb(0, 0, 0))
        self.dc = dc



    def blinkLoop(self):
        while not self.isBraked:
            if not self.isPaused:
                self.dc.addToQ(self.frame.setBackground, graphics.color_rgb(0, 0, 0))
                self.dc.addToQ(graphics.update, 30)
                sleep(1/self.delta/2)
                self.dc.addToQ(self.frame.setBackground, graphics.color_rgb(255, 255, 255))
                self.dc.addToQ(graphics.update, 30)
                sleep(1 / self.delta / 2)
                pass

        self.frame.close()

