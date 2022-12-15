#
#   Jacob Bentley
#   12/15/2022
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


#   Tests.

# print("Initialize:")
# p = Square(10, 100)
# p.dump()
# 
# print("Change values:")
# p.shuffle()
# p.dump()
# 
# print("Again:")
# p.shuffle()
# p.dump()
# 
# 