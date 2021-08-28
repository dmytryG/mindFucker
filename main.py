#Sorry for bad english in comments((((
#It actully not my primary language


import graphics
import AccelBrainBeat
import threading

import Blink
import MyAudioOld
import MyConsole

config = MyConsole.MyConfig() #Initialize config
bb = MyAudioOld.MyAudio()   #initialize binaular beat generator
dc = Blink.displayController()  #Initialize display queue
bw = Blink.Blink(dc)    #Initialize blinking window
console = MyConsole.MyConsole(bb, dc, bw, config)   #Initialize confole control


def main():
    bt = threading.Thread(target=bw.blinkLoop)  #Initialize blinking window thread
    bb.setFrequence(220)    #Setting default frequncy (for audio)
    bbt = threading.Thread(target=bb.playLoop)  #Initialize audio thread
    bbt.start() #Starting threads
    bt.start()
    console.setIsPlay(True)

    threading.Thread(target=console.consoleThreadLoop).start()


    while True:     #Main thread (loop) for working with window
        dc.loop()



if __name__ == '__main__':
    main()
