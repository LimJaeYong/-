def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A')+n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a')+n) % 26 + ord('a'))
    return s


while True:
    str1 = input("암호화 할 알파벳 입력 >> ")
    if len(str1) > 8000:
        continue

    n = int(input("밀 수 입력"))

    if 0 < n < 26:
        print(caesar(str1, n))
    else:
        continue
