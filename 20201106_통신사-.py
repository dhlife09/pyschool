tprice = 0
tttime = 0

temptm = 0

for i in range(1, 13, 1):
    temptm = int(input(str(i) + '월 통화시간(분): ' ))
    tttime = tttime + temptm
    tprice = tprice + temptm*60*2
    
    print(i, '월 통화 시간은 ', temptm, '분, 통화 요금은 ', temptm*60*2, '원')
    
print('1년 동안의 통화 시간은', tttime, '분, 사용 요금은 ', tprice, '원 ')

