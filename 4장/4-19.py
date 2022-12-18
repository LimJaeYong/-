def f(n):
    result = []
    if n > 100000 or n < 2:
        return print("잘못 입력")

    else:
        for i in range(n+1):
            if i == 0 or i == 1:
                result.append(i)
            else:
                x = result[i-1] + result[i-2]
                result.append(x % 1234567) #?
        return print(n, "번째 피보나치 수를 1234567로 나눈 수 : ", result[-1])
    
n = int(input("자연수 입력 >> "))
f(n)

#설명이 매우 이상함
#https://velog.io/@diddnjs02/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98
#이거 보기 전까지 절대 알수없다