def ave(scores):
    n = 0
    if scores[0] != len(scores[1:]):
        print("평균을 구할 수 없음")

    else:
        avg = sum(scores[1:])/scores[0]
        n = 0
        for j in scores[1:]:
            if j > avg:
                n += 1
    per = (n/scores[0])*100
    print(f"교실의 평균 점수{avg:.3f}보다 높은 학생의 비율 : {per:.3f}\n")


C = int(input("교실의 수 >> "))
for i in range(C):
    scores = list(map(int, input("인원수, 인원들의 평균 입력 >> ").split()))
    ave(scores)
