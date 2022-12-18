class gameCharacter:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def get_attacked(self, damage):
        if self.is_alive():
            if self.hp >= damage:
                self.hp -= damage
            else:
                self.hp = 0
                print(f"{self.name} 사망")
        else:
            print(f"{self.name} 사망")

    def attack(self, other_character):
        if self.is_alive():
            other_character.get_attacked(self.power)

    def __str__(self):
        return f"{self.name}님의 hp는 {self.hp}만큼 남았습니다."


def main():
    character1 = gameCharacter(input("캐릭터1 이름 >> "), int(
        input("체력 >> ")), int(input('공격력 >> ')))
    character2 = gameCharacter(input("캐릭터2 이름 >> "), int(
        input("체력 >> ")), int(input('공격력 >> ')))

    n = int(input("1. 1번이 공격, 2. 2번이 공격 >> "))

    while character2.is_alive() and character1.is_alive():
        if n == 1:
            if character2.is_alive():
                character1.attack(character2)
                print(character2)
                if character1.is_alive():
                    character2.attack(character1)
                    print(character1)
        elif n == 2:
            if character1.is_alive():
                character2.attack(character1)
                print(character1)
                if character2.is_alive():
                    character1.attack(character2)
                    print(character2)


if __name__ == '__main__':
    main()
