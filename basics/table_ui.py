from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QApplication, QWidget, QVBoxLayout
import sys
import pandas as pd


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


class TableApp(QWidget):
    matrix = [[]]
    max_width = 1900
    max_height = 900

    def __init__(self, matrix, rows, columns):
        self.columns = columns
        self.rows = rows
        self.matrix = matrix
        super().__init__()
        self.title = 'Table'
        self.left = 0
        self.top = 0
        self.width = self.max_width
        self.height = self.max_height
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable(self.matrix, self.rows, self.columns)

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Show widget
        self.show()

    def createTable(self, matrix, rows, columns):
        data = pd.DataFrame(matrix,
                            columns=(columns if columns else range(len(matrix[0]))),
                            index=(rows if rows else range(len(matrix))))

        # Create table

        self.tableWidget = QTableWidget()
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(len(matrix))
        self.tableWidget.setColumnCount(len(matrix[0]))
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(matrix[i][j]) if matrix[i][j] else ""))

        self.tableWidget.move(0, 0)
        self.tableWidget.resizeColumnsToContents()
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)


    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


def show_table(matrix, rows=None, columns=None):
    app = QApplication([])
    ex = TableApp(matrix, rows, columns)
    sys.exit(app.exec_())
