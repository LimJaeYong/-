class person:
    def __init__(self, name, id, age, height, weight) -> None:
        self.name = name
        self.id = id
        self.age = age
        self.height = height
        self.weight = weight
    
    def __str__(self) -> str:
        return f"이름: {self.name}, 나이: {self.age}, 키: {self.height}, 몸무게: {self.weight}"

        
def main():
    personList = [person("a", "1", 20, 60, 170), person("b", "2", 21, 65, 170), person("c", "3", 25, 70, 180), person("d", "4", 30, 80, 190)]
    
    for i in range(len(personList)):
        print(personList[i])

        
if __name__ == "__main__":
    main()

