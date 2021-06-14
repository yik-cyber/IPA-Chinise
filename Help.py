# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5.QtCore import QMetaObject, QCoreApplication, QRect
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame,QDialog, QLabel


class Help(QDialog):
    def __init__(self, p=None):
        super(QDialog,self).__init__(parent=p)
        self.setObjectName("Form")
        self.setMaximumSize(450, 500)
        self.setMinimumSize(450, 500)
        name = os.getcwd() + '\\帮助文档\\backgr.jpg'
        name = name.replace('\\', '/')
        self.setStyleSheet("QDialog{border-image: url(" + name+ ")}")
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(20, 10, 411, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(0, 0, 100, 50))
        font = QFont()
        font.setFamily("方正兰亭细黑_GBK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.frame)
        self.label_2.move(10, 50)
        font = QFont()
        font.setFamily("方正书宋简体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.move(0, 100)
        font = QFont()
        font.setFamily("方正兰亭细黑_GBK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self.frame)
        self.label_4.move(10, 140)
        font = QFont()
        font.setFamily("方正书宋简体")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.frame)
        self.label_5.move(0, 210)
        font = QFont()
        font.setFamily("方正兰亭细黑_GBK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QLabel(self.frame)
        self.label_6.move(0, 310)
        font = QFont()
        font.setFamily("方正兰亭细黑_GBK")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QLabel(self.frame)
        self.label_7.move(10, 250)
        font = QFont()
        font.setFamily("方正书宋简体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self.frame)
        self.label_8.move(10, 350)
        font = QFont()
        font.setFamily("方正书宋简体")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "帮助"))
        self.label.setText(_translate("Form", "内容"))
        self.label_2.setText(_translate("Form", "本软件包括六张表，分别为辅音表、元音表、开尾韵韵母表、元音\n"
"韵尾韵母表、前鼻韵韵母表和后鼻韵韵母表。"))
        self.label_3.setText(_translate("Form", "使用"))
        self.label_4.setText(_translate("Form", "1.发音：点击表中具体符号；\n"
"2.调节音量：选择菜单栏中的“设置”选项-->拉动随后弹出的音量\n"
"调节滑块。"))
        self.label_5.setText(_translate("Form", "相关概念"))
        self.label_6.setText(_translate("Form", "拓展知识"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><a href=\"https://baike.so.com/doc/5566859-5781976.html\"><span style=\" text-decoration: underline; color:#0000ff;\">声母</span></a></p><p><a href=\"https://baike.so.com/doc/855164-904184.html\"><span style=\" text-decoration: underline; color:#0000ff;\">韵母</span></a></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><a href=\"http://www.zdic.net/appendix/f10.htm\"><span style=\" text-decoration: underline; color:#0000ff;\">汉语拼音与国际音标对应表</span></a></p></body></html>"))

