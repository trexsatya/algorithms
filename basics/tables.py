import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
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


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, matrix, rows, columns):
        super().__init__()

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                matrix[i][j] = str(matrix[i][j]) if matrix[i][j] else ""

        self.table = QtWidgets.QTableView()

        data = pd.DataFrame(matrix,
                            columns=(columns if columns else range(len(matrix[0]))),
                            index=(rows if rows else range(len(matrix))))

        self.model = TableModel(data)
        self.table.setModel(self.model)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table.resizeColumnsToContents()
        self.setCentralWidget(self.table)


def show_table(matrix, rows=None, cols=None):
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(matrix, rows, cols)
    window.setFixedWidth(1600)
    window.setFixedHeight(900)
    window.show()
    app.exec_()


# show_table([[1,2]])