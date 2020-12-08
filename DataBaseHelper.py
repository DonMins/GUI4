import sqlite3


class DataBase:
    def __init__(self):
        super().__init__()

    def getConnectionDB(self):
        conn = sqlite3.connect('example.db')
        return conn

    def closeConnection(self):
        self.getConnectionDB().close()

    def fillBase(self):
        self.getConnectionDB().cursor().execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                     ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                     ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                     ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)]

        self.getConnectionDB().cursor().executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
        self.getConnectionDB().commit()

