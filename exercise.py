#
#   Jacob Bentley
#   01/07/2023
#   Mental math app
#

from chapter0 import ChapterZero
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, \
                              QWidget, QApplication

    #
    #   TODO:
    #       : Start working on a Menu class.
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

        #   Initialize drills and declare current drill.

        self.drills = drills
        self.drill = None

        #   Initialize strings.

        self.problem = self.solution = ""

    
    @Slot()
    def run(self):
        """
        Show each problem in `self.drills`: on first button click,
        just the problem; on second button click, show the problem
        together with its solution.
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
            self.close()


    def getProblem(self):
        """
        Get the next problem in the current drill, or else iterate
        to the next drill and get the problem there.
        """
        try:

            if not self.drill:
                self.drill = next(self.drills)

            self.problem, self.solution = next(self.drill)

        except StopIteration:
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

#   Launch.
  
window.show()
app.exec()

