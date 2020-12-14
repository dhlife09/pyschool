
'''

책에 없음 주의 !

'''

a = [1, 3, 5]
print(a[0])     # 0번째 값 -> 1
print(a[-1])    # 뒤에서 첫번째: 5
print(len(a))   # 3(개)
print(a[1:2])   # [3]    1번부터 1개 값
print(a[1:])    # [3, 5] 1번부터 2개 값
print(a[:2])    # [1, 3] 0번부터 2개 값

for i in range(3):  #3번 반복
    print(a[i])

g = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
print(g[4]) #목성

b = [2, 4, 6, 8]

b = b+[10, 12, 14]
print(b)    # 2, 4, 6, 8, 10, 12, 14

b.append(10)    # 10을 하나 더 추가함
print(b)

b[1] = 3    # b의 첫번째 값(4)를 3으로 지정
print(b)

planetScale = [2440, 6052, 6378, 3390, 69911, 58232, 25362, 24622]
maxScale = planetScale[0]
for i in range(1, 8):   # 1번부터 7번까지(1, 2, 3, 4, 5, 6, 7) 반복
    if planetScale[i] > maxScale:
        maxScale = planetScale[i]
print(maxScale)
