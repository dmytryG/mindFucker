import graphics
import AccelBrainBeat
import threading

import Blink
import MyAudioOld
import MyConsole

config = MyConsole.MyConfig()
bb = MyAudioOld.MyAudio()
dc = Blink.displayController()
bw = Blink.Blink(dc)
console = MyConsole.MyConsole(bb, dc, bw, config)


def main():
    bt = threading.Thread(target=bw.blinkLoop)
    bb.setFrequence(220)
    bbt = threading.Thread(target=bb.playLoop)
    bbt.start()
    bt.start()
    console.setIsPlay(True)

    threading.Thread(target=console.consoleThreadLoop).start()


    while True:
        dc.loop()



if __name__ == '__main__':
    main()
