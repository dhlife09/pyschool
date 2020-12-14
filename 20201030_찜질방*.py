age = int(input('나이 입력: '))

if (age >= 60):
    print('30% 요금 할인대상입니다')
    cost = 14000*0.7
elif (age <= 10):
    print('20% 요금할인 대상입니다')
    cost = 14000*0.8
else:
    print('요금할인 대상이 아닙니다')
    cost = 14000
print('요금: ' + str(int(cost)))
