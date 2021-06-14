import pyaudio
import threading
import wave
class Recorder():
    def __init__(self, chunk=1024, channels=1, rate=16000):
        self.CHUNK = chunk #chunck数
        self.FORMAT = pyaudio.paInt16 #格式
        self.CHANNELS = channels #声道数
        self.RATE = rate #采样率
        self._running = False  #录音状态
        self._frames = []

    def start(self):
        threading._start_new_thread(self.recording, ()) #开始录音

    def recording(self): #录音
        self._running = True
        self._frames = []
        p = pyaudio.PyAudio()
        #实例化pyaudio，使用数据流
        stream = p.open(format=self.FORMAT,  #样本大小和格式
                        channels=self.CHANNELS,
                        rate=self.RATE,
                        input=True,
                        frames_per_buffer=self.CHUNK)
        while(self._running): #数据流读入到frames
            data = stream.read(self.CHUNK)
            self._frames.append(data)
        stream.stop_stream() #停止数据流，关闭pyaudio
        stream.close()
        p.terminate()

    def stop(self):
        self._running = False

    def save(self, filename): #存储录音文件
        p = pyaudio.PyAudio()
        if not filename.endswith(".wav"):
            filename = filename + ".wav"
        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.CHANNELS) #设置
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.RATE)
        wf.writeframes(b''.join(self._frames)) #写入数据
        wf.close()

