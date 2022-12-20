#
#   Jacob Bentley
#   12/19/2022
#   Mental math app
#

from chapterZero import ChapterZero
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QCoreApplication


#   TODO: yield problems as a tuple of two strings to avoid splitting/joining.
#       : figure out button clicks and program flow
#       : make a GUI class

def runExercise(drills):
    #button.setText('Solve')
    for drill in drills.runAll():
        for problem in drill:
            print(problem)
#            problem = problem.split(' ')
#            prob = str(f"<p style='font-size: 24px;'> {' '.join(problem[:4])} </p>")
#            soln = str(f"<p style='font-size: 24px;'> {problem[-1]} </p>")
#            label.setText(prob)
#            button.clicked.connect(lambda: solve(prob, soln))  
#            button.clicked.connect(lambda: goNext())

def solve(problem, solution):
    label.setText(
        f"<p style='font-size: 24px;'> {problem} {solution} </p>"
    )
    button.setText('Next')

def goNext():
    button.setText('Solve')

#   Instantiate GUI elements.

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

label = QLabel("Mental math test\n")
button = QPushButton('Start')

drills = ChapterZero(3)

#   Compose widgets and display window.

layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.show()
runExercise(drills)

button.clicked.connect(QCoreApplication.instance().quit)
#button.clicked.connect(lambda: runExercise(drills))

#   Launch.

app.exec()

# QCoreApplication.instance().quit
