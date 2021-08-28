import Blink
import MyAudioOld
import ConsoleErrors

#Class that stores current data
class MyConfig:
    frequncy: int = 1
    delta: int = 1 #ACTUALLY BEAT FREQUENCY!!!!!!!!
    run: bool = False

    def saveConfigToFile(self, filename: str):
        try:
            f = open(filename+".mf", 'w')
            f.write(str(self.frequncy) + '\n' + str(self.delta) + '\n' + str(self.run))
            f.close()
        except:
            ConsoleErrors.error("Error during writing file. Config wasn't written")

    def loadConfigToFile(self, filename: str):
        oldConfig = MyConfig()
        oldConfig.delta=self.delta
        oldConfig.run=self.run
        oldConfig.frequncy=self.frequncy
        try:
            f = open(filename+".mf", 'r')
            l = f.readline()
            if(int(l)<1):
                raise ("Parameter can't be less 0")
            else:
                self.frequncy=int(l)
            l = f.readline()
            if (int(l) < 1):
                raise ("Parameter can't be less 0")
            else:
                self.delta = int(l)
            l = f.readline()
            if(l.startswith("False")):
                self.run=False
            elif(l.startswith("True")):
                self.run=True
            else:
                f.close()
                raise (f"Parameter can't be {l}")
            f.close()
        except:
            #If there are some errors with file loading, config doesn't change
            self.frequncy=oldConfig.frequncy
            self.delta = oldConfig.delta
            self.run = oldConfig.run
            ConsoleErrors.error("Error during reading file. Config wasn't loaded")



class MyConsole:
    audio: MyAudioOld.MyAudio = None
    displayControlled: Blink.displayController = None
    display: Blink.Blink = None
    config: MyConfig = None
    help: str = "set_freq <Frequence> for set frequence\n" \
                "set_delta <Delta> for set phase delta (beat hz)\n" \
                "save_config <filename(without .mf)> for save current config to file\n" \
                "load_config <filename(without .mf)> for load config from file\n" \
                "pause for temporally stop generation\n" \
                "play for resume or start generation\n"


    def __init__(self, audio, displayController, display, cnf):
        self.audio = audio
        self.display = display
        self.displayControlled = displayController
        self.config = cnf

        self.audio.isStarted = False
        self.display.isPaused = True

    #Should be callsed after updating config (sets parameters of modules to config parameters)
    def applyConfig(self):
        self.audio.setFrequence(self.config.frequncy)
        self.audio.setDelta(self.config.delta)
        self.audio.isStarted = self.config.run
        self.display.delta = self.config.delta
        self.display.isPaused = not self.config.run

    def setFrequncy(self, freq: int):
        self.config.frequncy = freq
        self.applyConfig()

    def setDelta(self, delta: int):
        self.config.delta = delta
        self.applyConfig()

    def setIsPlay(self, isPlay: bool):
        self.config.run=isPlay
        self.applyConfig()

    #Check obtained string, sets parameters to config, applying config
    def consoleCommand(self, string: str):
        try:
            args: list = string.split(" ")
            if args[0] == "set_freq":
                if(int(args[1]) < 1):
                    ConsoleErrors.Warning("Frequence must be not less than 1")
                else:
                    self.setFrequncy(int(args[1]))
            elif (args[0] == "set_delta"):
                if (int(args[1]) < 1):
                    ConsoleErrors.Warning("Delta must be not less than 1")
                else:
                    self.setDelta(int(args[1]))

            elif (args[0] == "save_config"):
                if (args[1] == ""):
                    ConsoleErrors.Warning("Input filename, please")
                else:
                    self.config.saveConfigToFile(args[1])

            elif (args[0] == "load_config"):
                if (args[1] == ""):
                    ConsoleErrors.Warning("Input filename, please")
                else:
                    self.config.loadConfigToFile(args[1])
                    self.applyConfig()

            elif (args[0] == "pause"):
                self.setIsPlay(False)
            elif (args[0] == "run"):
                self.setIsPlay(True)
            elif (args[0] == "exit"):
                self.audio.brakeLoop()
                self.audio.isBreaked=True
                self.display.isBraked=True

            elif (args[0] == "help"):
                ConsoleErrors.info(self.help)
            else:
                ConsoleErrors.info("There aren't such command ＞﹏＜\n"+self.help)
        except:
            ConsoleErrors.error("Unexpected console args")

    # Console loop (gets cl user input and calls method for analyse and act due to command
    def consoleThreadLoop(self):
        while (True):
            data = input("# ")
            self.consoleCommand(data)
