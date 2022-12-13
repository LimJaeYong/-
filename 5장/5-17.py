class line:
    length = 0
    
    def __init__(self, length):
        self.length = length
        print(f"{self.length} 길이의 선 생성")
    
    def __del__(self):
        print(self.length, "길이의 선 삭제")

    def __add__(self, other):
        return self.length + other.length
    
    def __lt__(self, other):
        return self.length < other.length
    
    def __eq__(self, other):
        return self.length == other.length


line1 = line(5)
line2 = line(10)

print("두 선의 합 : ", line1 + line2)

if line1 < line2:
    print("선2가 더 깁니다.")
    del(line1)

elif line1 == line2:
    print("두 선의 길이가 같습니다.")

else:
    print("선1이 더 깁니다.")
    del(line2)