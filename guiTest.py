#
#   Jacob Bentley
#   12/23/2022
#   Mental math app
#

import sys
from PySide6.QtCore import QEventLoop
from PySide6.QtWidgets import *
from chapterZero import ChapterZero
#from PyQt6.QtGui import *


    #   TODO: Wait on button clicks.
    #       : Set the window size.
    #       : Yield problems as tuple of two strings, avoid split/join.

    
class Exercise(QWidget):
    def __init__(self, drills):
        """
        Initialize label for displaying problems, button for clicking through.
        """
        super().__init__()
        self.drills = drills

        self.display = QLabel("Mental math test\n")
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.run)

        self.event = QEventLoop()

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addWidget(self.button)

        self.setLayout(layout)

#        self.run_slot = lambda: self.run()
#        self.solve_slot = lambda: self.solve()
#        self.next_slot = lambda: self.next()
#        self.exit_slot = lambda: self.exit()

    
    def run(self):
        """
        Run all problems in `drills`, pausing for button clicks.
        """
        self.button.clicked.disconnect(self.run)
        self.button.clicked.connect(self.next)

        for drill in self.drills.runAll():
            for problem in drill:

                print(problem) # for debugging

                self.get(problem)

                self.button.clicked.disconnect(self.next)
                self.button.clicked.connect(self.solve)

                # wait for button click

                self.button.clicked.disconnect(self.solve)
                self.button.clicked.connect(self.next)

                # wait for button click

        self.button.setText('Exit')

        self.button.clicked.disconnect(self.next)
        self.button.clicked.connect(self.exit)

        # wait for button click
    

    def get(self, problem):
        self.prob = str(
            f"<p style='font-size: 24px;'> \
            {' '.join(problem[:4])} \
            </p>"
        )
        self.soln = str(
            f"<p style='font-size: 24px;'> \
            {problem[-1]} \
            </p>"
        )


    def solve(self):
        self.display.setText(f"{self.prob} {self.soln}")
        self.button.setText('Next')


    def next(self):
        self.display.setText(f"{self.prob}")
        self.button.setText('Solve')


    def exit(self):
        self.close()


#   Instantiate GUI elements.
 
app = QApplication([])
drills = ChapterZero(3)
window = Exercise(drills)

window.show()


#   Launch.
 
app.exec()
 
