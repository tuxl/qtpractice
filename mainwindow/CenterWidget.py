# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeySequence

class CenterWidget(QWidget):
    def __init__(self, p):
        super(CenterWidget,self).__init__(p)
        self.psw = QLineEdit(self)
        self.psw.setContextMenuPolicy(Qt.NoContextMenu)
        self.psw.setPlaceholderText("请输入密码")
        self.psw.setEchoMode(QLineEdit.Password)
        self.psw.installEventFilter(self)


    def eventFilter(self, obj, ev):
        if obj == self.psw:
            if ev.type() in (QEvent.MouseMove, QEvent.MouseButtonDblClick):
                return True
            elif ev.type() == QEvent.KeyPress:
                if ev.matches(QKeySequence.SelectAll) \
                    or ev.matches(QKeySequence.Copy)\
                    or ev.matches(QKeySequence.Paste):
                    return True
        return QWidget.eventFilter(self,obj, ev)


