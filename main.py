from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def File():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("Empty window")
    win.setGeometry(300,500,300,400)

    text = QtWidgets.QLabel(win)
    text.setText('Close this window, please')
    text.move(80,135)
    text.adjustSize()

    btn = QtWidgets.QPushButton(win)
    btn.move(80,170)
    btn.setText('Button')
    btn.setFixedWidth(135)

    win.show()
    sys.exit(app.exec_())


File()
