import os

from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import *


class BtnLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, parent):
        super(QLabel, self).__init__(parent = parent)
        self.sound = QtMultimedia.QSoundEffect()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()
            self.play_sound(self.text())

    def play_sound(self, text):
        address = os.getcwd() + '\\元音舌位图\\'
        sound_file = address + text + '.wav'
        self.sound.setSource(QtCore.QUrl.fromLocalFile(sound_file))
        self.sound.play()


