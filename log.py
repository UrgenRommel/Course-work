import os
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap,QMovie,QStandardItemModel,QStandardItem
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent,QMediaPlaylist,QMediaMetaData
import sys
class mp3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('start.ui')
        self.ui.setWindowTitle('MP3')
        self.player = QMediaPlayer(self)
        self.list = QMediaPlaylist(self.player)

        self.files = os.listdir()
        self.clear_list = []
        self.list_control()
        self.addlist()

        self.player.setPlaylist(self.list)
        self.list.setPlaybackMode(QMediaPlaylist.Loop)

        self.plays()
        #print(self.files)
        self.ui.co.addItems(self.clear_list)
        self.num = -1
        self.ui.show()


    def nastr(self):
        pass

    def list_control(self):
        f = 'mp3'
        for i in self.files:
            fil = i.split('.')
            if len(fil) >= 2:
                fild = fil[-1].lower()
            if fild in f:
                self.clear_list.append(i)
    def addlist(self):
        kas = []
        for i in self.clear_list:
            kas.append(QStandardItem(i))
            self.list.addMedia(QMediaContent(QUrl(i)))

    def initt_play(self):
        self.num = -self.num
        self.ui.name_music.setText(self.clear_list[self.list.currentIndex()])
        self.ui.name_music.setStyleSheet('color: white')
        if self.num == 1:
            self.ui.play.setText('Pause')
            self.player.play()
        else:
            self.ui.play.setText('Play')
            self.player.pause()

    def plays(self):
        self.ui.play.clicked.connect(self.initt_play)
        self.ui.horizontalSlider.valueChanged.connect(self.volm)
        self.ui.next.clicked.connect(self.next)
        self.ui.back.clicked.connect(self.back)
        self.player.positionChanged.connect(self.vals)
        self.ui.co.activated[int].connect(self.set_m)



    def set_m(self,va):
        self.list.setCurrentIndex(va)
        self.ui.name_music.setText(self.clear_list[self.list.currentIndex()])
        self.ui.name_music.setStyleSheet('color: white')


    def vals(self,ev):
        self.ui.progressBar.setRange(0,self.player.duration())
        self.ui.progressBar.setValue(ev)




    def back(self):
        self.list.previous()
        self.ui.name_music.setText(self.clear_list[self.list.currentIndex()])
        self.ui.name_music.setStyleSheet('color: white')
        self.ui.co.setCurrentIndex(self.list.currentIndex())
    def next(self):
        self.list.next()
        self.ui.name_music.setText(self.clear_list[self.list.currentIndex()])
        self.ui.name_music.setStyleSheet('color: white')
        self.ui.co.setCurrentIndex(self.list.currentIndex())
    def volm(self,event):
        self.ui.loudness.setText(str(event))
        self.ui.loudness.setStyleSheet('color: white')
        self.player.setVolume(int(event))




app = QApplication(sys.argv)
st = mp3()
sys.exit(app.exec_())
