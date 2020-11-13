
'''

책에 없음 주의 !

'''

a = [1, 3, 5]
print(a[0])     # 1
print(a[-1])    # 5
print(len(a))   # 3
print(a[1:2])   # [3]
print(a[1:])    # [3, 5]
print(a[:2])    # [1, 3]

for i in range(3):
    print(a[i])

g = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
print(g[4])

b = [2, 4, 6, 8]

b = b+[10, 12, 14]
print(b)

b.append(10)
print(b)

b[1] = 3
print(b)

planetScale = [2440, 6052, 6378, 3390, 69911, 58232, 25362, 24622]
maxScale = planetScale[0]
for i in range(1, 8):
    if planetScale[i] > maxScale:
        maxScale = planetScale[i]
print(maxScale)
