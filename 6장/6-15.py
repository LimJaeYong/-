class Car:
    def __init__(self, name):
        self.name = name
        self.velocity = 50
        self.gear = 1

    def accel(self):
        self.velocity += self.gear
        return self.velocity

    def carBreak(self):
        self.velocity -= 20
        if self.velocity < 0:
            self.velocity = 0
        return self.velocity

    def gearChange(self):
        self.gear += 1
        if self.gear > 6:
            self.gear = 1
        return self.gear

    def info(self):
        print(
            f"차 이름은 {self.name}이고 속도는 {self.velocity}이며, 현재 기어는 {self.gear}입니다.")


a = Car(input("차 이름 입력 >> "))

while True:
    n = input("옵션 선택 (가속 / 브레이크 / 기어) >> ")
    if n == "가속":
        a.accel()
    elif n == "브레이크":
        a.carBreak()
    elif n == "기어":
        a.gearChange()
    else:
        break

print(a.info())
