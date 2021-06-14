from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtWidgets import QFrame, QLabel

from btnLabel import BtnLabel

class VowelsWidget(QFrame):
    global column, points, IPA, list1
    column = [100, 190, 280, 370]  # IPA放置位置
    points = {column[0]: (180, 227, 406, 453, 500, 686, 734),  # 点阵
              column[1]: (234, 281, 433, 480, 527, 686, 734),
              column[2]: (288, 335, 460, 507, 554, 686, 734),
              column[3]: (342, 389, 487, 534, 581, 686, 734)}
    IPA = [(('i', 'y'), ('ɨ', 'ʉ'), ('ɯ', 'u')),
           (('e', 'ø'), ('ɘ', 'ɵ'), ('ɤ', 'o')),
           (('ɛ', 'œ'), ('ɜ', 'ɞ'), ('ʌ', 'ɔ')),
           (('a', 'ɶ'), ('ä', 'ɒ̈'), ('ɑ', 'ɒ'))]
    list1 = [0, 3, 6]
    clicked = pyqtSignal()

    def __init__(self, parent = None):
        super(QFrame, self).__init__(parent = parent)
        self.setStyleSheet('background : white')
        self.resize(850, 450)
        self.move(0, 26)

        self.buttons = []
        Font = QFont('Arial', 15)
        for i in range(4): #国际音标
            for j in range(3):
                b1 = BtnLabel(self)
                b1.setText(IPA[i][j][0])
                b1.setFont(Font)
                b1.setFixedSize(30, 30)
                b1.setAlignment(Qt.AlignCenter)
                b1.move(points[column[i]][list1[j]] - 41, column[i] - 17)
                b1.clicked.connect(lambda :self.play_sound())
                self.buttons.append(b1)


                b2 = BtnLabel(self)
                b2.setText(IPA[i][j][1])
                b2.setFont(Font)
                b2.setFixedSize(30, 30)
                b1.setAlignment(Qt.AlignCenter)
                b2.move(points[column[i]][list1[j]] + 9, column[i] - 17)
                b2.clicked.connect(lambda :self.play_sound())
                self.buttons.append(b2)
        #一些其他的元音
        pos_and_vowels = {'ɪ':(320, 130), 'ʊ':(590, 130),
                          'ə':(480, 220),
                          'æ':(303, 310), 'ɐ':(510, 310)}
        for vowel, pos in pos_and_vowels.items():
            b = BtnLabel(self)
            b.setText(vowel)
            b.setFont(Font)
            b.setFixedSize(30, 30)
            b.setAlignment(Qt.AlignCenter)
            b.move(pos[0], pos[1])
            b.clicked.connect(lambda: self.play_sound())
            self.buttons.append(b)
        #中文
        chinese1 = ('闭', '半闭', '半开', '开')
        chinese2 = ('前', '中', '后')
        Font2 = QFont('微软雅黑', 12)
        for i in range(4):
            the_label = QLabel(chinese1[i], self)
            the_label.setFont(Font2)
            the_label.move(55, column[i] - 15)
        for i in range(3):
            the_label = QLabel(chinese2[i], self)
            the_label.setFont(Font2)
            the_label.move(points[column[0]][3 * i] - 15, 30)

        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLinesPoints(qp)
        qp.end()

    def drawLinesPoints(self, qp):
        from PyQt5.QtCore import Qt
        pen = QPen(Qt.black, 3, Qt.SolidLine)

        qp.setPen(pen) #竖线
        qp.drawLine(points[column[0]][0], column[0], points[column[3]][0], column[3])
        qp.drawLine(points[column[0]][6], column[0], points[column[3]][6], column[3])
        qp.drawLine(points[column[0]][3], column[0], points[column[3]][3], column[3])
        for i in column: #横线
            qp.drawLine(points[i][1], i, points[i][2], i)
            qp.drawLine(points[i][4], i, points[i][5], i)

        qp.setPen(QPen(Qt.black, 8))
        for i in column: #点
            for j in range(7):
                qp.drawPoint(points[i][j], i)

    def play_sound(self):
        pass

