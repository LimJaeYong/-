class Character:
    def __init__(self):
        self.life = 100
        self.strength = 10
        self.intellgence = 10
        self.stamina = 8
    
    def attacked(self):
        self.life -= 10
        print(f"공격 받았습니다. {self.life}")
    
    def attack(self):
        print("공격!!")
        
    def defend(self):
        print("방어")

    
class warrior(Character):
    def __init__(self):
        super(warrior, self).__init__()
        self.strength = 15
        self.intellgence = 15
        self.stamina = 2
        
    def attack(self):
        print("검 공격!!")
            
class wizard(Character):
    def __init__(self):
        super(wizard, self).__init__()
        self.strength = 5
        self.intellgence = 15
        self.stamina = 2
        
    def attack(self):
        print("마법 공격!!")
        
class bowman(Character):
    def __init__(self):
        super(bowman, self).__init__()
        self.strength = 4
        self.intellgence = 3
        self.stamina = 8
        
    def attack(self):
        print("바람 공격!!")

a = Character()
b = warrior()
c = wizard()
d = bowman()

t1 = [a, b, c, d]
t2 = [a, b, c, d]

for i in t1:
    i.attack()


# while True:
#     print("1. 공격 2. HP 확인 3. 방어 4. 종료 5. 팀 생성")
#     num = int(input("행동 입력 >> "))
    
#     if num == 1:
#         b.attack()
#         c.attack()
#         d.attack()
#     elif num == 2:
#         b.attacked()
#         c.attacked()
#         d.attacked()
#     elif num == 3:
#         b.defend()
#         c.defend()
#         d.defend()
#     elif num == 5:
#         t1 = input("팀을 구성할 객체 입력 >> ").split()
#         for i in range(len(t1)):
#             t1[i].attack()
#     else: 
#         break