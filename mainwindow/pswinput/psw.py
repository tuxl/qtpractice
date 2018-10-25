# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QLineEdit, QWidget
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QKeySequence
from .custominput import CustomInput

# 给密码输入框增加事件安装事件过滤器

class Psw(QDialog):
    def __init__(self, p):
        super(Psw,self).__init__(p)
        print("aaaaa")
        self.pswInput = QLineEdit(self)
        self.pswInput.setContextMenuPolicy(Qt.NoContextMenu)
        self.pswInput.setPlaceholderText("请输入密码")
        self.pswInput.setEchoMode(QLineEdit.Password)
        self.pswInput.installEventFilter(self)

    def eventFilter(self, obj, ev):
        if obj == self.pswInput:
            if ev.type() in (QEvent.MouseMove, QEvent.MouseButtonDblClick):
                return True
            elif ev.type() == QEvent.KeyPress:
                if ev.matches(QKeySequence.SelectAll) \
                    or ev.matches(QKeySequence.Copy)\
                    or ev.matches(QKeySequence.Paste):
                    return True
        return QDialog.eventFilter(self,obj, ev)