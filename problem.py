#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#

from random import randrange


#   Base class for problem generators.

class Problem():
    def __init__(self, start, stop):
        """
        Set range, generate random numbers.
        Random values are N such that (start <= N < stop).
        """
        self.setRange(start, stop)


    #   TODO: dump as JSON object.

    def dump(self):
        """
        Print fields for debugging.
        """
        print("a:", self.a)
        print("b:", self.b)

        return True


    def solve(self):
        """
        Return answer to problem.
        """
        pass


    def shuffle(self):
        """
        Assign new random integers.
        """
        self.a = randrange(self.start, self.stop)
        self.b = randrange(self.start, self.stop)

        return True
    

    def setRange(self, start, stop):
        """
        Enter new range for random values and shuffle.
        Random values are N such that (start <= N < stop).
        """
        self.start = start
        self.stop = stop
        self.shuffle()

        return True


print("Initialize:")
p = Problem(1, 10)
p.dump()

print("Change values:")
p.shuffle()
p.dump()

print("Double digits:")
p.setRange(10, 100)
p.dump()

