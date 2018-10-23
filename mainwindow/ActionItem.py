# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QSizePolicy

class ActionItem(QWidget):
    def __init__(self, p, title, callback):
        super(ActionItem, self).__init__(p)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout = QHBoxLayout()
        name = QLabel(title)
        bt = QPushButton("启动")
        layout.addWidget(name)
        layout.addStretch(1)
        layout.addWidget(bt)
        self.setLayout(layout)
        bt.clicked.connect(callback)
