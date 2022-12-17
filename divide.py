#
#   Jacob Bentley
#   12/16/2022
#   Mental math app
#

from math import floor, ceil
from problem import Problem


#   For generating division problems. 

class Divide(Problem):
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        """
        super().__init__(start, stop)
        self.options = {'float', 'floor', 'ceil'}
        self.mode = 'float'
    

    def dump(self):
        """
        Print base fields and quotient.
        """
        super().dump()
        print(f"Quot: {self.solve()}")
    

    def solve(self):
        """
        Return quotient depending on mode.
        """
        if self.mode == 'floor':
            return floor(self.a / self.b)
        elif self.mode == 'ceil':
            return ceil(self.a / self.b)
        
        return round(self.a / self.b, 3)

    
    def setMode(self, mode):
        """
        Validate input and change division mode.
        """
        mode = mode.lower()
        if mode not in self.options:
            raise ValueError("Not a valid mode.")

        self.mode = mode


#   Tests.

print("Initialize:")
p = Divide(10, 100)
p.dump()

print("Floor division:")
p.setMode('floor')
p.shuffle()
p.dump()

print("Ceiling division:")
p.setMode('ceil')
p.shuffle()
p.dump()

print("Invalid mode:")
try:
    p.setMode('wall')
except ValueError:
    print('Detected.')

print("Valid mode, capitalized:")
try:
    p.setMode('Float')
    print('Success.')
except ValueError:
    print('Failure.')

