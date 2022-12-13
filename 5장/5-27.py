pL = []
dL = []

def diagnosis():
    str = input("입원하나요? y/n")
    if str == "y":
        dL.append(pL[0])
        del pL[0]
    else:
        del pL[0]
    print(f"입원 리스트 > {dL}")

def receipt():
    patient = input("진료 접수하실 분 이름 입력 >> ")
    pL.append(patient)
    print(f"{patient} 등록완료")
    
while True:
    n = int(input("1. 접수 2. 진료"))
    if n == 1:
        receipt()
    elif n == 2:
        diagnosis()
    else:
        break