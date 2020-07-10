class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.operations = list()
        self.curOpIdx = -1

    def add(self, num: int):
        op = Add(num)
        if(self.curOpIdx == len(self.operations) - 1):
            self.curOpIdx += 1
        self.operations.append(op)
        self.value = op.perform_do(self.value)

    def subtract(self, num: int):
        op = Subtract(num)
        if(self.curOpIdx == len(self.operations) - 1):
            self.curOpIdx += 1
        self.operations.append(op)
        self.value = op.perform_do(self.value)

    def undo(self):
        if(self.curOpIdx >= 0):
            self.value = self.operations[self.curOpIdx].perform_undo(self.value)
            self.curOpIdx -= 1

    def redo(self):
        if(self.curOpIdx < len(self.operations) - 1):
            self.value = self.operations[self.curOpIdx].perform_do(self.value)
            self.curOpIdx += 1


    def bulk_undo(self, steps: int):
        for i in range(steps):
            self.undo()

    def bulk_redo(self, steps: int):
        for i in range(steps):
            self.redo()

class Operator():
    def __init__(self, num: int):
        self.value = num

    def perform_do(self, val: int):
        pass
    def perform_undo(self, val: int):
        pass

class Add(Operator):
    def __init__(self, num):
        super().__init__(num)
    def perform_do(self, val: int):
        return self.value + val
    def perform_undo(self, val: int):
        return -self.value + val

class Subtract(Operator):
    def __init__(self, num):
        super().__init__(num)
    def perform_do(self, val):
        return -self.value + val
    def perform_undo(self, val):
        return self.value + val
