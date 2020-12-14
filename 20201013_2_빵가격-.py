

#price=800
#bread=10

price=int(input('빵 가격: '));
bread=int(input('빵 개수: '));
total=price*bread
total=total-total*0.1


print('합계: ' + str(int(total)) + '원')
#print('합계:', str(int(total)), '원')
