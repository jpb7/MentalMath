#
#   Jacob Bentley
#   12/30/2022
#   Mental math app
#

from chapter0 import ChapterZero
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, \
                              QWidget, QApplication

    #
    #   TODO:
    #       : Generalize ChapterZero class to Chapter.
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
        self.current = next(self.drills)

        #   Initialize strings.

        self.problem = self.solution = ""

    
    @Slot()
    def runDrills(self):
        """
        Show each problem in `self.drills`; first just the problem,
        then the problem together with its solution.
        """
        try:

            if self.prompt:
                self.getProblem()
                self.showProblem()

            elif self.solve:
                self.showSolution()

            self.current = next(self.drills)

        except StopIteration:
            self.close()
            
    
    def getProblem(self):
        """
        Store problem in two parts: prompt and solution.
        """
        self.problem, self.solution = next(self.current)
    
    
    def showProblem(self):
        """
        Change label text to display a problem from `self.drills`.
        """
        self.prompt = False
        self.label.setText(self.problem)
        self.button.setText('Solve')
        self.solve = True
    

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

