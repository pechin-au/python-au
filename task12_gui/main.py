import sys
from PyQt5 import QtCore
from PyQt5 import QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog,QGraphicsView,QGraphicsScene,QVBoxLayout

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)
from PyQt5.QtGui import QPainter, QColor, QPen, QPainterPath, QPixmap, QImage, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import pyqtSignal, QObject, QPoint, QSize
from PyQt5.QtWidgets import QMainWindow, QApplication
import mnist



class Drawer(QWidget):
    newPoint = pyqtSignal(QPoint)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.path = QPainterPath()
        self.recog = mnist.numRecog()
        self.guess = 0


    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.black, 60, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawPath(self.path)
        pen = QPen(Qt.green, 60, Qt.SolidLine)
        painter.setPen(pen)
        painter.setFont(QFont("Sans Serif", 20))
        painter.drawText(QPoint(20,30), str(self.guess))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.path.moveTo(event.pos())
        elif event.button() == Qt.MiddleButton:
            self.savePic()
        else:
            self.path =  QPainterPath()
        self.update()

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        self.newPoint.emit(event.pos())
        self.update()

    def sizeHint(self):
        return QSize(560, 560)

    def savePic(self):
        img = QImage(28, 28, QImage.Format_ARGB32)
        painter = QPainter(img)
        painter.fillRect(0, 0, 28, 28, Qt.white)
        painter.scale(0.05, 0.05)
        pen = QPen(Qt.black, 60, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawPath(self.path)
        painter.end()
        img.save("img.png", "png")
        self.guess = self.recog.recog_image()



class MyWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setLayout(QVBoxLayout())
        #label = QLabel(self)
        drawer = Drawer(self)
        #drawer.newPoint.connect(lambda p: label.setText('Coordinates: ( %d : %d )' % (p.x(), p.y())))
        #self.layout().addWidget(label)
        self.layout().addWidget(drawer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())