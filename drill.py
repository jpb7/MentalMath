#
#   Jacob Bentley
#   12/30/2022
#   Mental math app
#   

from problem import Problem


#   Base class for drills, which run problem generators.

class Drill():
    def __init__(self, problemGenerator, n):
        """
        Initialize problem generator and number of problems.
        """
        self.generator = None
        self.problems = None
        self.reset(problemGenerator, n)


    def __iter__(self):
        """
        Make class object iterable so GUI can call `next()` on it.
        """
        return self


    def __next__(self):
        """
        Yield one problem at a time per drill up to `n`.
        """
        self.problems -= 1
        self.generator.shuffle()
        yield self.generator.display()

    
    def reset(self, problemGenerator, n):
        """
        Set the problem generator to a given type.
        """
        if isinstance(problemGenerator, Problem):
            self.generator = problemGenerator
            self.problems = n

        else:
            raise ValueError("Drill object received invalid problem generator.")


    def run(self):
        """
        Generate and output problems using a loop.
        """
        for _ in range(self.problems):
            self.generator.shuffle()
            yield self.generator.display()
        

#   Run all drills for a given chapter with `n` problems per drill.

class Chapter(Drill):
    def __init__(self, generators, n):
        """
        Initialize to first drill for `n` repetitions.
        """
        self.generators = generators
        self.current = next(self.generators)
        self.n = n

        super().__init__(self.current, self.n)

    
    def __next__(self):
        """
        Yield one problem at a time per drill up to `n`.
        """
        if self.problems:
            return super().__next__()

        self.current = next(self.generators)
        self.reset(self.current, self.n)


    def runAll(self):
        """
        Generate `n` problems per drill using a loop.
        """
        for gen in self.generators:
            self.reset(gen)
            yield self.run()


#   Test.

# drill = Drill(Add(10, 100), 5)
# print(type(drill.run()))

# drill.run()
# 
# drill = Drill(Subtract(10, 100), 5)
# drill.run()
# 
# drill = Drill(Multiply(10, 100), 5)
# drill.run()
# 
# 