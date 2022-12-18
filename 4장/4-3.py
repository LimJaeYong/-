print("     영화 예메 시스템\n\n")

movie = {"범죄도시(KR)": 19, "토이스토리(US)": 12, " 버즈라이트 이어(US)": 12, "알포인트(KR)": 19}
print("1. 영화목록 확인"
      "2. 영화등급 확인"
      "3.영화국적 확인"
      "4. 영화시스템 종료")

userNum = int(input("확인할 번호 입력 >> "))

while 1:
    if userNum == 1:
        for k, v in movie.items():
            print(k, v)

    if userNum == 2:
        for v in movie.values():
            print(f"{v}세 이용가")

    if userNum == 3:
        userCo = input("검색할 국적 입력 >> ")
        for k, v in movie.items():
            if userCo in k:
                print(k)

    if userNum == 4:
        break
