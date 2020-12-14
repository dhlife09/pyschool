def odd_even(num):
    if (num%2 == 0):  # 기호
        return '짝수'
    else:
        return '홀수'


num=int(input('숫자: '))
result= odd_even(num)

print(num, "은(는)", result, "입니다")

