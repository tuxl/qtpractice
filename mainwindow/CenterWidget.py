# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QPushButton, \
    QGridLayout, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeySequence
from ActionItem import ActionItem

class CenterWidget(QWidget):
    def __init__(self, p):
        super(CenterWidget,self).__init__(p)
        # self.psw = QLineEdit(self)
        # self.psw.setContextMenuPolicy(Qt.NoContextMenu)
        # self.psw.setPlaceholderText("请输入密码")
        # self.psw.setEchoMode(QLineEdit.Password)
        # self.psw.installEventFilter(self)

        self.centralLayout = QVBoxLayout()
        self.addActItem('1111', self.cb)
        self.addActItem('2222', self.cb)
        self.setLayout(self.centralLayout)
        self.centralLayout.addStretch()

    def passwordInputAdviceUsage(self):
        act = ActionItem(self, "密码输入框防复制功能", self.cb)
        self.centralLayout.addWidget(act)

    def cb(self):
        print("我是回调函数")

    def addActItem(self, title, callback):
        self.centralLayout.addWidget(ActionItem(self, title, callback))

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


