# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFrame, QLabel, QToolButton


class interface(QFrame):
    def __init__(self, p=None):
        super(QFrame, self).__init__(parent =p)
        self.setObjectName("widget_bk")
        self.resize(850, 500)
        name = os.getcwd() + '\\主界面\\interface.jpg'
        name = name.replace('\\', '/')
        name = '#widget_bk{border-image:url(' + name +');}'
        self.setStyleSheet(name)
        self.label = QLabel(self)
        self.label.setGeometry(QRect(320, 110, 150, 150))
        font = QFont()
        font.setFamily("华文行楷")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QRect(320, 230, 150, 150))
        font = QFont()
        font.setFamily("华文行楷")
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QRect(450, 190, 50, 200))
        font = QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QRect(490, 200, 50, 200))
        font = QFont()
        font.setFamily("华文行楷")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.toolButton_9 = QToolButton(self)
        self.toolButton_9.setGeometry(QRect(650, 410, 31, 81))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.toolButton_9.setFont(font)
        self.toolButton_9.setStyleSheet("background-color:transparent")
        self.toolButton_9.setObjectName("toolButton_9")
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(QRect(590, 410, 60, 60))
        font = QFont()
        font.setFamily("叶根友刀锋黑草")
        font.setPointSize(28)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.toolButton_4 = QToolButton(self)
        self.toolButton_4.setGeometry(QRect(80, 288, 50, 180))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setStyleSheet("background-color:transparent")
        self.toolButton_4.setObjectName("toolButton_4")
        
        font.setFamily("华文楷体")
        font.setPointSize(14)
    
        self.line_5 = QFrame(self)
        self.line_5.setGeometry(QRect(160, 300, 20, 111))
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.toolButton_5 = QToolButton(self)
        self.toolButton_5.setGeometry(QRect(120, 217, 41, 250))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet("background-color:transparent")
        self.toolButton_5.setObjectName("toolButton_5")
        self.line_4 = QFrame(self)
        self.line_4.setGeometry(QRect(130, 300, 3, 61))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_3 = QFrame(self)
        self.line_3.setGeometry(QRect(60, 300, 20, 61))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.toolButton_7 = QToolButton(self)
        self.toolButton_7.setGeometry(QRect(190, 174, 65, 300))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton_7.setFont(font)
        self.toolButton_7.setStyleSheet("background-color:transparent")
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_6 = QToolButton(self)
        self.toolButton_6.setGeometry(QRect(170, 174, 29, 300))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setStyleSheet("background-color:transparent")
        self.toolButton_6.setObjectName("toolButton_6")
        self.line_6 = QFrame(self)
        self.line_6.setGeometry(QRect(200, 300, 20, 111))
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QFrame(self)
        self.line_7.setGeometry(QRect(80, 300, 20, 61))
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.toolButton_10 = QToolButton(self)
        self.toolButton_10.setGeometry(QRect(540, 410, 31, 81))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.toolButton_10.setFont(font)
        self.toolButton_10.setStyleSheet("background-color:transparent")
        self.toolButton_10.setObjectName("toolButton_10")
        self.toolButton_8 = QToolButton(self)
        self.toolButton_8.setGeometry(QRect(30, 296, 50, 131))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton_8.setFont(font)
        self.toolButton_8.setStyleSheet("background-color:transparent")
        self.toolButton_8.setObjectName("toolButton_8")
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(QRect(520, 420, 21, 31))
        font = QFont()
        font.setFamily("叶根友刀锋黑草")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.toolButton_2 = QToolButton(self)
        self.toolButton_2.setGeometry(QRect(63, 60, 50, 100))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("background-color:transparent")
        self.toolButton_2.setObjectName("toolButton")
        self.toolButton = QToolButton(self)
        self.toolButton.setGeometry(QRect(125, 60, 50, 100))
        font = QFont()
        font.setFamily("华文楷体")
        font.setPointSize(14)
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color:transparent")
        self.toolButton.setObjectName("toolButton_2")
        self.label_7 = QLabel(self)
        self.label_7.setGeometry(QRect(50, 80, 21, 31))
        font = QFont()
        font.setFamily("Wingdings")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QLabel(self)
        self.label_8.setGeometry(QRect(110, 80, 21, 31))
        font = QFont()
        font.setFamily("Wingdings")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line_8 = QFrame(self)
        self.line_8.setGeometry(QRect(70, 300, 20, 31))
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, widget_bk):
        _translate = QCoreApplication.translate
        widget_bk.setWindowTitle(_translate("widget_bk", "Form"))
        self.label.setText(_translate("widget_bk", "汉"))
        self.label_2.setText(_translate("widget_bk", "语"))
        self.label_3.setText(_translate("widget_bk", "国\n"
"际\n"
"音\n"
"标"))
        self.label_4.setText(_translate("widget_bk", "学\n"
"习\n"
"软\n"
"件"))
        self.toolButton_9.setText(_translate("widget_bk", "帮\n"
"助"))
        self.label_5.setText(_translate("widget_bk", " ？"))
        self.toolButton_4.setText(_translate("widget_bk", "开\n"
"尾\n"
"韵\n"
"母\n"
"表"))
        
        self.toolButton_5.setText(_translate("widget_bk", "元\n"
"音\n"
"韵\n"
"尾\n"
"韵\n"
"母\n"
"表"))
        self.toolButton_7.setText(_translate("widget_bk", "后\n"
"鼻\n"
"音\n"
"韵\n"
"尾\n"
"韵\n"
"母\n"
"表"))
        self.toolButton_6.setText(_translate("widget_bk", "前\n"
"鼻\n"
"音\n"
"韵\n"
"尾\n"
"韵\n"
"母\n"
"表"))
        self.toolButton_10.setText(_translate("widget_bk", "其\n"
"它"))
        self.toolButton_8.setText(_translate("widget_bk", "语\n"
                                                          "音\n"
                                                          "评\n"
                                                          "测\n"
                                                            ))
        self.label_6.setText(_translate("widget_bk", "！"))
        self.toolButton.setText(_translate("widget_bk", "元\n"
"音\n"
"表"))
        self.toolButton_2.setText(_translate("widget_bk", "辅\n"
"音\n"
"表"))
        self.label_7.setText(_translate("widget_bk", "2"))
        self.label_8.setText(_translate("widget_bk", "2"))

