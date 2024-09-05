from PySide2 import QtCore, QtGui
from typing import Optional, List

class DoubleListModel(QtCore.QAbstractListModel):
    _WHITE = QtGui.QColor.fromRgb(255, 255, 255)
    _GREEN = QtGui.QColor.fromRgb(0, 255, 0)

    def __init__(self, a: Optional[List[str]], b: Optional[List[str]]):
        super().__init__()
        self._col_a: List[str] = a if a else []
        self._col_b: List[str] = b if b else []

    def rowCount(self, parent = None) -> int:
        return len(self._col_a) + len(self._col_b)

    def columnCount(self, parent = None) -> int:
        return 1

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.DisplayRole):
        if index.row() >= self.rowCount() or index.column() >= self.columnCount():
            return None
        is_col_a = index.row() < len(self._col_a)
        col = self._col_a if is_col_a else self._col_b
        row_index = index.row() if is_col_a else index.row() - len(self._col_a)
        item = col[row_index]
        if role == QtCore.Qt.DisplayRole:
            return item
        elif role == QtCore.Qt.ToolTipRole:
            return f'Tooltip: {item}'
        elif role == QtCore.Qt.BackgroundColorRole:
            # NOTE: Maybe this can somehow happen in the stylesheet?
            base_color = self._GREEN if is_col_a else self._WHITE 
            fade_scale = 100 if index.row() % 2 == 0 else 150
            return base_color.darker(fade_scale) 
        else:
            return None
