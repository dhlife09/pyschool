# 교 159p

def FtoC(F):
    C = (F-32)/1.8
    return C

def CtoF(C):
    F = C*1.8+32
    return F

F = int(input('변환할 화씨 온도: '))
C = FtoC(F)
print(C)

C = int(input('변환할 섭씨 온도: '))
F = CtoF(C)
print(F) 
