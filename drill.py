#
#   Jacob Bentley
#   12/12/2022
#   Mental math app
#   

from base import Problem


#   Base class for drills, which run problem generators.

class Drill():
    def __init__(self, problemGenerator, n):
        """
        Initialize problem generator and number of problems.
        """
        self.reset(problemGenerator, n)


    def __iter__(self):
        """
        Make class object iterable so GUI can call `next()` on it.
        """
        return self


    #   TODO: Separate yield from iteration (see line 90 in guiTest).
    #       : Line 90 in guiTest vs Line 65.
    #       : Default parameters?

    def __next__(self, problemGenerator = None, n = None):
        """
        Yield one problem at a time per drill up to `n`.
        """
        try:
            if self.problems:
                self.problems -= 1
                self.generator.shuffle()
                yield self.generator.display()
            else:
                self.reset(problemGenerator, n)
        
        #   TODO: Is it good practice to chain exceptions like this?
            
        except ValueError:
            raise StopIteration("No problems left in Drill object.") 

    
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