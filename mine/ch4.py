userInfo = {} # 계정 정보가 저장 될 딕셔너리 # key = ID, value = PW
login_condition = False # 입력받은 ID와 PW이 어느 함수로 들어가야할 지 방향을 정해줌 # True면 딕셔너리에 한가지 이상 값이 저장 되어있는 상태, False면 값을 생성해야 하는 상태

def info_insert(id, pw):
    userInfo[id] = pw #딕셔너리에 입력받은 ID와 PW추가 
    print(f"{id} created.")
    main()

def login_input(login_condition):
    id = input("ID : ")
    pw = input("PW : ")
    if login_condition == True:
        check_id(id, pw)
    else:
        info_insert(id, pw)

def check_id(id, pw):
    if id not in userInfo or pw != userInfo.get(id): # 입력한 ID가 userInfo key중 존재하지 않거나 ID의 value와 입력한 PW가 같지 않다면
        print("Please re_enter your ID and password\n")
        print("Do you want to create a new account?")
        a = input("y/n\n>>")
        if a == "y": # 새로운 계정 생성
            login_condition = False
            login_input(login_condition)
        else: # 재입력
            main()

    if id in userInfo and pw == userInfo.get(id): # 입력한 ID가 userInfo에 존재하고 PW가 ID의 value와 같다면
        print(f"\nWelcome {id}.")
        after_login(id) # 로그인 후 행동으로 이동

def after_login(id):
    while True:
        print("What do you want to do?\n")
        print("1. Inquire whole user ID")
        print("2. Change your password")
        print("3. Create new account")
        print("4. Delete user info")
        print("5. Log out")

        n = int(input(">>"))

        if n == 1: # 딕셔너리 조회
            print(userInfo.keys())
        elif n == 2: # 존재하는 key의 value 수정
            userInfo[id] = input("Please enter new password")
        elif n == 3: # 새로운 계정 생성
            login_condition = False
            login_input(login_condition)
        elif n == 4: # 현재 key 정보 삭제
            del userInfo[id]
            print("Your Info has been deleted")
            main()
        else: # 종료
            break

def main():
    global login_condition # 전역변수 선언
    
    print("\n\n          Login\n\n")
    print("Please enter your ID and password")
    if bool(userInfo) == True: # userInfo가 비어있지 않으면
        login_condition = True # 입력받을 ID와 PW는 check_id로

    login_input(login_condition) # 입력함수


main()
