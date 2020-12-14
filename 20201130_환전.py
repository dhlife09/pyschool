def exchange(c, m):
    m = m/1000
    if c == 1:
        m = str(m*0.9) + '$(달러)'
    elif c == 2:
        m = str(m*0.8) + '€(유로)'
    elif c == 3:
        m = str(m*5.6) + '¥(위안)'
    elif c == 4:
        m = str(m*91.8) + '¥(엔)'
    else:
        m = 'ERROR'
    return m

print('[1] 달러 [2] 유로 [3] 위안 [4] 엔')
c = int(input('환전 코드: '))
m = int(input('환전 금액: '))
r = exchange(c, m)
print(r) 
