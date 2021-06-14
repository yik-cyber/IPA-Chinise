import  os

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QFrame, QTableWidget, QAbstractItemView, QTableWidgetItem, QHBoxLayout


class yuanyinyunwei(QFrame):
    def __init__(self, parent = None):
        super(QFrame, self).__init__(parent = parent)
        self.resize(845, 465)
        self.move(0, 20)
        self.MyTable = QTableWidget(4, 4)
        self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置不能更改表格文字
        list1 = [' ', 'i韵尾', 'u韵尾', 'o韵尾']
        self.MyTable.setHorizontalHeaderLabels(list1)
        self.MyTable.verticalHeader().setVisible(False)

        consonant_1 = QTableWidgetItem('二合')#二合
        consonant_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #设置表格对齐方式
        self.MyTable.setSpan(0, 0, 2, 1)
        self.MyTable.setItem(0, 0, consonant_1)

        consonant_2 = QTableWidgetItem('三合') #三合
        consonant_2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MyTable.setSpan(2, 0, 2, 1)
        self.MyTable.setItem(2, 0, consonant_2)

        list3 = [(('ai [ai][aɪ]', 0, 1), ('ei [ei][eɪ]', 1, 1), ('uai [uai][uaɪ]', 2, 1), ('uei [uei][ueɪ]', 3, 1)),   #韵母音标
                 (('ou [ou][̜o˕ʊ]', 0, 2), ('iou [iou][i̜oʊ]', 2, 2)),
                 (('ao [ɑu][ɑʊ]', 0, 2), ('iao [iɑu][iɑʊ]', 2, 2))]
        for i in range(3):
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

        address = os.getcwd() + '\\元音韵尾\\'
        sound_file = address + str(row) + str(column) + '.wav'

        self.sound.setSource(QUrl.fromLocalFile(sound_file))
        self.sound.play()
