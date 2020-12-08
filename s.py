import random
userInput = None    #변수 선언
accountList = set()

def createAccount():
    name = str(input('이름: '))
    age = int(input('나이: '))
    while True:
        acn = random.randrange(1,100)   #최대 100명의 USER가 있다고 가정
        if acn in accountList:
            acn = 0 #재선택
        else:
            accountList.add(acn)
            print(' -> ', name, '님의 계좌번호는 ', acn, '입니다.')
            return acn
            break

if (len(accountList) == 0):
    print('==========[ 비아 은행 ]==========')
    print(' - 계좌가 존재하지 않습니다.')
    print(' - 신규 계좌를 생성해 주세요.')
    a = createAccount()

while userInput != 0:   #defaultValue: 0
    print('g')
    userInput = int(input('u: '))
