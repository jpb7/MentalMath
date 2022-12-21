#
#   Jacob Bentley
#   12/21/2022
#   Mental math app
#

from chapterZero import ChapterZero
from PyQt6.QtWidgets import *


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

        layout = QVBoxLayout()
        layout.addWidget(self.display)
        layout.addWidget(self.button)

        self.setLayout(layout)

    
    def run(self):
        """
        Run all problems in `drills`, pausing for button clicks.
        """
        for drill in self.drills.runAll():
            for problem in drill:
                print(problem)

                prob = str(
                    f"<p style='font-size: 24px;'> \
                    {' '.join(problem[:4])} \
                    </p>"
                )

                self.display.setText(prob)
                self.button.setText('Solve')

                #   wait for button click

                soln = str(
                    f"<p style='font-size: 24px;'> \
                    {problem[-1]} \
                    </p>"
                )

                self.display.setText(f"{prob} {soln}")
                self.button.setText('Next')

                #   wait for button click

        self.button.setText('Exit')

        #   wait for button click

        self.close()
    

#    def solve(self):
#        self.display.setText(f"{self.prob} {self.soln}")
#        self.button.setText('Next')
#
#
#    def next(self):
#        self.display.setText(f"{self.prob}")
#        self.button.setText('Solve')
#    
#
#    def exit(self):
#        self.close()


#   Instantiate GUI elements.
 
app = QApplication([])
drills = ChapterZero(3)
window = Exercise(drills)

window.show()


#   Launch.
 
app.exec()
 
