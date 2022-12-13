#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#

from problem import Problem


#   For generating addition problems. 

class Add(Problem):
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        """
        super().__init__(start, stop)


    def dump(self):
        """
        Print base fields and sum.
        """
        super().dump()
        print(f"Sum: {self.solve()}")

        return True


    def solve(self):
        """
        Return sum.
        """
        return self.a + self.b


#   Tests.

print("Initialize:")
p = Add(1, 10)
p.dump()

print("Change values:")
p.shuffle()
p.dump()

print("Double digits:")
p.setRange(10, 100)
p.dump()

