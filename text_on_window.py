# showing test on the screen

from PyQt5 import QtWidgets,QtCore,QtGui
import sys

# Initalize
app = QtWidgets.QApplication(sys.argv)

# set a Text on window
label = QtWidgets.QLabel('Hello World')

# Set the position of text on window
label.setAlignment(QtCore.Qt.AlignCenter)

# Set the window name
label.setWindowTitle('GUI')

# set the style and color of text on window
label.setStyleSheet('color: red')
label.setFont(QtGui.QFont('Arial',30))

# set the size of window 
label.resize(400, 300)
# label.setGeometry(QtCore.QRect(0, 0, 400, 300))

# show the window
label.show()

# execute the app
sys.exit(app.exec_())
