#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#   

from drill import Drill
from multiply import Multiply

#   TODO: create base class, make this inherit.

#   For multiplying two- or three-digit numbers by 11.

class MultByEleven(Drill):
    def __init__(self, numProblems, digits = 2):
        """
        Initialize Multiply object for either 2 or 3 digits,
        and specify number of problems to generate.
        """
        if digits == 2:
            super().__init__(Multiply(10, 100), numProblems)
        elif digits == 3:
            super().__init__(Multiply(100, 1000), numProblems)
        else:
            raise ValueError("Digits must be either 2 or 3.")


    def run(self):
        """
        Generate and output problems.
        """
        for i in range(self.problems):
            self.generator.shuffle()
            self.generator.setA(11)
            self.generator.dump()

        return True
        

#   Test.

drill = MultByEleven(10)
drill.run()

