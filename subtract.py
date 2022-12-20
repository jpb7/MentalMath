#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#

from problem import Problem


#   For generating subtraction problems. 

class Subtract(Problem):
    def __init__(self, start, stop, absolute = True):
        """
        Set range, generate random numbers.
        """
        super().__init__(start, stop)
        self.absolute = absolute
    

    def dump(self):
        """
        Print base fields and difference.
        """
        super().dump()
        print(f"Diff: {self.solve()}")
    

    def display(self):
        """
        Return problem as a string for graphical display.
        """
        return f"{self.a} - {self.b} = {self.solve()}"


    def solve(self):
        """
        Return difference (always positive by default).
        """
        return abs(self.a - self.b) if self.absolute else self.a - self.b


#   Tests.

# print("Initialize:")
# p = Subtract(1, 10)
# p.dump()
# 
# print("Change values:")
# p.shuffle()
# p.dump()
# 
# print("Double digits:")
# p.setRange(10, 100)
# p.dump()
# 
# print("Allow negatives:")
# p.absolute = False
# p.shuffle()
# p.dump()
# 
# print("Display:")
# p.shuffle()
# print(p.display())
# 