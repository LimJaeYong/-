book_info = []

def reservation():
    print("예약하는 분 입력")
    book_info.append(input(">> "))

def view():
    for i in book_info:
        print(i)

def mod():
    a = input("수정할 예약정보 입력")
    if a in book_info:
        book_info[book_info.index(a)] = input("새로운 정보 입력")
    else:
        print("재시도")
        main()

def delete():
    a = input("삭제할 예약정보 입력")
    book_info.remove(a)

def main() :
    while True:
        print("예약 관리 프로그램")
        print("1. 예약")
        print("2. 조회")
        print("3. 변경")
        print("4. 삭제")
        print("5. 종료")
        n = int(input("항목 선택 > "))
        
        if n == 1:
            reservation()
        elif n == 2:
            view()
        elif n == 3:
            mod()
        elif n == 4:
            delete()
        else:
            quit()
        
        
main()