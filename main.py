from PyQt5 import QtWidgets, uic
import sys
import detect
import cv2

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)

        self.button = self.findChild(QtWidgets.QPushButton, 'printButton') # Find the button
        self.button.clicked.connect(self.printButtonPressed) # Remember to pass the definition/method, not the return value!

        self.input = self.findChild(QtWidgets.QLineEdit, 'input')

        self.show()
        #self.input.text()
    def printButtonPressed(self):
        detect.runDetect(self.input.text() + ".png")
        #print(self.input.text())4
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
