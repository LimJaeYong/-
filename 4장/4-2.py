x = []
for i in range(5):
    x.append(int(input(f"{i+1}번 인덱스 입력 >> ")))

print(f"최댓값 : {max(x)}")
print(f"최댓값의 위치 : {x.index(max(x))}번")

##리스트 함수를 이용하면 간단하게 해결 가능