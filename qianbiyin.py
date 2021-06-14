import  os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QFrame, QTableWidget, QAbstractItemView, QTableWidgetItem, QHBoxLayout


class qianbiyinyunwei(QFrame):
    def __init__(self, parent=None):
        super(QFrame, self).__init__(parent = parent)
        self.resize(845, 465)
        self.move(0, 20)
        self.MyTable = QTableWidget(4, 3)
        self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置不能更改表格文字
        list1 = ['四呼', 'a韵腹', 'e韵腹']
        self.MyTable.setHorizontalHeaderLabels(list1)
        self.MyTable.verticalHeader().setVisible(False)

        list2 = (' 开口呼 ', ' 齐齿呼 ', ' 合口呼 ', ' 撮口呼 ')
        for i in range(4):
            four_hu = QTableWidgetItem(list2[i])
            self.MyTable.setItem(i , 0, four_hu)


        list3 = [(('an [an]', 0, 1), ('ian [iɛn]', 1, 1), ('uan [uan]', 2, 1), (' üan [yæn]/[yᵘæn] ', 3, 1)),   #开尾韵音标
                 (('en [ən]', 0, 1), ('in [in]/[iᵊn]', 1, 1), ('uen [uən]', 2, 1), (' ün [yn]/[yᵊn] ', 3, 1))]
        for i in range(2):
            for consonant in list3[i]:
                consonant_item = QTableWidgetItem(consonant[0])
                consonant_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.MyTable.setSpan(consonant[1], i+1, consonant[2], 1)
                self.MyTable.setItem(consonant[1], i+1, consonant_item)

        self.sound = QSoundEffect(self)

        self.MyTable.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        self.MyTable.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        self.MyTable.itemClicked.connect(lambda: self.play_sound())
        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

    def play_sound(self):
        row = self.MyTable.currentItem().row()
        column = self.MyTable.currentItem().column()

        address = os.getcwd() + '\\前鼻音韵尾\\'
        sound_file = address + str(row) + str(column) + '.wav'

        self.sound.setSource(QUrl.fromLocalFile(sound_file))
        self.sound.play()
