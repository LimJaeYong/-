import sys

input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]
dic = {}
result = 0
num = 9

for w in words:
    cnt = len(w) - 1
    for ww in w:
        print(ww)
        if ww not in dic:
            dic[ww] = pow(10, cnt)
        else:
            dic[ww] += pow(10, cnt)
        cnt -= 1

dic = sorted(dic.values(), reverse=True)

for v in dic:
    result += v*num
    num -= 1

print(result)
