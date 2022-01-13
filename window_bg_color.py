from PyQt5 import QtWidgets, QtGui, QtCore
import sys

def window():
    # Initalization of the application
    app = QtWidgets.QApplication(sys.argv)
    
    # create a window
    win = QtWidgets.QWidget()
    
    # set window title
    win.setWindowTitle('Hello World')
    
    # Window Size
    win.setGeometry(100, 100, 400, 300)
    
    # set background color of window
    # win.setStyleSheet('background-color: blue')
    
    # show the window
    win.show()
    
    # execute the app
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
