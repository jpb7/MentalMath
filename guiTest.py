#
#   Jacob Bentley
#   12/27/2022
#   Mental math app
#

from chapterZero import ChapterZero
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, \
                              QWidget, QApplication

    #
    #   TODO:
    #       : Iterate through different drills.
    #       : Set the window size.
    #       : Yield problems as tuple of two strings, avoid split/join.
    #
    
class Exercise(QWidget):
    def __init__(self, drills):
        """
        Initialize label for displaying problems, button for clicking through.
        """
        super().__init__()

        self.label = QLabel("Mental math test\n")
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.runDrills)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        #   Flags for controlling click behavior.

        self.prompt = True      # show problem
        self.solve = False      # show problem with solution

        #   Initialize first problem of first drill.

        self.drills = drills
        self.currentDrill = next(self.drills.runAll())
        self.currentProblem = next(self.currentDrill)

    
    @Slot()
    def runDrills(self):
        """
        Show each problem in `self.drills`; first just the problem,
        then the problem together with its solution.
        """
        try:

            if self.prompt:
                self.showProblem()

            elif self.solve:
                self.showSolution()

            self.currentProblem = next(self.currentDrill)

        except StopIteration:

            try:
                self.currentDrill = next(self.drills.runAll())

            except StopIteration:
                self.close()
            
    
    def showProblem(self):
        """
        Change label text to display a problem from `self.drills`.
        """
        self.prompt = False
        self.getProblem()
        self.label.setText(self.problem)
        self.button.setText('Solve')
        self.solve = True
    

    def getProblem(self):
        """
        Split generated problem into prompt and solution.
        Will be removed when return values of generators are changed.
        """
        self.problem = ' '.join(self.currentProblem.split(' ')[:4])
        self.solution = self.currentProblem.split(' ')[-1]
    
    
    def showSolution(self):
        """
        Change label text to display a problem and its solution.
        """
        self.solve = False
        self.label.setText(f"{self.problem} {self.solution}")
        self.button.setText('Next')
        self.prompt = True


#   Instantiate GUI elements.
 
app = QApplication([])
drills = ChapterZero(3)
window = Exercise(drills)

window.show()
 

#   Launch.
  
app.exec()

