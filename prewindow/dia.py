# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QPushButton

class Dia(QDialog):
    def __init__(self, p):
        super(Dia, self).__init__(p)
        bt = QPushButton(self)
        bt.setText("ok")
        bt.clicked.connect(self.accept)