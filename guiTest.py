#
#   Jacob Bentley
#   12/24/2022
#   Mental math app
#

from chapterZero import ChapterZero
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, \
                              QWidget, QApplication


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

        self.label = QLabel("Mental math test\n")
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.run)

        self.wait = True

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    
    @Slot()
    def run(self):
        """
        Run all problems in `drills`, pausing for button clicks.
        """
        self.button.clicked.disconnect(self.run)
        self.button.clicked.connect(self.display)

        for drill in self.drills.runAll():
            for problem in drill:

                print(problem)

                self.get(problem)
                self.display()

                self.button.clicked.disconnect(self.display)
                self.button.clicked.connect(self.solve)

                # wait for button click

                self.solve()
                self.button.clicked.disconnect(self.solve)
                self.button.clicked.connect(self.display)

                # wait for button click

        self.button.clicked.disconnect(self.display)
        self.button.clicked.connect(self.exit)
        self.button.setText('Exit')

        # wait for button click
    
        self.exit()
    

    def get(self, problem):
        self.prob = ' '.join(problem.split(' ')[:4])
        self.soln = problem.split(' ')[-1]


    @Slot()
    def display(self):
        self.wait = False
        self.label.setText(self.prob)
        self.button.setText('Solve')
        self.wait = True


    @Slot()
    def solve(self):
        self.wait = False
        self.label.setText(f"{self.prob} {self.soln}")
        self.button.setText('Next')
        self.wait = True


    @Slot()
    def exit(self):
        self.close()


#   Instantiate GUI elements.
 
app = QApplication([])
drills = ChapterZero(3)
window = Exercise(drills)

window.show()
 
#   Launch.
  
app.exec()
