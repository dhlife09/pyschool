base = 270
use = int(input('전기 사용량: '))
cost = base*use

if (base > use) : #누진세추가
    cost = cost + cost*0.2
    print('전기 요금: ' + str(cost) + '원(누진세 적용됨)')
else:
    print('전기 요금: ' + str(cost) + '원')
print('전기 사용량: ' + str(use) + 'kW')
