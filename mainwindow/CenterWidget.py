# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QDialog
from ActionItem import ActionItem
from pswinput.psw import Psw
from filechooser.FileChooseDia import FileChooseDia

class CenterWidget(QWidget):
    def __init__(self, p):
        super(CenterWidget,self).__init__(p)

        self.centralLayout = QVBoxLayout()
        self.addActItem()
        self.setLayout(self.centralLayout)
        self.centralLayout.addStretch()

    def addActItem(self):
        actions = [
            {
                'name':"密码输入框阻止复制，选择，",
                'callback':self.passwordProcess,
            },
            {
                'name':"文件选择器",
                'callback':self.fileChoose,
            },
        ]
        for item in actions:
            self.centralLayout.addWidget(ActionItem(self, item['name'], item['callback']))

    def passwordProcess(self):
        dia = Psw(self)
        dia.exec()

    def fileChoose(self):
        dia = FileChooseDia(self)
        dia.exec()