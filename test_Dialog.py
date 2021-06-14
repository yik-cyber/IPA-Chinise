# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'study.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtMultimedia, QtCore
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, QUrl
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QLabel, QFrame, QWidget, QTextBrowser, QHBoxLayout, QToolButton
from Draw import Draw_Frame
from Recorder import Recorder
from ise import get_chapter, test_audio, test_data


class test_Dialog(QDialog):
    def __init__(self, parent = None):
        super(QDialog, self).__init__(parent = parent)
        self.setFixedSize(651, 500)
        self.setObjectName("MainWindow")
        self.setWindowTitle('语音评测')
        name = os.getcwd() + '\\主界面\\interface.jpg'
        name = name.replace('\\', '/')
        name = '#centralwidget_bk{border-image:url(' + name +');}'
        self.setStyleSheet(name)
        self.centralwidget_bk = QWidget(self)
        self.centralwidget_bk.setStyleSheet("#centralwidget")
        self.centralwidget_bk.setObjectName("centralwidget_bk")
        self.textBrowser_score = QTextBrowser(self.centralwidget_bk)
        self.textBrowser_score.setGeometry(QRect(19, 40, 300, 190))
        self.textBrowser_score.setObjectName("textBrowser_score")
        self.frame_operate = QFrame(self.centralwidget_bk)
        self.frame_operate.setGeometry(QRect(19, 30, 300, 45))
        self.frame_operate.setStyleSheet("background-color: rgb(226, 225, 228);")
        self.frame_operate.setFrameShape(QFrame.StyledPanel)
        self.frame_operate.setFrameShadow(QFrame.Raised)
        self.frame_operate.setObjectName("frame_operate")
        self.horizontalLayout = QHBoxLayout(self.frame_operate)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_4 = QFrame(self.frame_operate)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout.addWidget(self.line_4)
        self.toolButton = QToolButton(self.frame_operate)
        self.toolButton.setStyleSheet("")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.test_data_get)
        self.horizontalLayout.addWidget(self.toolButton)
        self.line = QFrame(self.frame_operate)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.line_2 = QFrame(self.frame_operate)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.toolButton_3 = QToolButton(self.frame_operate)
        self.toolButton_3.setStyleSheet("")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_3.clicked.connect(self.start_record)
        self.horizontalLayout.addWidget(self.toolButton_3)
        self.line_3 = QFrame(self.frame_operate)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.line_6 = QFrame(self.frame_operate)
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.toolButton_4 = QToolButton(self.frame_operate)
        self.toolButton_4.setStyleSheet("")
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_4.clicked.connect(self.end_record)
        self.horizontalLayout.addWidget(self.toolButton_4)
        self.line_5 = QFrame(self.frame_operate)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout.addWidget(self.line_5)
        self.toolButton.raise_()
        self.toolButton_3.raise_()
        self.toolButton_4.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.textBrowser_graph = QTextBrowser(self.centralwidget_bk)
        self.textBrowser_graph.setGeometry(QRect(19, 245, 613, 230))
        self.textBrowser_graph.setObjectName("textBrowser_graph")
        self.textBrowser_score_2 = QTextBrowser(self.centralwidget_bk)
        self.textBrowser_score_2.setGeometry(QRect(330, 40, 300, 190))
        self.textBrowser_score_2.setObjectName("textBrowser_score_2")
        self.frame_operate_2 = QFrame(self.centralwidget_bk)
        self.frame_operate_2.setGeometry(QRect(330, 30, 300, 45))
        self.frame_operate_2.setStyleSheet("background-color: rgb(226, 225, 228);")
        self.frame_operate_2.setFrameShape(QFrame.StyledPanel)
        self.frame_operate_2.setFrameShadow(QFrame.Raised)
        self.frame_operate_2.setObjectName("frame_operate_2")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_operate_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.line_7 = QFrame(self.frame_operate_2)
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.line_8 = QFrame(self.frame_operate_2)
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.horizontalLayout_2.addWidget(self.line_8)
        self.line_9 = QFrame(self.frame_operate_2)
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_2.addWidget(self.line_9)
        self.toolButton_5 = QToolButton(self.frame_operate_2)
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.test_match)
        self.horizontalLayout_2.addWidget(self.toolButton_5)
        self.toolButton_6 = QToolButton(self.frame_operate_2)
        self.toolButton_6.setText('语音')
        self.toolButton_6.clicked.connect(self.play_sound)
        self.horizontalLayout_2.addWidget(self.toolButton_6)
        self.line_10 = QFrame(self.frame_operate_2)
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.horizontalLayout_2.addWidget(self.line_10)
        self.line_11 = QFrame(self.frame_operate_2)
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.horizontalLayout_2.addWidget(self.line_11)
        self.line_12 = QFrame(self.frame_operate_2)
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.horizontalLayout_2.addWidget(self.line_12)


        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

        self.graph = QFrame(self.textBrowser_graph)
        self.graph.setGeometry(QRect(-12, -12, 600, 237.5))
        self.graph.setFrameShape(QFrame.StyledPanel)
        self.graph.setFrameShadow(QFrame.Raised)

        self.rec = Recorder()

        self.draw = Draw_Frame(self.graph)

        font = QFont('IPAPANNEW', 22)
        self.label1 = QLabel(self.textBrowser_score)
        self.label1.setFont(font)
        self.label1.setText('')
        self.label1.setGeometry(QRect(25, 25, 200, 170))

        font = QFont('Yu Gothic', 10)
        self.label3 = QLabel(self.textBrowser_score)
        self.label3.setFont(font)
        self.label3.setText('语音评测\n点击 △ 获取试题\n点击 ▶ 开始录音\n点击 ■ 停止录音\n点击评测提交')
        self.label3.setGeometry(QRect(25, 25, 200, 170))

        font = QFont('微软雅黑', 15)
        self.label2 = QLabel(self.textBrowser_score_2)
        self.label2.setFont(font)
        self.label2.setText('讯飞评测分数：\n')
        self.label2.setGeometry(QRect(20, 0, 200, 170))

        self.chapter, self.IPA, self.pinyin = get_chapter()


    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser_score.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        button_font = QFont('Yu Gothic')
        self.toolButton.setFont(button_font)
        self.toolButton_3.setFont(button_font)
        self.toolButton_4.setFont(button_font)
        self.toolButton.setText(_translate("MainWindow", "△"))
        self.toolButton_3.setText(_translate("MainWindow", "▶"))
        self.toolButton_4.setText(_translate("MainWindow", "■"))
        self.textBrowser_graph.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_score_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.toolButton_5.setText(_translate("MainWindow", "测评"))



    def start_record(self):
        self.rec.start()

    def end_record(self):
        self.rec.stop()
        self.rec.save(r'test_audio.wav')
        self.draw_graph()

    def draw_graph(self):
        self.draw = Draw_Frame(self.graph)
        self.draw.draw(r'test_audio.wav')
        self.draw.show()

    def test_data_get(self):
        self.test_lst = test_data(self.chapter, self.IPA, self.pinyin)
        self.label3.hide()
        self.label1.setText(self.test_lst[1])
        self.label2.setText('讯飞评测分数：\n')

    def test_match(self):
        self.score = float(test_audio())
        if self.score >= 0:
            score_str = '讯飞评测分数：\n' + str(self.score)
            self.label2.setText(score_str)
        else:
            self.dialog = QDialog()
            self.dialog.setFixedSize(450,200)
            self.dialog.layout = QHBoxLayout(self.dialog)
            self.dialog.font = QFont('微软雅黑', 12)
            self.dialog.setWindowTitle('运行错误提示')
            self.dialog.text = QTextBrowser(self.dialog)
            self.dialog.text.setFont(self.dialog.font)
            self.dialog.text.setText('由于您的ip未在白名单内，故无法提供讯飞语音评测结果。\n'+'请联系软件制作者将ip加入白名单。')
            self.dialog.layout.addWidget(self.dialog.text)
            self.dialog.show()

    def play_sound(self):
        self.sound = QtMultimedia.QSoundEffect(self)
        address = os.getcwd() + '\\样例\\'
        sound_file = address + self.test_lst[2] + '.wav'
        self.sound.setSource(QtCore.QUrl.fromLocalFile(sound_file))
        self.sound.play()
        self.draw = Draw_Frame(self.graph)
        self.draw.draw(sound_file)
        self.draw.show()


