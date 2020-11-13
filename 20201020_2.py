
'''
type = input('승객 유형(임산부/노약자/일반): ') #ddf

if (type == '임산부' or type == '노약자'):
    print('좌석 이용가능')
else:
    print('좌석 이용불가')

'''


'''
type = input('승객 유형(임산부/노약자/일반): ') #ddf

if (type != '임산부' and type != '노약자'):
    print('좌석 이용불가')
else:
    print('좌석 이용가능')
'''


'''
type = input('종류 입력 [사람, 강아지, 고양이, 새]: ')

if (not type == '사람'):
    print('운송 용기 사용')
else:
    print('운송 용기 미사용')
'''


type = input('종류 입력 [사람, 강아지, 고양이, 새]: ')

if (type != '사람'):
    print('운송 용기 사용')
else:
    print('운송 용기 미사용')
