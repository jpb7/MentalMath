#
#   Jacob Bentley
#   12/16/2022
#   Mental math app
#

from problem import Problem


#   For generating division problems. 

class Divide(Problem):
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        """
        super().__init__(start, stop)
    

    def dump(self):
        """
        Print base fields and quotient.
        """
        super().dump()
        print(f"Quot: {self.solve()}")
    

    def solve(self):
        """
        Return quotient.
        """
        return round(self.a / self.b, 3)


#   Tests.

print("Initialize:")
p = Divide(1, 10)
p.dump()

print("Change values:")
p.shuffle()
p.dump()

print("Double digits:")
p.setRange(10, 100)
p.dump()

