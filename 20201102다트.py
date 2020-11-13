'''
point = 0
uinpt = 0
while (point < 20):
    uinpt = int(input('점수 입력: '))
    point = point + uinpt
    print(str(uinpt) + '점 추가되었습니다.')
print(str(point) + '점으로 20점이 넘었어요.')

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#__#_#_#_#

star = 0

while star < 100:
    star = star + 1
    print('★' + str(star))

'''

basket = 0
soccer = 0
baseba = 0

userin = ''

while (userin != '3'):
    userin = input('농구공[0] 축구공[1] 야구공[2] 종료[3]: ')
    if (userin == '0'):
        basket = basket + 1
    elif (userin == '1'):
        soccer = soccer + 1
    elif (userin == '2'):
        baseba = baseba + 1
    elif (userin == '3'):
        break
    else:
        print('잘못된 입력')

print('\n===== [ TOTAL ] =====')
print('농구공: ' + str(basket) + '개')
print('축구공: ' + str(soccer) + '개')
print('야구공: ' + str(baseba) + '개')


