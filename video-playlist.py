# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import youtube_dl

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 229)
        MainWindow.setMinimumSize(QtCore.QSize(360, 199))
        MainWindow.setMaximumSize(QtCore.QSize(8888, 8888))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.adrescubugu = QtWidgets.QLineEdit(self.centralwidget)
        self.adrescubugu.setGeometry(QtCore.QRect(140, 80, 181, 31))
        self.adrescubugu.setObjectName("adrescubugu")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.klasoradi = QtWidgets.QPushButton(self.centralwidget)
        self.klasoradi.setGeometry(QtCore.QRect(20, 170, 201, 31))
        self.klasoradi.setObjectName("klasoradi")
        self.indir = QtWidgets.QPushButton(self.centralwidget)
        self.indir.setGeometry(QtCore.QRect(240, 170, 91, 31))
        self.indir.setObjectName("indir")
        self.mp3b = QtWidgets.QRadioButton(self.centralwidget)
        self.mp3b.setGeometry(QtCore.QRect(180, 130, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mp3b.setFont(font)
        self.mp3b.setObjectName("mp3b")
        self.mp4b = QtWidgets.QRadioButton(self.centralwidget)
        self.mp4b.setGeometry(QtCore.QRect(270, 130, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mp4b.setFont(font)
        self.mp4b.setObjectName("mp4b")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 122, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.klasor = ""

        self.retranslateUi(MainWindow)
        self.indir.clicked.connect(self.indirici)
        self.klasoradi.clicked.connect(self.klasorsec)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video/Playlist Downloader"))
        self.label.setText(_translate("MainWindow", "Video/Playlist Downloader"))
        self.label_2.setText(_translate("MainWindow", "Video URL:"))
        self.klasoradi.setText(_translate("MainWindow", "Choose/Change Folder To Save"))
        self.indir.setText(_translate("MainWindow", "Download!"))
        self.mp3b.setText(_translate("MainWindow", "MP3"))
        self.mp4b.setText(_translate("MainWindow", "MP4"))
        self.label_3.setText(_translate("MainWindow", "File Format:"))

    def indirici(self):
        try:
            if self.klasor == "":
                self.hata("You have not selected the folder to save!")
            elif self.mp3b.isChecked() == False and self.mp4b.isChecked() == False:
                self.hata("You not choose file format!")
            else:
                if self.mp3b.isChecked():
                    ydl_opts = {
                        'outtmpl': self.klasor+"\\%(title)s-%(id)s.%(ext)s",
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '320',}],
                    }
                    try:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([self.adrescubugu.text()])
                    except youtube_dl.utils.DownloadError as e:
                        self.hata("Please enter correct adress")

                elif self.mp4b.isChecked():
                    ydl_opts = {
                    'outtmpl': self.klasor+"\\%(title)s-%(id)s.%(ext)s",
                    'format': '135',
                    }
                    try:
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([self.adrescubugu.text()])
                    except:
                        pass
                self.adrescubugu.setText("")
        except:
            self.hata("Something Went Wrong!")

    def klasorsec(self):
        self.klasor = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        caption = "Choose Directory",
        directory = "C:\\users\\%username%\\Desktop",
        options = QtWidgets.QFileDialog.ShowDirsOnly,
        )

    def hata(self, mesaj):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(mesaj)
        msg.setWindowTitle("Error")
        msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
