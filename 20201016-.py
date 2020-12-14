print('이름을 입력해주세요')
name = input()
print(name + '님 안녕하세요')
age = int(input('나이를 입력해주세요: '))
if (age >= 20):
    print(str(abs(20-age)) + '년 전에 20살이 넘었어요 ㅋ')    # abs => 절대값
else:
    print(str(20-age) + '년 후면 20살이시네요')
