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
    #       : Generalize GUI class.
    #       : Fix extra iterations: not displaying last problem.
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

        self.chapter = drills
        self.drill = next(self.chapter)

        #   Initialize strings.

        self.problem = self.solution = ""

    
    @Slot()
    def run(self):
        """
        Show each problem in `self.drills`; first just the problem,
        then the problem together with its solution.
        """
        try:

            if self.prompt:
                #self.getProblem()
                self.showProblem()

            elif self.solve:
                self.showSolution()
            
            else:
                self.goToNext()
                self.run()

        except StopIteration:
            self.close()


    def goToNext(self):
        try:
            self.getProblem()

        # TypeError should be StopIteration.
        except (TypeError, StopIteration):
            self.drill = next(self.chapter)
        
        self.prompt = self.solve = True

    
    def getProblem(self):
        """
        Store problem in two parts: prompt and solution.
        """
        self.problem, self.solution = next(self.drill)
    
    
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

