import sys

from PySide2.QtWidgets import QApplication, QPushButton

def say_hello():
    print("Button clicked, Hello!")

app = QApplication(sys.argv)
Button1 = QPushButton("Click me")
Button1.clicked.connect(say_hello)
Button1.show()

app.exec_()
