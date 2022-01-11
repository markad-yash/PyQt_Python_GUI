# creating a button on window

from PyQt5 import QtWidgets
import sys

# Initalization of the application
app = QtWidgets.QApplication(sys.argv)

# Create a window
win = QtWidgets.QWidget()

# window Title
win.setWindowTitle('Hello World')

# Window Size
win.resize(400, 300)

# Button creation
btn = QtWidgets.QPushButton(win)

# Button text
btn.setText('Click Me')

# Button Size
btn.resize(100, 50)

# Button Position
btn.move(150, 100)

# define a function for button
def btn_fn():
    print('Clicked')

# Button Function
# btn.clicked.connect(lambda: print('Hello World'))
btn.clicked.connect(btn_fn)

# Show the window
win.show()

# Execute the application
sys.exit(app.exec_())
