from . import model 
from . import view
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLayout, QTableView

import sys
from pathlib import Path
from enum import IntEnum, auto


class ButtonState(IntEnum):
    GREEN = 0
    YELLOW = 1
    RED = 2
    MAX = auto()


class CustomButton(QPushButton):
    COUNTER_PROPERTY_NAME = 'counter'

    def __init__(self, label, parent):
        super().__init__(label, parent)
        self.clicked.connect(self._on_clicked)
        self._counter = int(ButtonState.GREEN)
        self._update_style()

    def _on_clicked(self):
        self._counter = (self._counter + 1) % ButtonState.MAX
        self._update_style()

    def _update_style(self) -> None:
        self.setProperty(self.COUNTER_PROPERTY_NAME, self._counter)
        self.style().unpolish(self)
        self.style().polish(self)


class TestWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        for _ in range(3):
            layout = self._add_buttton(layout)
        
        self._model = model.DoubleListModel(["This", "be", "a", "row"], ["OOF!", "more", "items", "hi"])
        self._table = QTableView()
        self._table.setModel(self._model)
        self._double_list_view = view.DoubleListView()
        self._double_list_view.setModel(self._model)
        layout.addWidget(self._table)
        layout.addWidget(self._double_list_view)
        self.setLayout(layout)

    def _add_buttton(self, layout: QLayout) -> QLayout:
        button = CustomButton("BUTTON", parent=self)
        layout.addWidget(button)
        return layout


def load_stylesheet(path: Path) -> str:
    stylesheet = ''
    with open(path) as style_file:
        stylesheet = style_file.read()
    return stylesheet


if __name__ == '__main__':
    stylesheet = load_stylesheet(Path(__file__).parent / 'style.qss')
    app = QApplication(sys.argv)
    print(stylesheet)
    app.setStyleSheet(stylesheet)
    window = TestWindow()
    window.show()
    app.exec_()
