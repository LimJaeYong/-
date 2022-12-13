D = {"사과 주스": 1000, "콜라": 2000, "커피": 1000, "사이다": 2000}


def calc_change(data):
    return data // 1000 if data >= 1000 else print("error")


while True:
    money = int(input("돈 투입 >>"))

    if money % 1000 != 0:
        print("재입력")
    else:
        break

while True:
    print(D)
    D_sel = input("음료 선텍 >> ")
    if D_sel not in D:
        print("다시 선택")
    else:
        D_price = D[D_sel]
        print(D_price)
        if D_price > money:
            print("돈 부족")
        else:
            break

change = money - D_price
a = calc_change(change)

print(f"거스름 : 1000원짜리 {a}장 {change}원")
