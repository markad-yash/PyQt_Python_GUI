#create a empty window

from PyQt5 import QtWidgets
import sys

# Initalization of the application
app = QtWidgets.QApplication(sys.argv)

# Create a window
win = QtWidgets.QDialog()

# window size
# win.resize(400, 300)
win.setGeometry(100, 100, 400, 300)

# window title
win.setWindowTitle('Hello World')

# show the window
win.show()

# execute the application
sys.exit(app.exec_())
