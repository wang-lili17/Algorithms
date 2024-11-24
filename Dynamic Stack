class Stack:
    def __init__(self):
        self.arr = [] 
        

    def isEmpty(self):
        return len(self.arr) == 0


    def push(self,a):
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


stack1 = Stack()  
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
