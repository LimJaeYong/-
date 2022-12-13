def grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

        
def inputdata():
    a = int(input('점수 입력 : '))
    return a

while True:
    j = inputdata()
    
    if j == 0:
        break
    
    print(f"Your grade is {grade(j)}.")
