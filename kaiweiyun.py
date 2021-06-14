import  os
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtWidgets import QFrame, QTableWidget, QAbstractItemView, QTableWidgetItem, QHBoxLayout


class kaiweiyun(QFrame):
    def __init__(self, parent=None):
        super(QFrame, self).__init__(parent = parent)
        self.resize(845, 465)
        self.move(0, 20)
        self.MyTable = QTableWidget(5, 5)
        self.MyTable.setEditTriggers(QAbstractItemView.NoEditTriggers) #设置不能更改表格文字
        list1 = [' ', '开口呼', '齐齿呼', '合口呼',  '撮口呼']
        self.MyTable.setHorizontalHeaderLabels(list1)
        self.MyTable.verticalHeader().setVisible(False)

        consonant_1 = QTableWidgetItem('单韵母')#单韵母
        consonant_1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #设置表格对齐方式
        self.MyTable.setSpan(0, 0, 3, 1)
        self.MyTable.setItem(0, 0, consonant_1)

        consonant_2 = QTableWidgetItem('后响复合\n元音韵母') #后响复合元音韵母
        consonant_2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.MyTable.setSpan(3, 0, 2, 1)
        self.MyTable.setItem(3, 0, consonant_2)

        list3 = [(('a [a]', 0, 1), ('e [ɤ]', 1, 1), ('o [o]', 2, 1), ('er [ər]/[ɐr]', 3, 2)),   #辅音音标
                 (('i [i]/[ɿ]/[ʅ]', 0, 3), ('ia [ia]', 3, 1), ('ie [iɛ]', 4, 1)),
                 (('u [u]', 0, 3), ('ua [ua]', 3, 2)),
                 (('ü [y]', 0, 3), ('üe [yɛ]', 3, 2))]
        for i in range(4):
            for consonant in list3[i]:
                consonant_item = QTableWidgetItem(consonant[0])
                consonant_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.MyTable.setSpan(consonant[1], i+1, consonant[2], 1)
                self.MyTable.setItem(consonant[1], i+1, consonant_item)

        self.MyTable.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        self.MyTable.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        self.MyTable.itemClicked.connect(lambda: self.play_sound())
        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

        self.sound = QSoundEffect(self)


    def play_sound(self):
        row = self.MyTable.currentItem().row()
        column = self.MyTable.currentItem().column()

        address = os.getcwd() + '\\开尾韵\\'
        sound_file = address + str(row) + str(column) + '.wav'


        self.sound.setSource(QUrl.fromLocalFile(sound_file))
        self.sound.play()


