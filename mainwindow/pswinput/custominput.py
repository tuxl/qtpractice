# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLineEdit, QWidget
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QKeySequence

class CustomInput(QLineEdit):
    def __init__(self, p):
        super(CustomInput, self).__init__(p)
        self.installEventFilter(self)
