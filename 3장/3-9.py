import random

goodsong = ['a1 - a1','a2 - a2','a3 - a3']
sadsong = ['b1 - b1', 'b2 - b2', 'b3 - b3']
angrysong = ['c1 - c1', 'c2 - c2', 'c3 - c3']

while True:
    feeling = input("기분 입력(슬픔, 신남, 나쁨) >> ")
    
    if feeling == '그만':
        break
    
    if feeling == "신남":
        print("\n신나는 하루라 다행이네요! 기분에 맞는 신나는 노래를 추천 해드릴게요!\n\n", random.choice(goodsong),"\n")

    elif feeling == "슬픔":
        print("\n내일은 분명 괜찮을거에요. 노래 듣고 힘내세요!\n\n",random.choice(sadsong),"\n")
        
    elif feeling == "나쁨":
        print("\n듣고 기분전환이 되길 바랍니다. 분명 지나갈거에요!\n\n", random.choice(angrysong),"\n")