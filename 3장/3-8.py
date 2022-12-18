p = int(input("숫자 입력 >> "))

number = range(1, 101)

while p not in number:
    print("다시 입력")
    p = int(input("숫자 입력 >>"))

while True:
    c = number[(len(number)//2) - 1]
    print("컴퓨터: ", c)

    if p == c:
        print("성공")
        break

    answer = input("up or down?: ")

    if p > c and answer == "up":
        number = number[number.index(c)+1:]
    elif p < c and answer == "down":
        number = number[:number.index(c)]
    else:
        print("out of range")
