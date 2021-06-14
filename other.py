# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'other.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel



class other(QDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent = parent)
        self.setWindowTitle('其他')
        self.setMaximumSize(240, 350)
        self.setMinimumSize(240, 350)
        name = os.getcwd() + '\\帮助文档\\backgr.jpg'
        name = name.replace('\\', '/')
        self.setStyleSheet("QDialog{border-image: url(" + name+ ")}")


        self.label = QLabel(self)
        self.label.move(40, 70)
        font = QFont()
        font.setFamily("方正大标宋_GBK")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("“汉语国际音标\n"
"学习软件”用于\n"
"学习汉语普通话\n"
"音韵，采用国际\n"
"音标，功能简洁。")


