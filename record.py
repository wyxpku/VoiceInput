# coding=UTF-8
from pyaudio import PyAudio, paInt16 
# import numpy as np 
from datetime import datetime 
import wave

class Record():
    def __init__(self):
        self.RATE = 8000
        self.CHUNK = 2000
        self.RECORD_SECONDS = 10
        self.FORMATE = paInt16
        self.pa = PyAudio()
        self.stream = self.pa.open(format=self.FORMATE, channels=1, rate=self.RATE, input=True, frames_per_buffer=self.CHUNK)

    # 将data中的数据保存到名为filename的WAV文件中
    def save_wave_file(self, filename, data):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.pa.get_sample_size(self.FORMATE))
        # wf.setsampwidth(2)
        wf.setframerate(self.RATE)
        wf.writeframes("".join(data))
        wf.close()

    def record(self):
        # save_count = 0
        save_buffer = []
        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = self.stream.read(self.CHUNK)
            save_buffer.append(data)

        filename = 'data/' + datetime.now().strftime("%Y-%m-%d_%H_%M_%S") + ".wav" 
        self.save_wave_file(filename, save_buffer) 
        # save_buffer = []
        return filename