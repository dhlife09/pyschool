for i in range(10, 0, -1):  # 역순으로 ( 10부터 0까지 (10, 9, 8, 7, 6, 5, 4, 3, 2, 1) -1씩 증가)
    print(i)

for i in range(200, 9 , -5):    # 200부터 10까지 -5씩 증가
    print(i)
    
sum = 0

for i in range(1, 101, 1):  # 1부터 100까지 1씩 증가
    print(i)
    sum = sum + i
print('합계: ', sum)


'''
sum = 0
for i in range(1, 101, 2):
    print(i)
    sum = sum+i
print(sum)

total = 0
point = 0

for i in range(1, 21, 1):
    point = int(input('점수: '))
    print(point, '점이 추가됩니다.')
    total = total + point
print('최종 점수: ', total)

'''


