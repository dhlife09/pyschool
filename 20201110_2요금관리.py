name = ['홍길동', '이순신', '황진이']
gend = ['남', '남', '여']
time = [100, 50, 72]
disc = ['없음', '청소년', '국가유공자']


user = len(name)
price = 0
total_m = 0
total_w = 0
total_a = 0


print('전체 사용자 수: ', user)
print('\n')
for i in range(0, user) :
    if disc[i] == '청소년':
        # 20% 할인
        price = int(time[i]*60*2*0.8)
        #print(i, '번 사용자 요금(청소년): ', price, '원')
    elif disc[i] == '국가유공자':
        # 30% 할인
        price = int(time[i]*60*2*0.7)
        #print(i, '번 사용자 요금(국가유공자): ', price, '원')
    else:
        price = int(time[i]*60*2)
        #print(i, '번 사용자 요금(일반): ', price, '원')

    print(i,'번 사용자 요금(', disc[i],'): ', price, '원')

    if gend[i] == '남':
        total_m = total_m + price
    elif gend[i] == '여':
        total_w = total_w + price

    total_a = total_a + price


print('\n')
print('남자 회원 사용요금: ', total_m, '원')
print('여자 회원 사용요금: ', total_w, '원')
print('전체 회원 사용요금: ', total_a, '원')
