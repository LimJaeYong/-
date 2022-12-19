from random import randint, choice


class Character:
    def __init__(self):
        self.life = 100
        self.low = 1
        self.max = 10
        self.strength = randint(self.low, self.max)

    def attacked(self, other):
        self.life -= other.strength
        if self.life <= 0:
            self.life = 0

    def attack(self, other):
        if other.isAlive() and self.isAlive():
            other.attacked(self)
            print(f"{self} attack {other}")

    def isAlive(self):
        return self.life > 0


class warrior(Character):
    def __init__(self):
        super().__init__()
        self.low = 30
        self.max = 50
        self.strength = randint(self.low, self.max)

    def __str__(self):
        return "전 사"


class wizard(Character):
    def __init__(self):
        super().__init__()
        self.life = 80
        self.low = 10
        self.max = 50
        self.strength = randint(self.low, self.max)

    def __str__(self):
        return "마법사"


class bowman(Character):
    def __init__(self):
        super().__init__()
        self.life = 90
        self.low = 10
        self.max = 100
        self.strength = randint(self.low, self.max)

    def __str__(self):
        return "궁 수"


t1_b = warrior()
t1_c = wizard()
t1_d = bowman()

t2_b = warrior()
t2_c = wizard()
t2_d = bowman()

t1 = [t1_b, t1_c, t1_d]
t2 = [t2_b, t2_c, t2_d]
inGame_team = [t1, t2]
turn = 0


def t1_aliveChecker(): return any(t1_aliveList)


def t2_aliveChecker(): return any(t2_aliveList)


def team_status(team):
    name = "t1" if team == t1 else "t2"
    print(f"\n<<{name}>>")
    for i in team:
        print(f"{name}'s {i} life : {i.life}")


while True:
    print("-"*20)
    print(f"\n\n<<Turn {turn+1}>>")
    t1_aliveList = []
    t2_aliveList = []

    for i in t1:
        print(f"{i} Alive: {i.isAlive()} | Life: {i.life} | Strength: {i.strength}")
        t1_aliveList.append(i.isAlive())

    print()
    for i in t2:
        print(f"{i} Alive: {i.isAlive()} | Life: {i.life} | Strength: {i.strength}")
        t2_aliveList.append(i.isAlive())

    if t1_aliveChecker() is True and t2_aliveChecker() is True:
        for i in inGame_team:
            team_status(i)
            for j in i:
                j.attack(choice(inGame_team[(inGame_team.index(i) + 1) % 2]))

    else:
        if t1_aliveChecker() is True:
            print("t1 승리")
        elif t2_aliveChecker() is True:
            print("t2 승리")
        else:
            print("비김")
        break

    turn += 1
