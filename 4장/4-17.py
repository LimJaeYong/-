import random


menus = ['a','b','c','d']

price = ['1000','2000', '3000', '4000']

print("메뉴 : ")

for i in range(len(menus)) :
    print(menus[i], price[i])

i = random.randint(0, len(menus)-1)

print('추천 메뉴: ', menus[i])
print('메뉴 가격: ', price[i])