# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QPushButton, QLabel, QFileDialog

class FileChooseDia(QDialog):
    def __init__(self, p):
        super(FileChooseDia, self).__init__(p)
        self.bt = QPushButton(self)
        self.bt.setText("选择")
        self.bt.clicked.connect(self.btreact)
        self.lb = QLabel(self)
        self.resize(500,300)

    def btreact(self):
        fileName = QFileDialog.getOpenFileName(self,
                                                "打开图片",
                                               "",
                                               "Image Files (*.png *.jpg *.bmp);;Text files (*.txt);;XML files (*.xml)")
        print(fileName)
