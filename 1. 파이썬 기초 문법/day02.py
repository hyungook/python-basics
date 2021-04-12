'''
Day 02

변수 입력과 연산자
'''

# a=input("숫자를 입력하세요 :")
# print(a)

# split
'''
a,b=input("숫자를 입력하세요 :").split()
a=int(a)
b=int(b)
print(a+b)
#print(type(a))



a,b=map(int,input("숫자를 입력하세요: ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # a 를 b로 나눈 몫
print(a%b) # a를 b로 나눈 나머지
print(a**b) # 제곱

'''


# type은 형이 다른 연산을 하면 더 넓은, 더 큰 범위로 출력값이 나온다.
a=4.3 #실수
b=5 #정수
c=a+b #실수
print(type(c))