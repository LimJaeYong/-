def Grade(t):
    grade = {
        'A+': 4.5,
        'A0': 4.0,
        'B+': 3.5,
        'B0': 3.0,
        'C+': 2.5,
        'C0': 2.0,
        'F': 0,
    }

    for i in range(t):
        total_c = 0
        total_g = 0
        n = int(input("과목 수: "))
        print("학점 별 성적 : ", grade)

        for i in range(n):
            c, g = map(float, input("학점 수 평점 입력 >>").split())

            total_c += c
            total_g += c*g
            
        ave_g = total_g/total_c
        print(f"{int(total_c)}학기에 들은 학점 : {ave_g} \n 나의 평점 : {i+1}")

t = int(input("학기 수 : "))
Grade(t)
