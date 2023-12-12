import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


class Window(QMainWindow):
    '''Класс окна программы'''

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.pushButton.clicked.connect(self.showInfo)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()

    def showInfo(self):
        '''Слот реализует работу кнопки self.pushButton и
        выводит данные на self.tableWidget'''

        coffee = self.cur.execute('''SELECT * FROM coffee_info''').fetchall()
        if coffee:
            self.tableWidget.setRowCount(len(coffee))
            self.tableWidget.setColumnCount(7)
            for i in range(len(coffee)):
                for j in range(len(coffee[0])):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(coffee[i][j])))
                    print(coffee[i][j])


app = QApplication(sys.argv)
if __name__ == '__main__':
    ex = Window()
    ex.show()
    sys.exit(app.exec())
