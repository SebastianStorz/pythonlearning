import sys

from PySide2.QtWidgets import QApplication, QLabel, QPushButton


app = QApplication(sys.argv)

#label = QLabel("Hello World!")

label = QLabel("<font color=red size=50>Hello World!</font>")

label.show()

app.exec_()
