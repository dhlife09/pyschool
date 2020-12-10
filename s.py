card = 0
userin = None


def payment(name, price):
  global card
  if (price < 1):
    message = '결제할 금액이 1원 미만일 수 없습니다.'
  elif (card >= price):
    card = card-price
    message = name + ' 결제에 성공했습니다. 남은 잔액: ' + str(card)
  else:
    message = '잔액이 부족합니다.'
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
