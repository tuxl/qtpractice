# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from pswinput.psw import Psw
from filechooser.FileChooseDia import FileChooseDia

class CenterWidget(QWidget):
    def __init__(self, p):
        super(CenterWidget,self).__init__(p)

        self.centralLayout = QGridLayout()
        self.addActItem()
        self.setLayout(self.centralLayout)
        self.centralLayout.setColumnStretch(0,1)

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
        for k, item in enumerate(actions, 1) :
            lb = QLabel(item['name'])
            bt = QPushButton("启动")
            bt.clicked.connect(item['callback'])
            self.centralLayout.addWidget(lb, k, 0)
            self.centralLayout.addWidget(bt, k, 1)

    def passwordProcess(self):
        dia = Psw(self)
        dia.exec()

    def fileChoose(self):
        dia = FileChooseDia(self)
        dia.exec()