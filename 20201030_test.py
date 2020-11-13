
import random
import sys
mod = sys.modules[__name__]

group_1 = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ']
group_2 = ['1', '2','3','4','5','6','7','8','9']
selected_1 = []
selected_2 = []


def selectRandom(groupName):
    print(groupName)
    while True:
        temp = random.choice(group_1) # Data 비교를 위한 임시 변수
        if (len(selected_1) != 2):
            if temp not in setattr(mod, 'selected_{}'.format(groupName), groupName):   # Already Selected == false 일 경우
                selected_1.insert(0, temp)   # Selected 에 추가
                print(selected_1[0])         
        elif (len(selected_1) == 2): # group A 에서 2명 선정 완료하면
                break;              # 중단

selectRandom(input('선정할 그룹 이름: '))


for i in range(1,6):
    dt = "group_"+str(i)
    print(locals()[dt])
