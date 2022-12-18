lib = {}

while 1:
    switch = 0

    print("="*60)
    print("도서 관리 프로그램")
    print("1. 도서 등록")
    print("2. 도서 대여")
    print("3. 도서 검색")
    print("4. 전체 도서")
    print("5. 도서명 변경")
    print("6. 종료\n")

    num = int(input("입력 >> "))

    if num == 1:
        book = input("등록할 도서 입력 >> ")
        if book in lib:
            lib[book] = lib[book]+1
            print("한 권 추가")
        else:
            lib[book] = 1
            print(f"{book}을 한 권 추가", sep="")

        print(lib)

    elif num == 2:
        book = input("대여할 책 입력 >> ")
        if book in lib:
            if lib[book] > 0:
                lib[book] = lib[book] - 1
                print(f"{book} 대여", sep='')
            else:
                print("수량 부족")
            print(lib)
        else:
            print("없는 도서입니다.")

    elif num == 3:
        book = input("검색할 도서 입력 >> ")
        for k, v in lib.items():
            if book in k:
                print(f"{k}, {v}권")
                switch = 1
        if switch == 0:
            print("해당 없음")

    elif num == 4:
        print(lib)

    elif num == 5:
        book = input("변경할 책 이름 입력 >> ")
        if book in lib:
            new = input("새 책 입력 >> ")
            if new in lib:
                print("이미 있는 책")
            else:
                lib[new] = lib.pop(book)
        else:
            print("해당 책 없음")

    elif num == 6:
        quit()

    else:
        print("잘못 입력")
