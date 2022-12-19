#
#   Jacob Bentley
#   12/19/2022
#   Mental math app
#

from PyQt6.QtWidgets import *
from PyQt6.QtCore import QCoreApplication


#   Instantiate GUI elements.

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
label = QLabel("Mental math test\n")
button = QPushButton('Exit')


#   Compose widgets and display window.

layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)
button.clicked.connect(QCoreApplication.instance().quit)
window.show()


#   Launch.

app.exec()
