

# Not Gate
class NOT():
    def __init__(self):
        self.inA = 0
        self.out = 1
    
    def __str__(self):
        return f"NOT Gate"

    def setInput(self, input):
        self.inA = input
    
    def Output(self):
        if self.inA >= 1:
            return 0
        else:
            return 1


# 2 inputs OR Gate
class OR():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.out = 0
    
    def __str__(self):
        return f"2 inputs OR Gate"

    def setInA(self, inputA):
        self.inA = inputA
    
    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB

    def Output(self):
        if self.inA == 1 or self.inB == 1:
            return 1
        else:
            return 0


# 2 inputs AND Gate
class AND():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.out = 0
    
    def __str__(self):
        return f"2 inputs AND Gate"

    def setInA(self, inputA):
        self.inA = inputA

    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB
    
    def Output(self):
        if self.inA == 1 and self.inB == 1:
            return 1
        else:
            return 0


# 2 inputs NOR Gate
class NOR():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.out = 0
    
    def __str__(self):
        return f"2 inputs NOR Gate"

    def srtInA(self, inputA):
        self.inA = inputA

    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB
    
    def Output(self):
        orGate = OR()
        notGate = NOT()
        
        orGate.setInputs(self.inA, self.inB)
        notGate.setInput(orGate.Output())

        return notGate.Output()


# 2 inputs NAND Gate
class NAND():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.out = 0
    
    def __str__(self):
        return f"2 inputs NAND Gate"

    def setInA(self, inputA):
        self.inA = inputA
    
    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB
    
    def Output(self):
        andGate = AND()
        notGate = NOT()

        andGate.setInputs(self.inA, self.inB)
        notGate.setInput(andGate.Output())

        return notGate.Output()


# 2 inputs XOR Gate
class XOR():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.out = 0
    
    def __str__(self):
        return f"2 inputs XOR Gate"

    def setInA(self, inputA):
        self.inA = inputA

    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB
    
    def Output(self):
        notGate1 = NOT()
        notGate2 = NOT()
        andGate1 = AND()
        andGate2 = AND()
        orGate = OR()

        notGate1.setInput(self.inB)
        notGate2.setInput(self.inA)
        andGate1.setInputs(self.inA, notGate1.Output())
        andGate2.setInputs(notGate2.Output(), self.inB)
        orGate.setInputs(andGate1.Output(), andGate2.Output())

        return orGate.Output()


# 2 inputs XNOR Gate
class XNOR():
    def __init__(self):
        self.inA = 0
        self.inB = 0
        self.out = 0
    
    def __str__(self):
        return f"2 inputs XNOR Gate"

    def setInA(self, inputA):
        self.inA = inputA

    def setInB(self, inputB):
        self.inB = inputB

    def setInputs(self, inputA, inputB):
        self.inA = inputA
        self.inB = inputB
    
    def Output(self):
        notGate1 = NOT()
        notGate2 = NOT()
        notGate3 = NOT()
        andGate1 = AND()
        andGate2 = AND()
        orGate = OR()
        
        notGate1.setInput(self.inB)
        notGate2.setInput(self.inA)
        andGate1.setInputs(self.inA, notGate1.Output())
        andGate2.setInputs(notGate2.Output(), self.inB)
        orGate.setInputs(andGate1.Output(), andGate2.Output())
        notGate3.setInput(orGate.Output())

        return notGate3.Output()

"""
Usage: 
1)
# Get output
gate1 = OR()
gate1.setIputs(1,0)
print(gate1.Output())

2)
# show truth table
gate1 = OR()
listA = [0,0,1,1]
listB = [0,1,0,1]
print("A B | Q")
print("----|--")
for i in range(0, 3):
    gate1.setInputs(listA[i], listB[i])
    print(f"{listA[i]} {listB[i]} | {gate1.Output()}")

"""

