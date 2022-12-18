import random

# 너무 많아서 일단 4개
# 근데 왜 딕셔너리 안쓰고 굳이?
word = [['delivery date', '납품일'], ['on sale', '할인 중인'], ['cut price', '할인 가격'], ['rock-bottom price','최저 가격']]

n = int(input('문제 갯수 : '))
print(len(word))
m = random.sample(range(len(word)), n)  # word의 단어들 중 입력한 단어 개수 만큼 랜덤 선택
count = 0

for i in m:
    sample = random.sample(m, 4)  # 랜덤 4개 문제 집어넣기
    if i in sample:
        k = sample.index(i)  # 보기에 답이 있으면 답 위치를 k에 넣음
    else:
        k = random.randint(0, 3)
        sample[k] = i
    print(word[i][0])

    for i in range(4):
        # 4개 선택지 출력시 1~4번 각 뜻 한 줄씩 출력
        print('%d.' %(i+1)+word[sample[i]][1], end=' ')
    print()

    answer = int(input('답 : '))

    if answer - 1 == k:
        print("정답")
        count += 1
    else:
        print("틀림, 정답은 ", k+1)
    print()
    
print()
print('정답 수 : %d '%count)

