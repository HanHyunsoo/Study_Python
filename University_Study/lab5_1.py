"""
챕터: day5
주제: 함수
문제:
두 개의 정수를 매개변수로 받아서, 두 수의 차를 반환하는 함수 subtract를 정의한다.
4, 9을 매개변수로 subtract를 호출한 후 결과를 출력한다.
작성자: 한현수
작성일: 2018.10.2.
"""
# 두 수의 차를 반환하는 함수
def subtract(a, b):
    # a: 첫번째 수, b: 두번째 수
    return a - b

# 함수를 이용해 a, b의 차를 구한다.
print(subtract(4, 9))
print(subtract(b=4, a=1)) # 키워드에 의한 매개변수 가능

a = 10
b = True
c = '김치'

print(type(a)) # 변수의 타입을 반환하는 함수
print(type(b))
print(type(c))