import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setMinimumSize(QtCore.QSize(622, 433))
        self.pic.setMaximumSize(QtCore.QSize(622, 433))
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.verticalLayout_2.addWidget(self.pic)
        self.draw = QtWidgets.QPushButton(self.centralwidget)
        self.draw.setObjectName("draw")
        self.verticalLayout_2.addWidget(self.draw)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.draw.setText(_translate("MainWindow", "Draw"))


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.border_down = (50, 50)
        self.border_up = (600, 450)
        self.draw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setBrush(QColor(*color))
        center = (randint(self.border_down[0], self.border_up[0]), randint(self.border_down[1], self.border_up[1]))
        radius = randint(5, 100)
        qp.drawEllipse(*center, radius, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
