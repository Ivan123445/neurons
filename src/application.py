import os
import sys
import subprocess
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QColor


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()

        # window
        self.setWindowTitle("Распознаватель текста")  # добавление виджетов и установка параметров
        # self.resize(1000, 500)

        # title
        self.title = QLabel(self)
        self.title.setText("Выберите файл")
        self.title.move(100, 70)
        self.title.adjustSize()

        # buttons
        self.btnSetFile = QPushButton("Выбрать файл", self)
        self.btnSetFile.move(30, 150)
        self.btnSetFile.setFixedSize(250, 50)
        self.btnSetFile.clicked.connect(self.evt_btn_set_file_clicked)

        self.btnStartAlg = QPushButton("Начать обработку", self)
        self.btnStartAlg.move(30, 210)
        self.btnStartAlg.setFixedSize(250, 50)
        self.btnStartAlg.clicked.connect(self.evt_btn_start_alg_clicked)

        self.btnExit = QPushButton("Выход", self)
        self.btnExit.move(30, 300)
        self.btnExit.setFixedSize(250, 50)
        # self.btnStartAlg.clicked.connect()  # todo exit with delete files

        # img
        self.img_preview = QLabel(self)
        self.img_preview.setFixedSize(600, 350)
        self.img_preview.move(300, 20)
        self.pixmap = QPixmap(600, 350)
        self.pixmap.fill()
        self.img_preview.setPixmap(self.pixmap)

        # result
        self.ledResText = QLineEdit("Результат", self)  # todo grey text
        self.ledResText.move(300, 380)
        self.ledResText.setFixedSize(600, 60)

    def evt_btn_set_file_clicked(self):  # todo normal way
        print("Trying to choose file")
        path, _ = QFileDialog.getOpenFileName(self, "Выберете файл",\
                                             '../data/test', 'JPG File (*.jpg);;PNG File (*.png)')
        my_file = open("$temp_path_file.txt", "w+")
        my_file.write(path)
        my_file.close()

        self.set_img(path)
        self.ledResText.setText("")
        print(path)

    def evt_btn_start_alg_clicked(self):
        print("Trying to start alg")
        if os.path.exists("$temp_path_file.txt"):  # todo normal way
            print("Start alg")
            subprocess.Popen([sys.executable, 'process_image.py'])
            path_file = open("$temp_recognised_char.txt", "r")
            self.set_result(path_file.read())           # todo remove overlay
            # os.remove('$temp_path_file.txt')
        else:
            print("No file")
            QMessageBox.information(self, "Не найден файл!", "Пожалуйста, выберете файл")

    def set_result(self, string):
        self.ledResText.setText(string)

    def set_img(self, path):
        print("Set img")
        self.pixmap.load(path)
        self.img_preview.setPixmap(self.pixmap.scaled(600, 350))


if __name__ == '__main__':  # значит, что он не импортирован, и запускается в основной программе
    app = QApplication(sys.argv)  # создание приложения
    dlgMain = DlgMain()  # создание главного окна
    dlgMain.show()
    sys.exit(app.exec_())
