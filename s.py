'''
수행 주제 및 알고리즘
카드에 있는 잔액으로 물건을 결제하는 프로그램을 제작해 보았다.

프로그램을 실행하면 먼저 카드와 입력을 위한 변수를 선언하고 while 반복문으로 메뉴([1] 잔액 확인, [2] 잔액 충전, [3] 결제 하기)를 입력받는다. 잔액 확인 메뉴를 요청하면 현재 카드의 잔액을 알려주고 잔액 충전 메뉴를 요청하면 충전할 금액을 입력받고 카드에 입력한 금액만큼의 금액을 충전해 준다. 결제 하기 메뉴를 요청하면 상품의 이름과 상품의 가격을 입력받고 payment 함수로 이동해 먼저 결제할 금액이 1원 미만인지(결제 불가), 물건의 금액보다 카드의 금액이 크거나 같을 경우에만 카드의 잔액에서 물건의 가격을 차감하고 사용자에게 결제를 완료했음을 알린다. 결제할 금액이 1원 미만(결제 불가) 상태이거나 결제가 완료한 경우가 아니라면 잔액이 부족하다는 메시지를 띄운다.

수행 중 느낀 점
결제하는 부분은 함수(payment)를 제작해 while -> if 문에서 분리해 내었더니 코드가 훨씬 간결해지고 유지보수하기도 더 편해진 것 같다. 평소 프로그래밍을 할 때 함수를 잘 활용하지 않는데 앞으로는 함수를 자주 사용해봐야겠다.

'''

card = 0
userin = None

# 1210 박도현 정보 수행평가: 파이썬

def payment(name, price):
  global card
  if (price < 1):
    message = '결제할 금액이 1원 미만일 수 없습니다.'
  elif (card >= price):
    card = card-price
    message = name + ' 결제에 성공했습니다. 남은 잔액: ' + str(card)
  else:
    message = '잔액이 부족합니다. 현재 잔액: ' + str(card)
  return message
  
while (userin != 0):
  print('[0] 종료 / [1] 잔액 확인 / [2] 잔액 충전 / [3] 결제하기')
  userin = int(input(' -> '))
  if (userin == 1):
    print('현재 잔액은 ', card, '원 입니다.')
  elif (userin == 2):
    print('충전할 금액을 입력해 주세요.')
    card = card+int(input(' -> '))
    print('충전되었습니다.')
  elif (userin == 3):
    name = str(input(' 물건 이름: '))
    pric = int(input(' 물건 가격: '))
    print(payment(name, pric))
  elif (userin == 0):
    break
  else:
    print('잘못 입력하셨습니다.')
  print('')
