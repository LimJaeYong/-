import datetime


def time():
    global now
    now = datetime.datetime.now()
    print(f"시간 : {now.minute}분 {now.second}초")


print("10초 맞추기")
while True:
    num = int(input("1. 시작 2. 종료"))
    if num == 1:
        while True:
            time()
            start_s = now.second
            s = input("10초 세고 엔터...")
            time()
            end_s = now.second
            result = end_s - start_s
            print(f"결과 : {result}초")
            if result == 10:
                print("10초 맞추기 성공")
                break
            else:
                print("10초 맞추기 실패")
                break
    elif num == 2:
        break
    else:
        continue