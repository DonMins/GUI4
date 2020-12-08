from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import sqlite3
import DataBaseHelper as db

top = 400
left = 400
width = 1000
height = 600


class MyTableWidget(QMainWindow):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.setFixedSize(970, 350)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.addTab(self.tab4, "Tab 4")
        self.tabs.addTab(self.tab5, "Tab 5")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton("PyQt5 button")
        # self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.layout = QFormLayout(self)
        self.db = 0

        title = "Генератор курса валют на торговом рынке"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setFixedSize(width, height)

        mainMenu = self.menuBar()
        menu = mainMenu.addMenu("Меню")

        setConnection = QAction("Set connection", self)
        setConnection.triggered.connect(self.getConnectionDB)

        menu.addAction(setConnection)

        close = QAction("Close", self)
        close.triggered.connect(self.closeConnection)
        menu.addAction(close)

        self.btn1 = QPushButton("bt1 (select Column)", self)
        self.btn1.move(12,50)
        self.btn1.resize(150,25)
        self.btn1.setFont(QFont('Arial', 7))

        self.btn2= QPushButton("bt2 (Query2)", self)
        self.btn2.move(174, 50)
        self.btn2.resize(150, 25)
        self.btn2.setFont(QFont('Arial', 7))

        self.btn3 = QPushButton("bt3 (Query3)", self)
        self.btn3.move(174+150+12, 50)
        self.btn3.resize(150, 25)
        self.btn3.setFont(QFont('Arial', 7))

        self.combo = QComboBox(self)
        self.combo.addItems(["Ubuntu", "Mandriva",
                        "Fedora", "Arch", "Gentoo"])
        self.combo.resize(150, 25)
        # self.combo.activated[str].connect(self.onActivated)
        self.combo.move(174+150+12+200, 50)

        self.tabs = QTabWidget(self)
        self.tab1 = QTableWidget (self)
        self.tab2 = QTableWidget (self)
        self.tab3 = QTableWidget (self)
        self.tab4 = QTableWidget (self)
        self.tab5 = QTableWidget (self)
        self.tabs.setFixedSize(970, 450)

        # Add tabs
        self.tabs.addTab(self.tab1, "Tab 1")
        self.tabs.addTab(self.tab2, "Tab 2")
        self.tabs.addTab(self.tab3, "Tab 3")
        self.tabs.addTab(self.tab4, "Tab 4")
        self.tabs.addTab(self.tab5, "Tab 5")
        self.tabs.move(10,100)

    def addTableRow(self, table, row_data):
        row = table.rowCount()
        table.setRowCount(row + 1)
        col = 0
        for item in row_data:
            cell = QTableWidgetItem(str(item))
            table.setItem(row, col, cell)
            col += 1

    def getConnectionDB(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE if not exists stocks
                     (date text, trans text, symbol text, qty real, price real)''')
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                     ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                     ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                     ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)]

        c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
        conn.commit()
        data = c.execute('SELECT * FROM stocks').fetchall()

        info_table = c.execute('PRAGMA table_info(stocks)').fetchall()
        self.tab1.setColumnCount(len(info_table))
        columnsName = []
        for row in info_table:
            columnsName.append(row[1])
        self.tab1.rowCount()
        self.tab1.setHorizontalHeaderLabels(columnsName)

        for row in data:
            self.addTableRow(self.tab1, row)

        # cur = g.fetchall()
        # for i, row in enumerate(cur):
        #     for j, val in enumerate(row):
        #         self.tabs.setItem(i, j, QTableWidgetItem(str(val)))
        #
        # for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        #     print(row)
        self.db = conn

    def closeConnection(self):
        if self.db != 0:
            self.db.cursor().execute('delete from stocks')
            self.db.commit()

            self.db.close()

    def onActivated(self, text):
        self.combo.setText(text)
        self.combo.adjustSize()


    def buttonClicked(self):
        newOil = float(self.oilEdit.text())
        oldOil = float(self.oil.getOil())
        self.oil.setOil(self.oilEdit.text())
        if newOil > oldOil:
            self.ruble.setRuble.emit(1)
            self.rubleEdit.setText(self.ruble.getRuble())

            self.dollar.setDollar.emit(-1)
            self.dollarEdit.setText(self.dollar.getDollar())

        if newOil < oldOil:
            self.dollar.setDollar.emit(1)
            self.dollarEdit.setText(self.dollar.getDollar())

            self.ruble.setRuble.emit(-1)
            self.rubleEdit.setText(self.ruble.getRuble())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()