#
#   Jacob Bentley
#   01/04/2023
#   Mental math app
#

from chapter0 import ChapterZero
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, \
                              QWidget, QApplication

    #
    #   TODO:
    #       : Fix lingering iteration problems.
    #

class Exercise(QWidget):
    def __init__(self, label, drills):
        """
        Initialize label for displaying problems, button for clicking through.
        """
        super().__init__()

        self.label = QLabel(label + "\n")
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.run)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        #   Flags for controlling click behavior.

        self.prompt = False     # show problem
        self.solve = False      # show problem with solution

        #   Initialize first problem of first drill.

        self.drills = drills
        self.drill = next(self.drills)

        #   Initialize strings.

        self.problem = self.solution = ""

        # For debugging.
        self.total = 0
        self.stopIter = 0
        self.typeError = 0

    
    @Slot()
    def run(self):
        """
        Show each problem in `self.drills`; first just the problem,
        then the problem together with its solution.
        """
        try:

            if self.prompt:
                self.showProblem()

            elif self.solve:
                self.showSolution()
            
            else:
                self.getProblem()
                self.run()

        except StopIteration:
            print("Exceptions:", self.total)
            print("TypeError:", self.typeError)
            print("StopIteration:", self.stopIter)
            self.close()


    def getProblem(self):
        """
        Get the next problem in the current drill, or else iterate
        to the next drill and get the problem there.
        """
        try:
            self.problem, self.solution = next(self.drill)

        except TypeError:
            self.typeError += 1
            self.total += 1
            self.drill = next(self.drills)
            self.getProblem()
        
        except StopIteration:
            self.stopIter += 1
            self.total += 1
            self.drill = next(self.drills)
            self.getProblem()
    
        self.prompt = self.solve = True

    
    def showProblem(self):
        """
        Change label text to display a problem from `self.drills`.
        """
        self.prompt = False
        self.label.setText(self.problem)
        self.button.setText('Solve')
    

    def showSolution(self):
        """
        Change label text to display a problem and its solution.
        """
        self.solve = False
        self.label.setText(f"{self.problem} {self.solution}")
        self.button.setText('Next')


#   Instantiate GUI elements.
 
app = QApplication([])

drills = ChapterZero(3)
window = Exercise("Mental math test", drills)

window.show()
 

#   Launch.
  
app.exec()

