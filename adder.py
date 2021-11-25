from gates import *


# 2 inputs Half Adder with Carry
class HalfAdder():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.carry = 0
        self.out = 0

    def __str__(self):
        return "2 inputs Half Adder with Carry"

    def setInA(self, inputA):
        self.inA = inputA
    
    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB

    def performSum(self):
        And1 = AND()
        Xor1 = XOR()

        And1.setInputs(self.inA, self.inB)
        Xor1.setInputs(self.inA, self.inB)

        self.out = Xor1.Output()
        self.carry = And1.Output()

    def getSum(self):
        return self.out

    def getCarry(self):
        return self.carry


# 3 inputs Full Adder with Carry
class FullAdder():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.inC = 0
        self.carry = 0
        self.out = 0
    
    def __str__(self):
        return "3 inputs Full Adder with Carry"

    def setInA(self, inputA):
        self.inA = inputA

    def setInB(self, inputB):
        self.inB = inputB

    def setInC(self, inputC):
        self.inC = inputC

    def setInputs(self, inputA, inputB, inputC):
        self.inA = inputA
        self.inB = inputB
        self.inC = inputC

    def performSum(self):
        And1 = AND()
        And2 = AND()
        And3 = AND()
        Xor1 = XOR()
        Xor2 = XOR()
        Or1 = OR()
        Or2 = OR()

        And1.setInputs(self.inA, self.inB)
        And2.setInputs(self.inA, self.inC)
        And3.setInputs(self.inB, self.inC)
        Xor1.setInputs(self.inA, self.inB)
        Xor2.setInputs(Xor1.Output(), self.inC) 
        Or1.setInputs(And1.Output(), And2.Output()) 
        Or2.setInputs(Or1.Output(), And3.Output()) 

        self.out = Xor2.Output()
        self.carry = Or2.Output()

    def getSum(self):
        return self.out

    def getCarry(self):
        return self.carry


# Nibble Adder - sum 4 Bits
class NibbleAdder():
    def __init__(self):
        self.A0 = 0
        self.A1 = 0
        self.A2 = 0
        self.A3 = 0
        self.B0 = 0
        self.B1 = 0
        self.B2 = 0
        self.B3 = 0
        self.O0 = 0
        self.O1 = 0
        self.O2 = 0
        self.O3 = 0
        self.carry = 0
        self.out = []
    
    def __str__(self):
        return "4 bit Adder with Carry"
    
    def setInputCarry(self, Carry):
        self.carry = Carry

    def setInputsA(self, D3, D2, D1, D0):
        self.A0 = D0
        self.A1 = D1
        self.A2 = D2
        self.A3 = D3
    
    def setInputsB(self, D3, D2, D1, D0):
        self.B0 = D0
        self.B1 = D1
        self.B2 = D2
        self.B3 = D3

    def performSum(self):
        fa1 = FullAdder()
        fa2 = FullAdder()
        fa3 = FullAdder()
        fa4 = FullAdder()

        fa1.setInputs(self.carry, self.A0, self.B0)
        fa1.performSum()
        fa2.setInputs(fa1.getCarry(), self.A1, self.B1)
        fa2.performSum()
        fa3.setInputs(fa2.getCarry(), self.A2, self.B2)
        fa3.performSum()
        fa4.setInputs(fa3.getCarry(), self.A3, self.B3)
        fa4.performSum()

        self.O0 = fa1.getSum()
        self.O1 = fa2.getSum()
        self.O2 = fa3.getSum()
        self.O3 = fa4.getSum()
        self.carry = fa4.getCarry()
        self.out = [self.O3, self.O2, self.O1, self.O0]

    def getSum(self):
        return self.out

    def getCarry(self):
        return self.carry


# Byte Adder - sum 8 bits
class ByteAdder():
    def __init__(self):
        self.A0 = 0
        self.A1 = 0
        self.A2 = 0
        self.A3 = 0
        self.A4 = 0
        self.A5 = 0
        self.A6 = 0
        self.A7 = 0
        self.B0 = 0
        self.B1 = 0
        self.B2 = 0
        self.B3 = 0
        self.B4 = 0
        self.B5 = 0
        self.B6 = 0
        self.B7 = 0
        self.O0 = 0
        self.O1 = 0
        self.O2 = 0
        self.O3 = 0
        self.O4 = 0
        self.O5 = 0
        self.O6 = 0
        self.O7 = 0
        self.carry = 0
        self.out = []
        self.lsb = []
        self.msb = []
    
    def __str__(self):
        return "8 bit Adder with Carry"

    def setInputsA(self, D7, D6, D5, D4, D3, D2, D1, D0):
        self.A0 = D0
        self.A1 = D1
        self.A2 = D2
        self.A3 = D3
        self.A4 = D4
        self.A5 = D5
        self.A6 = D6
        self.A7 = D7

    def setInputsB(self, D7, D6, D5, D4, D3, D2, D1, D0):
        self.B0 = D0
        self.B1 = D1
        self.B2 = D2
        self.B3 = D3
        self.B4 = D4
        self.B5 = D5
        self.B6 = D6
        self.B7 = D7

    def performSum(self):
        na1 = NibbleAdder() #LSB
        na2 = NibbleAdder() #MSB

        #Less Signifcant bits (Left Nibble)
        na1.setInputCarry(0)
        na1.setInputsA(self.A3, self.A2, self.A1, self.A0)
        na1.setInputsB(self.B3, self.B2, self.B1, self.B0)
        na1.performSum()
        
        #Most significant Bits (Right Nibble)
        na2.setInputCarry(na1.getCarry())
        na2.setInputsA(self.A7, self.A6, self.A5, self.A4)
        na2.setInputsB(self.B7, self.B6, self.B5, self.B4)
        na2.performSum()

        lsb = na1.getSum()
        msb = na2.getSum()

        self.carry = na2.getCarry()
        self.out = [msb[0], msb[1], msb[2], msb[3], lsb[0], lsb[1], lsb[2], lsb[3]]

    def getCarry(self):
        return self.carry

    def getSum(self):
        return self.out


"""
Example Usage:
ba = FullAdder()
ba.setInputsA(0,0,0,1,1,0,1,0)
ba.setInputsB(0,0,0,0,1,1,1,0)
ba.performSum()
print(ba.getSum())
"""
