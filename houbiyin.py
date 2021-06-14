from PyQt5.QtWidgets import QFrame, QTableWidget, QAbstractItemView, QTableWidgetItem, QHBoxLayout
from PyQt5 import QtCore, QtMultimedia
import os


class houbiyinyunwei(QFrame):
    def __init__(self, parent=None):
        super(QFrame, self).__init__(parent = parent)
        self.resize(845, 465)
        self.move(0, 20)
        self.MyTable = QTableWidget(4, 4)
        self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置不能更改表格文字
        list1 = ['四呼', 'a韵腹', 'e韵腹', 'o韵腹']
        self.MyTable.setHorizontalHeaderLabels(list1)
        self.MyTable.verticalHeader().setVisible(False)

        list2 = (' 开口呼 ', ' 齐齿呼 ', ' 合口呼 ', ' 撮口呼 ')
        for i in range(4):
            four_hu = QTableWidgetItem(list2[i])
            self.MyTable.setItem(i , 0, four_hu)

        list3 = [((' ang [ɑŋ] ', 0, 1), (' iang [iɑŋ] ', 1, 1), ('uang [uɑŋ]', 2, 1)),   #开尾韵音标
                 ((' eng [əŋ]/[ʌŋ] ', 0, 1), (' ing [iŋ]/[iᵊŋ]/[iᶺŋ] ', 1, 1), (' ueng [uəŋ]/[uʌŋ] ', 2, 1)),
                 ((' ong [uŋ]/[ʊŋ] ', 2, 1), (' iong [yŋ]/[yuŋ]/[yʊŋ] ', 3, 1))]
        for i in range(3):
            for consonant in list3[i]:
                consonant_item = QTableWidgetItem(consonant[0])
                consonant_item.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                self.MyTable.setSpan(consonant[1], i+1, consonant[2], 1)
                self.MyTable.setItem(consonant[1], i+1, consonant_item)

        self.sound = QtMultimedia.QSoundEffect(self)

        self.MyTable.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        self.MyTable.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        self.MyTable.itemClicked.connect(lambda: self.play_sound())
        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

    def play_sound(self):
        row = self.MyTable.currentItem().row()
        column = self.MyTable.currentItem().column()

        address = os.getcwd() + '\\后鼻音韵尾\\'
        sound_file = address + str(row) + str(column) + '.wav'

        self.sound.setSource(QtCore.QUrl.fromLocalFile(sound_file))
        self.sound.play()
