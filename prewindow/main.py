# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import Qt
import sys
from dia import Dia

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = QMainWindow()
    d = Dia(None)
    r = d.exec()
    if r == QDialog.Accepted :
        print('ok')
        mw.show()
        sys.exit(app.exec())
    else:
        print('close')
        sys.exit(1)