class Stack:
    def __init__(self, max_n):
        self.arr = []  # Stack elements
        self.max_n = max_n  # Maximum capacity

    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return len(self.arr) == self.max_n

    def push(self,a):
       
        if self.isFull():
            return "Stack is full"
        else:
            '''a = int(input("Input the value to push: "))'''
            self.arr.append(a)
       

    def pop(self):
        
        if self.isEmpty():
            return "Stack is empty"
        return self.arr.pop()

    def top(self):
        
        if self.isEmpty():
            return "Stack is empty"
        return self.arr[-1]

    def printStack(self):
        print(self.arr)


stack1 = Stack(5)  
stack1.push(1) 
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.printStack()  
print(stack1.top())  
stack1.pop()  
stack1.printStack()  
