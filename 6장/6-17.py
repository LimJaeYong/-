class BMI:
    def __init__(self, name, height, weight, bmi) -> None:
        self.name, self.height, self.weight, self.bmi = name, height, weight, bmi

    def info(self):
        print(f"{self.name}의 bmi 지수 : {self.bmi}")


person = []


def enter():
    name = input("이름 >> ")
    height = float(input("키 입력 (미터 단위) >> "))
    weight = float(input("몸무게 입력 (kg 단위) >> "))
    bmi = round((weight/(height * 0.01)**2), 2)
    person.append(BMI(name, height, weight, bmi))


while True:
    n = int(input("1. 이름, 신체정보\n2. BMI 리스트\n3. 목록 초기화\n4. 종료 \n>> "))
    if n == 1:
        enter()
    elif n == 2:
        if not person:
            print("이름과 신체정보 입력")
            continue
        for i in person:
            i.info()
    elif n == 3:
        if not person:
            print("초기화 할 목록 없음")   
            continue
        person.claer()
        print("목록 초기화 완료")
    else:
        print("종료")
        quit()