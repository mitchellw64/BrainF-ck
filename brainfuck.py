# ASCII printable characters = 32-126
# ord() converts ASCII to English
# chr() converts English to ASCII

class brainfuck:

    def __init__(self, input=None):
        if input is None:                # don't initialize immutables
            self.input = []
        else:
            self.input = list(input)

        self.str_output = ""
        self.list_output = []
        self.L = [0 for i in range(10)]  # if using lists, keep max memory slots at 10 for now                # bug?
        self.index = 0                   # which memory slot you're in
        
        self.open = 0                    # used in [] loops
        self.closed = 0                  # used in [] loops
        self.recursion_counter = 0       # used to break stack overflow
        self.initial_index = 0           # memory slot that must be at 0 for [] loop to end

    def __repr__(self):
        """use print to show brainfuck code"""
        return "".join(self.input)
        
    def memory_slots(self):
        """see the memory strip"""
        return self.L

    def clear(self):
        """clears code without initializing new instance of the class"""
        self.input = []
        self.str_output = ""
        self.list_output = []
        self.L = [0 for i in range(10)]  
        self.index = 0 
        self.open = 0
        self.closed = 0
        self.recursion_counter = 0
        self.initial_point = 0
        return
    
    def put(self, new_input):
        """adds brainfuck code to input"""
        put_L = list(new_input)
        for i in range(len(put_L)):
            self.input.append(put_L[i])

    def remove(self, x):
        """removes x number of symbols from the brainfuck code"""
        if x >= len(self.input): # debugs "pop from empty list"
            self.input = []
            return

        for i in range(x):
            self.input.pop()
        return

    def display_results(self):
        """Returns ASCII output of brainfuck code"""
        for num in range(len(self.list_output)): # converts each number to english
            self.list_output[num] = chr(int(self.list_output[num]))
        self.str_output = "".join(self.list_output) # form string of english
        return self.str_output
          
    def plus(self):
        """increments memory slot by one"""
        if self.L[self.index] != 255:       # can't go above 255
            self.L[self.index] += 1
        return

    def minus(self):
        """decrements memory slot by one"""
        if self.L[self.index] != 0:         # can't go below 0
            self.L[self.index] -= 1
        return 

    def right_carrot(self):
        """shifts current memory slot pointer forwards one"""
        # use modulo to keep inside the memory slots when doing more than 10 >'s at a time
        if self.index == 9:
            self.index = 0
        else:
            self.index +=1

    def left_carrot(self):
        """shifts current memory slot pointer back one"""
        # use modulo to keep inside the memory slots when doing more than 10 <'s at a time
        if self.index == 0:
            self.index = 9
        else:
            self.index -= 1

    def period(self): # doesn't this output one thing?
        """add output of current memory slot to self.output"""
        self.list_output.append(self.L[self.index]) # makes a list of ascii numbers to be outputted
        return

    def interpret_code(self, loop=None):
        """does the brainfucking, default parameter is all code"""

        if loop is None:
            loop = self.input
            self.L = [0 for i in range(10)]
            self.index = 0

        self.str_output = ""  # re-initializes these guys so that outputs are resetted in between interprets
        self.list_output = [] # aka don't wanna keep code that you've already outputted; just the code you have now
        
        for i in range(len(loop)):

            if loop[i] == '+':
                self.plus()
            elif loop[i] == '-':
                self.minus()
            elif loop[i] == '>':
                self.right_carrot()
            elif loop[i] == '<':
                self.left_carrot()

            # fix: ] indicates recursion, but need to cancel stuff inside [] before seeing ] and recursing

            elif loop[i] == '[':

                self.initial_point = self.index # the memory slot that has to go to 0

                self.open += 1
                open_flag = i
                if self.open - self.closed >= 2:
                    raise KeyError("nested for loops coming soon!")

            elif loop[i] == ']':

                self.closed += 1
                closed_flag = i

                if self.closed < self.open:
                    raise KeyError("bracket typo!")

                elif self.closed == self.open:
                    inner_loop = loop[open_flag+1:closed_flag] # splices list from bracket to bracket, not including the brackets!
                    while self.L[self.initial_index] != 0:                  # does the while loop
                        self.recursion_counter += 1
                        if self.recursion_counter == 100:
                            raise RecursionError("Self defined (100) recursion limit exceeded")
                        self.interpret_code(inner_loop)

            elif loop[i] == '.':
                self.period()
            else:
                raise KeyError(f"The character {loop[i]} is not brainfuck!")

        if self.open != self.closed: # if more open than closed at end of code (after for loop)
            raise KeyError("loop not defined!")