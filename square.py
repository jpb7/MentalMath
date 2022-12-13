#
#   Jacob Bentley
#   12/13/2022
#   Mental math app
#

from random import randrange, choice
from multiply import Multiply


#   For generating square problems.

class Square(Multiply):
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        """
        super().__init__(start, stop)


    def shuffle(self):
        """
        Set both `a` and `b` to the same random number. 
        """
        self.a = self.b = randrange(self.start, self.stop)
    

    def dump(self):
        """
        Print value and square it.
        """
        print("a:", self.a)
        print(f"Square: {self.solve()}")


#   For squaring two-digit numbers ending in 5.

class SquareEndInFive(Square):
    def __init__(self):
        """
        Initialize target values and instantiate base-class object.
        """
        self.numbers = (5, 15, 25, 35, 45, 55, 65, 75, 85, 95)
        self.shuffle()

    
    def shuffle(self):
        """
        Randomly select target value from above.
        """
        self.a = self.b = choice(self.numbers)


#   Tests.

print("Initialize:")
p = Square(10, 100)
p.dump()

print("Change values:")
p.shuffle()
p.dump()

print("SquareEndInFive:")
p = SquareEndInFive()
p.dump()

print("Again:")
p.shuffle()
p.dump()

