class coffee:
    def __init__(self):
        self.p = {'우유': 300, '믹스커피': 500, '카페라떼': 500}
        self.n = {1: '우유', 2: '믹스커피', 3: "카페라떼"}
        self.money = 0

    def menu(self):
        print("메뉴판")
        for k, v in self.p.items():
            print(k, v, "원")
        print()

    def coin(self):
        while True:
            try:
                self.money += int(input("돈 투입 >> "))
            except Exception as e:
                print(e)
                continue
            else:
                print("금액: ", self.money)
                print()
                break

    def buy(self):
        try:
            n = int(input("메뉴 선택: "))
        except Exception as e:
            print(e)
        else:
            if n == 0:
                return 0
            if n >= 1 and n <= 4:
                if self.money >= self.p[self.n[n]]:
                    print(self.n[n], "구입 완료")
                    self.money = self.money - self.p[self.n[n]]
                    print("잔액", self.money)
                else:
                    print("잔액 부족")
                    self.coin()
            else:
                print("잘못된 번호")
        return 1


a = coffee()
a.menu()
a.coin()
 
while a.buy():
    print()

print("판매 종료")
print("잔돈: ", a.money)