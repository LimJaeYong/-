class square:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class triangle(square):
    def area(self):
        super().area()
        return self.width * self.height / 2
    
class comparison:
    def __init__(self, s, t):
        self.square = s
        self.triangle = t
        
    def compare(self):
        if self.square > self.triangle:
            print("사각형이 삼각형보다 큼")
        elif self.square < self.triangle:
            print("삼각형이 사각형보다 큼")
        else:
            print("둘의 크기는 같음")

width = int(input("길이 입력 >> "))
height = int(input("높이 입력 >> "))

width2 = int(input("길이 입력 >> "))
height2 = int(input("높이 입력 >> "))
        
obj1 = square(width, height)
square = obj1.area()
print(square)

obj2 = triangle(width2, height2)
triangle = obj2.area()
print(triangle)

obj3 = comparison(square, triangle)
compare = obj3.compare()
print(compare)
        
    