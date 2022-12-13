from math import pi


def squareArea(s):
    print("정사각형")
    area = s * s
    print(area)
    return area


def trianlge(b, s):
    print("삼각형")
    area = b * s / 2
    print(area)
    return area


def cirCle(r):
    print("원 둘레")
    area = 2 * r * pi
    print(area)
    return area


def Circle(r):
    print("원 넓이")
    area = r * r * pi
    print(area)
    return area


print("도형 계산기")

while True:
    n = int(input("1. 정사각형 2. 삼각형 3. 원 둘레 4. 원 넓이 5. 종료"))

    if n == 1:
        a1 = int(input("변 길이 입력 >> "))
        squareArea(a1)
    elif n == 2:
        a1 = int(input("밑변 입력 >> "))
        a2 = int(input("높이 입력 >> "))
        trianlge(a1, a2)
    elif n == 3:
        a1 = int(input("반지름 입력 >> "))
        cirCle(a1)
    elif n == 4:
        a1 = int(input("반지름 입력 >> "))
        Circle(a1)
    else:
        break

        