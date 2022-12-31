#
#   Jacob Bentley
#   12/30/2022
#   Mental math app
#

from math import floor, ceil
from random import randrange


#   Base class for problem generators.

class Problem():
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        Random values are N such that (start <= N < stop).
        """
        self.setRange(start, stop)


    def setRange(self, start, stop):
        """
        Enter new range for random values and shuffle.
        Random values are N such that (start <= N < stop).
        """
        self.start, self.stop = start, stop
        self.shuffle()


    def shuffle(self):
        """
        Assign new random integers.
        """
        self.a = randrange(self.start, self.stop)
        self.b = randrange(self.start, self.stop)
    

    def dump(self):
        """
        Print fields for debugging.
        """
        print("a:", self.a)
        print("b:", self.b)

    
    def display(self):
        """
        Return problem as a string for graphical display.
        """
        pass


    def solve(self):
        """
        Return answer to problem.
        """
        pass


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


    def display(self):
        """
        Return problem as a string for graphical display.
        """
        return (f"{self.a} + {self.b} =", f"{self.solve()}")


    def solve(self):
        """
        Return sum.
        """
        return self.a + self.b


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
        return (f"{self.a} - {self.b} =", f"{self.solve()}")


    def solve(self):
        """
        Return difference (always positive by default).
        """
        return abs(self.a - self.b) if self.absolute else self.a - self.b


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
        return (f"{self.a} \u00d7 {self.b} =", f"{self.solve()}")


    def solve(self):
        """
        Return product.
        """
        return self.a * self.b


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


    def display(self):
        """
        Return problem as a string for graphical display.
        """
        return (f"{self.a} \u00f7 {self.b} =", f"{self.solve()}")
    

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


    def display(self):
        """
        Return problem as a string for graphical display.
        """
        return (f"{self.a}\u00b2 =", f"{self.solve()}")


#   Test.

#test = Square(10, 100)
#print(test.display())

