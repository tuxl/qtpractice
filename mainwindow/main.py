import sys
from PyQt5.QtWidgets import QApplication, QWidget
from MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow(app)
    w.show()

    sys.exit(app.exec_())