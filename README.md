# mindFucker
Python binaural beats generator

A simple program for generating binaural beats. In addition to generating sound, it also generates blinking with the help of the on-screen window in time with the sound, which may increase the effectiveness of the effect of binaural beats.

Command line commands:
set_freq <Frequence> for set frequence //sets the base frequence for beat
set_delta <Delta> for set phase delta (beat hz) //Actually sets the beat frequence
save_config <filename(without .mf)> for save current config to file //Save and load config from filesystem (config file must be in root folder of the program)
load_config <filename(without .mf)> for load config from file
pause for temporally stop generation
play for resume or start generation
