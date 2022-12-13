def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


def run():
    while True:
        print("1. 덧셈 2. 뺄셈 3. 나눗셈 4. 곱셈 5. 종료")
        menu = int(input("메뉴 선텍 >> "))

        if menu == 1:
            a, b = map(int, input("두 정수 입력 >> ").split())
            print(f"{a} + {b} = {add(a,b)}")

        elif menu == 2:
            a, b = map(int, input("두 정수 입력 >> ").split())
            print(f"{a} + {b} = {sub(a,b)}")
        elif menu == 3:
            a, b = map(int, input("두 정수 입력 >> ").split())
            if b == 0:
                print("error")
            else:
                print(f"{a} + {b} = {div(a,b)}")
        elif menu == 4:
            a, b = map(int, input("두 정수 입력 >> ").split())
            print(f"{a} + {b} = {mul(a,b)}")

        elif menu == 5:
            break


run()
