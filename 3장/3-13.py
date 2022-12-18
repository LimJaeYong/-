class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        self.items.pop()
    
    def view(self):
        print("스택 출력 >> ", end = "")
        for i in range(len(self.items)):
            print(self.items[i], " ", end = "")
        
    def size(self):
        print("스택 사이즈 : ", len(self.items))
    
    def empty(self):
        if len(self.itmes) == 0:
            print("Empty")
        else:
            print("Not empty")
    
stk = Stack()

print("스택 생성")

while True:
    n = int(input("1. push 2. pop 3. view 4. size 5. empty 0. quit"))
    
    if n == 1:
        stk.push(input("삽입할 데이터 입력 >> "))
    elif n == 2:
        stk.pop()
        print("삭제")
    elif n == 3:
        stk.view()
    elif n == 4:
        stk.empty()
    else:
        break