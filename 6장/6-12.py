class Human:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        
class Student(Human):
    def __init__(self, name, age, number) -> None:
        super().__init__(name, age)
        self.number = number
    
    def __add__(self, new):
        return self.age + new.age

    def __gt__(self, new):
        return self.age > new.age
    
    def __eq__(self, new):
        return self.age == new.age
    
    def info(self):
        print(f"이름: {self.name}\n나이: {self.age}\n학번: {self.number}")

a = Student("임재용", 24, 18)
b = Student("홍길동", 24, 19)
c = Student("적길동", 21, 21)

a.info()
b.info()
c.info()

print(a+b)
print(a == b, a<c, b>c)