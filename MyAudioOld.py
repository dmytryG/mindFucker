# ЕДИНСТВЕННО РАБОЧИЙ КЛАСС
import numpy
import pyaudio


class MyAudio:
    BITRATE = 44100
    frequency = 440.0
    delta = 10
    pa = None
    stream = None
    stereo_signal = None
    isStarted: bool = False
    isBreaked: bool = False

    def init(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(format=pyaudio.paFloat32,
                                   channels=2,
                                   rate=self.BITRATE,
                                   output=True)
        self.isBreaked = False

    def __init__(self):
        self.init()

    def sinOsc(self, frequency, duration, amplitude=1.0):
        nframes = duration * self.BITRATE
        frames = numpy.arange(nframes)
        frame_frequency = frequency / self.BITRATE
        val = amplitude * numpy.sin(frames * frame_frequency * 2.0 * numpy.pi)
        return val.astype(dtype=numpy.float32)

    def setFrequence(self, freq):
        self.frequency = freq
        signal = self.sinOsc(frequency=self.frequency, duration=2.0)
        signal2 = self.sinOsc(frequency=self.frequency+self.delta, duration=2.0)
        self.stereo_signal = numpy.ravel(numpy.column_stack((signal,signal2)))
        self.isStarted = True

    def setDelta(self, delta):
        self.delta=delta
        signal = self.sinOsc(frequency=self.frequency, duration=2.0)
        signal2 = self.sinOsc(frequency=self.frequency + self.delta, duration=2.0)
        self.stereo_signal = numpy.ravel(numpy.column_stack((signal, signal2)))
        self.isStarted = True

    def playLoop(self):
        while not self.isBreaked:
            if self.isStarted:
                self.stream.write(self.stereo_signal.tostring())

    def start(self, isStarted: bool):
        self.isStarted = isStarted

    def brakeLoop(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pa.terminate()
        self.isStarted = False
        self.isBreaked = True
