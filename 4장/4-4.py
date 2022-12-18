import random

R = []
option = ["가위", "바위", "보"]

for i in range(10000):
    comA = random.choice(option)
    comB = random.choice(option)
    
    if comA == "가위":
        if comB == "가위":
            R.append("비김")
        elif comB == "바위":
            R.append("B")
        else:
            R.append("A")
            
    elif comA == "바위":
        if comB == "가위":
            R.append("A")
        elif comB == "바위":
            R.append("비김")
        else:
            R.append("B")
            
    elif comA == "보":
        if comB == "가위":
            R.append("B")
        elif comB == "바위":
            R.append("A")
        else:
            R.append("비김")
   
aWin = R.count("A")   
bWin = R.count("B")   
Draw = R.count("비김")
         
if aWin != bWin:
    if aWin > bWin:
        print(f"{aWin}times A win")
    else:
        print(f"{bWin}times B win")
else:
    print("Draw")