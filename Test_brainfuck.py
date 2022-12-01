from brainfuck import brainfuck
import unittest

class bftest(unittest.TestCase):

    def testhelloworld(self):
        hello_world = brainfuck(f"++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.<<+.")
        hello_world.interpret_code()
        self.assertEqual(hello_world.display_results(), "Hello World!")

    def testinit_put_clear_remove(self):
        bf = brainfuck("-")
        self.assertEqual(bf.input, ["-"])
        bf.put("+++")
        self.assertEqual(bf.input, ["-", "+", "+", "+"])
        bf.remove(2)
        self.assertEqual(bf.input, ["-", "+"])
        bf.clear()
        self.assertEqual(bf.input, [])

    def testmemory(self):
        bf = brainfuck("+++>+++-")
        bf.interpret_code()
        self.assertEqual(bf.memory_slots(), [3, 2, 0, 0, 0, 0, 0, 0, 0, 0])
        

    def testdisplay(self):
        bf = brainfuck()
        self.assertEqual(bf.display_results(), "")
        bf2 = brainfuck("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++..")
        bf2.interpret_code()
        self.assertEqual(bf2.display_results(), "GG")

    # done?? I tested it in display
    def testperiod(self):
        pass

    def testplus(self):
        bf = brainfuck("+")
        bf.interpret_code()
        self.assertEqual(bf.L[bf.index], 1)

        bf2 = brainfuck("+++++")
        bf2.interpret_code()
        self.assertEqual(bf2.L[bf2.index], 5)

        bf3 = brainfuck()
        for i in range(300):
            bf3.put("+")
        bf3.interpret_code()
        self.assertEqual(bf3.L[bf3.index], 255)

        # omg i'm cracked at this

    def testminus(self):
        bf = brainfuck("---")
        bf.interpret_code()
        self.assertEqual(bf.L[bf.index], 0)

        bf2 = brainfuck("+++.---")
        bf2.interpret_code()
        self.assertEqual(bf2.L[bf2.index], 0)

    def testcarrots(self):
        bf = brainfuck()
        for i in range(20):
            bf.put("+")
        bf.put(">")
        for i in range(50):
            bf.put("+")
        bf.interpret_code()
        self.assertEqual(bf.L[0], 20)
        self.assertEqual(bf.L[1], 50)
        for i in range(3):
            bf.put("<+")
        bf.interpret_code()
        self.assertEqual(bf.index, 8)
        self.assertEqual(bf.L[bf.index], 1)
    
        bf2 = brainfuck("++++++++++++++++++++++++++++++++++++++++++.>+++++++++++++++++++++++++++++++++++++++++++++.")
        bf2.interpret_code()
        self.assertEqual(bf2.display_results(), "*-")

unittest.main()