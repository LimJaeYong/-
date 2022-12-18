import time


class Hamster:
    def __init__(self, hp) -> None:
        self.hp = hp

    def view(self):
        print(f"현재 체력: {self.hp}")

    def eat(self):
        self.hp += 1
        print("밥 먹는 중")
        for i in range(3):
            time.sleep(0.3)
            print("."*(i+1))
        self.view()

    def play(self):
        self.hp -= 1
        print("쳇바퀴 타는 중")
        for i in range(3):
            time.sleep(0.3)
            print("."*(i+1))
        self.view()


ham = Hamster(5)
print("햄스터 키우기")

while True:
    n = int(input("1. 시작 2. 종료"))
    if n == 1:
        while True:
            n1 = int(input("1. 밥 주기 2. 놀기 >> "))
            if ham.hp > 0:
                if n1 == 1:
                    ham.eat()
                elif n1 == 2:
                    ham.play()
                else:
                    continue
            else:
                break
    else:
        break            