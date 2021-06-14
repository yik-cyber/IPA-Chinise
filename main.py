import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, \
    qApp, QDialog, QSlider, QLabel, QHBoxLayout
from interface import interface
from fuyin import ConsonantWidget
from houbiyin import houbiyinyunwei
from kaiweiyun import kaiweiyun
from qianbiyin import qianbiyinyunwei
from yuanyin import yuanyinyunwei
from yuanyinshewei import VowelsWidget
from Help import Help
from other import other
from test_Dialog import test_Dialog

class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setWindowTitle('汉语国际音标学习软件')
        self.setFixedSize(850, 500)
        self.layout = QHBoxLayout(self)
        self.interface = interface(self)
        self.layout.addWidget(self.interface, 0, Qt.AlignCenter)
        self.interface.toolButton_2.clicked.connect(self.show_fuyin) #按钮信号槽连接
        self.interface .toolButton_7.clicked.connect(self.show_houbiyin)
        self.interface.toolButton_4.clicked.connect(self.show_kaiweiyun)
        self.interface.toolButton_6.clicked.connect(self.show_qianbiyin)
        self.interface.toolButton_5.clicked.connect(self.show_yuanyin)
        self.interface.toolButton.clicked.connect(self.show_volwes)
        self.interface.toolButton_9.clicked.connect(self.help)
        self.interface.toolButton_10.clicked.connect(self.Other)
        self.interface.toolButton_8.clicked.connect(self.test_dialog)

        self.fuyinbiao = ConsonantWidget(self)#每一个具体的表
        self.layout.addWidget(self.fuyinbiao, 0, Qt.AlignCenter)
        self.houbiyin = houbiyinyunwei(self)
        self.layout.addWidget(self.houbiyin, 0, Qt.AlignCenter)
        self.kaiwei = kaiweiyun(self)
        self.layout.addWidget(self.kaiwei, 0, Qt.AlignCenter)
        self.qianbiyin = qianbiyinyunwei(self)
        self.layout.addWidget(self.qianbiyin, 0, Qt.AlignCenter)
        self.yuanyin = yuanyinyunwei(self)
        self.layout.addWidget(self.yuanyin, 0, Qt.AlignCenter)
        self.volwes = VowelsWidget(self)
        self.layout.addWidget(self.volwes, 0, Qt.AlignCenter)
        self.fuyinbiao.hide()
        self.volwes.hide()
        self.yuanyin.hide()
        self.qianbiyin.hide()
        self.houbiyin.hide()
        self.kaiwei.hide()

        exitAct = QAction('&退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('关闭窗口')
        exitAct.triggered.connect(qApp.quit)

        returnAct = QAction('&返回', self)
        returnAct.setShortcut('Backspace')
        returnAct.setStatusTip('返回到主界面 : 快捷键 Backspace')
        returnAct.triggered.connect(self.show_interface)

        settingAct = QAction('&设置', self)
        settingAct.setStatusTip('音量调节')
        settingAct.triggered.connect(self.settings)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAct)
        menubar.addAction(returnAct)
        menubar.addAction(settingAct)

        statusbar = self.statusBar()
        self.show()

        with open('volumn.txt') as f:
            self.volumn = float(f.read())
        self.volumn_change(False)

    def show_fuyin(self):
        self.interface.hide()
        self.fuyinbiao.show()

    def show_houbiyin(self):
        self.interface.hide()
        self.houbiyin.show()

    def show_kaiweiyun(self):
        self.interface.hide()
        self.kaiwei.show()

    def show_qianbiyin(self):
        self.interface.hide()
        self.qianbiyin.show()

    def show_yuanyin(self):
        self.interface.hide()
        self.yuanyin.show()

    def show_volwes(self):
        self.interface.hide()
        self.volwes.show()

    def show_interface(self):
        self.fuyinbiao.hide()
        self.volwes.hide()
        self.yuanyin.hide()
        self.qianbiyin.hide()
        self.houbiyin.hide()
        self.kaiwei.hide()
        self.interface.show()

    def settings(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle('设置')
        self.dialog.setStyleSheet('background : white')
        self.dialog.setMaximumSize(300, 50)
        self.dialog.setMinimumSize(300, 50)

        self.label = QLabel(self.dialog)
        self.label.setText('音量调节')
        self.label.move(10, 15)

        self.slider = QSlider(Qt.Horizontal, self.dialog)
        self.slider.setRange(0, 100)
        self.slider.setValue(int(self.volumn))
        self.slider.move(150, 15)
        self.slider.valueChanged.connect(self.volumn_change)
        self.dialog.show()

    def help(self):
        self.help = Help(self)
        self.help.show()

    def Other(self):
        self.other = other(self)
        self.other.show()

    def volumn_change(self, sett = True):
        if sett:
            self.volumn = self.slider.value() * 1.0
        with open('volumn.txt', 'w') as f:
            f.write(str(self.volumn))
        self.fuyinbiao.sound.setVolume(self.volumn / 100)
        self.houbiyin.sound.setVolume(self.volumn / 100)
        self.kaiwei.sound.setVolume(self.volumn / 100)
        self.qianbiyin.sound.setVolume(self.volumn / 100)
        self.yuanyin.sound.setVolume(self.volumn / 100)
        for each in self.volwes.buttons:
            each.sound.setVolume(self.volumn / 100)

    def test_dialog(self):
        self.dialog = test_Dialog()
        self.dialog.show()


if __name__=='__main__':
    app1 = QApplication(sys.argv)
    myWindow = Main_Window()
    sys.exit(app1.exec_())
