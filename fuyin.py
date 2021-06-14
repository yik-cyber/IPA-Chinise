from PyQt5 import QtCore, QtMultimedia
import os
from PyQt5.QtWidgets import QFrame, QTableWidget, QAbstractItemView, QTableWidgetItem, QHBoxLayout


class ConsonantWidget(QFrame):
    def __init__(self, parent=None):
        super(QFrame, self).__init__(parent = parent)
        self.resize(845, 465)
        self.move(0, 20)
        self.MyTable = QTableWidget(8, 10)
        self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置不能更改表格文字
        list1 = ['清辅特征', '发音方法', '送气特征',  '双唇', '唇齿', '舌尖前齿', '舌尖中齿龈',
                 '卷舌', '舌面前硬腭', '舌面后软腭']
        self.MyTable.setHorizontalHeaderLabels(list1)
        self.MyTable.verticalHeader().setVisible(False)

        consonant_1 = QTableWidgetItem('清音')#清音
        consonant_1.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) #设置表格对齐方式
        self.MyTable.setSpan(0, 0, 5, 1)
        self.MyTable.setItem(0, 0, consonant_1)

        consonant_2 = QTableWidgetItem('浊音') #浊音
        consonant_2.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.MyTable.setSpan(5, 0, 3, 1)
        self.MyTable.setItem(5, 0, consonant_2)

        list2 = ['塞音', '塞擦音', '擦音', '鼻音', '边音', '通音'] #发音方式
        self.MyTable.setSpan(0, 1, 2, 1)
        self.MyTable.setSpan(2, 1, 2, 1)
        j = 0
        for i in [0, 2, 4, 5, 6, 7]:
            tempItem = QTableWidgetItem(list2[j])
            tempItem.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.MyTable.setItem(i, 1, tempItem)
            j += 1

        list3 = [(('不送气', 0), ('送气', 1), ('不送气', 2), ('送气', 3)),
                 (('b [p]', 0), ('p [pʰ]', 1), ('m [m]', 5)),   #辅音音标
                 (('f [f]', 4),),
                 (('z [ts]', 2), ('c [tsʰ]', 3), ('s [s]', 4)),
                 (('d [t]', 0), ('t [tʰ]', 1), ('n [n]', 5), ('l [l]', 6)),
                 (('zh [ʈʂ]', 2), ('ch [ʈʂʰ]', 3), ('sh [ʂ]', 4), ('r [ɻ]', 7)),
                 (('j [tɕ]', 2), ('q [tɕʰ]', 3), ('x [ɕ]', 4)),
                 (('g [k]', 0), ('k [kʰ]', 1), ('h [x]', 4))]
        for i in range(8):
            for consonant in list3[i]: #consonant是每一组，包括字符串和行坐标
                consonant_item = QTableWidgetItem(consonant[0])
                consonant_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.MyTable.setItem(consonant[1], i+2, consonant_item)
                                     #行坐标        列坐标

        self.MyTable.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        self.MyTable.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        self.MyTable.itemClicked.connect(lambda: self.play_sound())
        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

        self.sound = QtMultimedia.QSoundEffect(self)

    def play_sound(self):
        row = self.MyTable.currentItem().row()
        column = self.MyTable.currentItem().column()

        address = os.getcwd() + '\\辅音表\\'
        sound_file = address + str(row) + str(column) + '.wav'

        self.sound.setSource(QtCore.QUrl.fromLocalFile(sound_file))
        self.sound.play()
