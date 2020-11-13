height = int(input('키를 입력해주세요: '))
weight = int(input('몸무게를 입력해주세요: '))
bmi = (weight / (height * height))*10000
print('체질량 지수:' + str(bmi))
