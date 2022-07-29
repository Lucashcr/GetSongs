import os, sys
from PySide6.QtWidgets import QApplication

from ui.mainwindow.controller import MainWindow


if __name__ == '__main__':
    app = QApplication( sys.argv )
    win = MainWindow()
    win.show()
    sys.exit(app.exec())