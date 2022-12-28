#
#   Jacob Bentley
#   12/27/2022
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
        self.button.clicked.connect(self.runDrills)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        #   Flags for controlling click behavior.

        self.prompt = True      # show problem
        self.solve = False      # show problem with solution


    #   TODO: use the next() method of the generators,
    #         integrate into GUI.

    
    @Slot()
    def runDrills(self):
        """
        Show each problem in `self.drills`; first just the problem,
        then the problem together with its solution.
        """
        if self.prompt:
            self.showProblem()

        elif self.solve:
            self.showSolution()
        
    
    def showProblem(self):
        """
        Change label text to display a problem from `self.drills`.
        """
        self.prompt = False
        self.label.setText("Problem.")
        self.button.setText('Solve')
        self.solve = True
    
    
    def showSolution(self):
        """
        Change label text to display a problem and its solution.
        """
        self.solve = False
        self.label.setText("Solution.")
        self.button.setText("Next")
        self.prompt = True


#    def get(self, problem):
#        self.prob = ' '.join(problem.split(' ')[:4])
#        self.soln = problem.split(' ')[-1]
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

