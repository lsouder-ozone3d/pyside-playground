from PySide2 import QtCore
from typing import Optional, List

class DoubleListModel(QtCore.QAbstractTableModel):

    def __init__(self, a: Optional[List[str]], b: Optional[List[str]]):
        super().__init__()
        row_a: List[str] = a if a else []
        row_b: List[str] = b if b else []
        self._data = [row_a, row_b]

    def rowCount(self, parent = None) -> int:
        return len(self._data)

    def columnCount(self, parent = None) -> int:
        return max((len(x) for x in self._data)) 

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.DisplayRole):
        if index.row() >= self.rowCount():
            return None 
        row = self._data[index.row()]
        if index.column() >= len(row):
            return None
        item = row[index.column()]
        if role == QtCore.Qt.DisplayRole:
            return item
        elif role == QtCore.Qt.ToolTipRole:
            return f'Tooltip: {item}'
        else:
            return None