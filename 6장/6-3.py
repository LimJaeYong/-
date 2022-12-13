import math


class Circle:
    def __init__(self, radius, cx, cy):
        self.radius = radius
        self.cx = cx
        self.cy = cy

    def area(self):
        return self.radius * self.radius * math.pi

    def center(self):
        return self.cx, self.cy
    
def main():
    print("정보 입력")
    rad = int(input("반지름 >> "))
    cx = int(input("x >> "))
    cy = int(input("y >> "))
    circle = Circle(rad, cx, cy)

    print(f"월의 넓이: {circle.area()}")
    print(f"중심 좌표: {circle.center()}")
    
if __name__ == "__main__":
    main()

