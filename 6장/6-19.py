class Calculator:
    def __init__(self, first, second) -> None:
        self.first, second = first, second
    
    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second
    
    def mul(self):
        return self.first * self.second
    
    def div(self):
        return self.first / self.second

a, b = map(float, input("두 수 입력 >> ".split()))
num  = Calculator(a, b)
n = input("계산 방식 선택 >> ")

if n == 1:
    print(num.add())
elif n == 2:
    print(num.sub())
elif n == 3:
    print(num.mul())
elif n == 4:
    print(num.div())
else:
    quit()
