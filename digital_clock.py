import sys
import time
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout)
from PyQt5.QtCore import (QTimer, QTime, Qt)
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.label = QLabel(self)
        self.timer = QTimer(self)
        self.initUi()

    def initUi(self):
        # self.setGeometry(600,400,300,100)
        self.setStyleSheet("background-color: black;")

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)

        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 150px;"
                                 "color: hsl(111,100%,50%);")
        
        font_id = QFontDatabase.addApplicationFont("assets/Technology.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.label.setFont(my_font)
        
        self.timer.timeout.connect(self.currentTime)
        self.timer.start(1000)

        self.currentTime()
        
    def currentTime(self):
        current_time=QTime.currentTime().toString("hh:mm:ss ap")
        self.label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()