#!/usr/bin/python3
# -*- coding: utf-8 -*-
# noinspection PyUnresolvedReferences

# import cv2

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets


def start_processing():
    print("start")

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Тайтл, хуле")
    window.setGeometry(500, 250, 350, 200)

    title = QtWidgets.QLabel(window)
    title.setText("Хуле, тайтл")
    title.move(100, 100)
    title.adjustSize()

    btn = QtWidgets.QPushButton(window)
    btn.move(70, 150)
    btn.setText("Кнопка")
    btn.clicked.connect(start_processing)


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    application()

