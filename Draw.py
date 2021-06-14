import wave as we
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy, QFrame
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

def wavread(filename): #返回用于绘图的 data 和 time
    wavfile = we.open(filename, "rb")
    params = wavfile.getparams() #getparams方法，获取声道数，采样精度，采样率，帧数
    channels, framesra, frameswav =params[0],params[2], params[3] #采样率 帧数
    datawav = wavfile.readframes(frameswav) #读取每一帧的声音数据
    wavfile.close()
    datause = np.fromstring(datawav, dtype=np.short) #将得到的string格式data转化为数组
    if channels == 1:
        datause.shape = -1, 1
    if channels == 2:
        datause.shape = -1, 2 #将数组分成两列（左右声道数据）
    datause = datause.T #转置数组
    time = np.arange(0, frameswav) * (1.0 / framesra) #numpy的arrange方法创建数字序列
    return datause, time

class Draw_canvas(FigureCanvas): #FigureCanvas可以嵌入到pyqt中
    def __init__(self, parent=None, width=5, height=4, dpi=100): #宽 高 分辨率
        self.fig = Figure(figsize=(width, height), dpi=dpi) #创建matplt里的绘图对象，类似于pyqt里的窗口
        self.axes = self.fig.add_subplot(1, 1, 1) #给窗口加上子图，子图是1 * 1格式
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding) #可拉伸
        FigureCanvas.updateGeometry(self)

class Draw_Frame(QFrame):
    def __init__(self, parent = None):
        super(QFrame, self).__init__(parent = parent)
        self.layout = QVBoxLayout(self)
        self.figure1 = Draw_canvas(width=12.5, height=4.5, dpi=52)
        self.layout.addWidget(self.figure1)

    def draw(self, filename): #绘制波形图
        wavedata, wavetime = wavread(filename)
        self.figure1.axes.plot(wavetime, wavedata[0])

