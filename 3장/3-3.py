score = int(input("점수 입력 >> "))

if score >= 90: # elif 활용
    print('A', end = ' ')
elif score >= 80:
    print('B', end = ' ')
elif score >= 70:
    print('C', end = ' ')
elif score >= 60:
    print('D', end = ' ')
else:
    print("F")

print("학점 입니다.")