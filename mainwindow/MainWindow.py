# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox
from PyQt5.QtGui import QIcon
from img import *
from CenterWidget import CenterWidget

class MainWindow(QMainWindow):
    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self.resize(800,300)
        self.setWindowTitle("测试窗口")
        self.fileMenu()
        self.setCentralWidget(CenterWidget(self))

    def fileMenu(self):
        fm = self.menuBar().addMenu("文件")
        openAction = QAction("打开", fm)
        openAction.triggered.connect(self.oepn)
        openAction.setIcon(QIcon(":/img/open.png"))
        fm.addAction(openAction)
        tb = self.addToolBar("file")
        tb.addAction(openAction)
        tb.insertSeparator(openAction)

        self.statusBar().showMessage("状态栏 hello world")

    def oepn(self):
        box = QMessageBox()
        box.setText("我的测试box")
        box.setWindowTitle("提示消息")
        box.setInformativeText("确认保存文档")
        box.setStandardButtons(QMessageBox.Save|QMessageBox.Ok|QMessageBox.Cancel)
        box.setDetailedText("my name is tuxl")
        res = box.exec()
