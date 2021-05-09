# 입출력과 사칙연산

'''
# 2557
Hello World!를 출력하시오.

'''
print('Hello World!')

'''
# 10718
두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

'''
print('강한친구 대한육군','강한친구 대한육군',sep='\n')

'''
# 10171
아래 예제와 같이 고양이를 출력하시오.

'''
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")


'''
# 1000
첫째 줄에 A+B를 출력한다.

'''
a,b=input().split()
a=int(a)
b=int(b)
print(a+b)

'''
# 1001
첫째 줄에 A-B를 출력한다.

'''
print(a-b)

'''
# 10998
첫째 줄에 A x B를 출력한다.

'''
print(a*b)

'''
# 1008
첫째 줄에 A / B를 출력한다.

'''
print(a/b)


'''
# 10869
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

'''
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)


'''
# 10430
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

'''
a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
print(int((a+b)%c))
print(int(((a%c)+(b%c))%c))
print(int((a*b)%c))
print(int(((a%c)*(b%c))%c))



'''
# 2588
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

'''

A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈


num1 = int(input())
num2 = input()

for i in range(0, 3):
    result = num1*int(num2[2-i])
    print(result)
 
print(num1*int(num2))