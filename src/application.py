import sys
import os
import subprocess
from PySide2.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QFileDialog, \
    QLineEdit, QLabel, QHBoxLayout, QMessageBox
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QCoreApplication
from PySide2 import QtWidgets

path = '../data/test/test_image_6.jpg'


def choose_file():
    path = QFileDialog.getOpenFileName()[0]
    my_file = open("$temp_path_file.txt", "w+")
    my_file.write(path)
    my_file.close()

    print(path)


def start_processing_file():
    if os.path.exists("$temp_path_file.txt") == False :
        print("hello")
        error = QMessageBox()
        error.setWindowTitle("Warning!")
        error.setText("Choose file!")
    else:
        subprocess.Popen([sys.executable, 'process_image.py'])


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Распознаватель текста")
# смещение             x    y    weigh high
    window.setGeometry(500, 250, 700, 300)

    # '../data/test/test_image_6.jpg'

    title = QtWidgets.QLabel(window)
    title.setText("Выберите файл")
    title.move(50, 50)
    title.adjustSize()

    btn_choose_file = QtWidgets.QPushButton(window)
    btn_choose_file.move(30, 240)
    btn_choose_file.setFixedWidth(250)
    btn_choose_file.setText("Choose file")
    btn_choose_file.clicked.connect(choose_file)

    btn_process = QtWidgets.QPushButton(window)
    btn_process.move(30, 200)
    btn_process.setFixedWidth(250)
    btn_process.setText("Start processing")
    btn_process.clicked.connect(start_processing_file)

    # hbox = QHBoxLayout(window)
    # pix = QPixmap('../data/test/test_image_6.jpg')
    # lbl = QLabel(window)
    # # pix = QPixmap('../data/test/test_image_6.jpg')
    # # pix.load()
    # lbl.setPixmap(pix)
    # hbox.addWidget(lbl)
    # window.setLayout(hbox)

    hbox = QHBoxLayout(window)
    pixmap = QPixmap(1000, 1000)
    pixmap.load('../data/test/test_image_6.jpg')
    lbl = QLabel(window)
    QLabel()
    lbl.move(250, 10)
    lbl.setPixmap(pixmap)
    hbox.addWidget(lbl)
    window.setLayout(hbox)


    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
