def encryption(p):
    p1 = ""
    for i in p:
        a = ord(i)
        a += 150
        p1 += chr(a)
    print(f"암호화 완료. {p1}")
    
def decryption(p):
    p1 = ""
    for i in p:
        a = ord(i)
        a -= 150
        p1 += chr(a)
    print(f"암호화 완료. {p1}")
    
while True:
    a = int(input("1. 암호화 2. 복호화 3. 종료"))
    if a == 1:
        encryption(input("문장 입력 >> "))
    elif a == 2:
        decryption(input("문장 입력 >> "))
    else: break