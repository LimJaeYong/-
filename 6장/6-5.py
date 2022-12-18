class Contact:
    def __init__(self, name, phone_num, email, addr):
        self.name = name
        self.phone_num = phone_num
        self.email = email
        self.addr = addr
    
    def print_info(self):
        print(f"이름: {self.name}")
        print(f"번호: {self.phone_num}")
        print(f"E-mail: {self.email}")
        print(f"주소: {self.addr}")
        
def set_contact():
    name = input("이름 입력 >> ")
    phone_num = input("번호 입력 >> ")
    e_mail = input("E-mail 입력 >> ")
    addr = input("주소 입력 >> ")
    contact = Contact(name, phone_num, e_mail, addr)
    return contact

def print_menu():
    print("1. 인적 사항 입력 \n2. 인적 사항 출력 \n3. 종료")
    n = int(input("메뉴 선택 >> "))
    return n

def printContact(contact_list):
    for i in contact_list:
        i.print_info()
        
def main():
    contact_list = []
    while True:
        menu = print_menu()
        if menu == 1:
            contact = set_contact()
            contact_list.append(contact)
        elif menu == 2:
            printContact(contact_list)
        elif menu == 3:
            break

if __name__ == "__main__":
    main()

