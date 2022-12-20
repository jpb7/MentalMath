#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#

from problem import Problem


#   For generating multiplication problems. 

class Multiply(Problem):
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        """
        super().__init__(start, stop)
    

    def dump(self):
        """
        Print base fields and product.
        """
        super().dump()
        print(f"Prod: {self.solve()}")
    

    def display(self):
        """
        Return problem as a string for graphical display.
        """
        return f"{self.a} \u00d7 {self.b} = {self.solve()}"


    def solve(self):
        """
        Return product.
        """
        return self.a * self.b


#   Tests.

# print("Initialize:")
# p = Multiply(1, 10)
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
# print("Multiply by 11:")
# p.shuffle()
# p.setA(11)
# p.dump()
#
# print("Display:")
# p.shuffle()
# print(p.display())
# 