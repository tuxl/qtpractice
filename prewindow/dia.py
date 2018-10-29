# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QFormLayout, \
    QHBoxLayout, QLineEdit, QMessageBox

class Dia(QDialog):
    def __init__(self, p):
        super(Dia, self).__init__(p)
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        f_layout = QFormLayout()
        i_user = QLineEdit()
        i_psw = QLineEdit()
        i_psw.setEchoMode(QLineEdit.Password)
        f_layout.addRow("用户名:", i_user)
        f_layout.addRow("密码:", i_psw)
        self.i_user = i_user
        self.i_psw = i_psw

        h_layout = QHBoxLayout()
        ok_btn = QPushButton("确定")
        ok_btn.clicked.connect(self.verifyInput)
        cancel_btn = QPushButton("取消")
        cancel_btn.clicked.connect(self.reject)
        h_layout.addWidget(ok_btn)
        h_layout.addWidget(cancel_btn)

        v_layout.addLayout(f_layout)
        v_layout.addLayout(h_layout)

    def verifyInput(self):
        user = self.i_user.text()
        psw = self.i_psw.text()
        print(user, psw)
        if user != 'root' or psw != '123456':
            QMessageBox.warning(self, "警告", "用户名密码错误", QMessageBox.Yes)
            self.reject()
        else:
            self.accept()
