# 문자열

'''
# 11654 아스카 코드
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.
'''

a = str(input())

print(ord(a))

'''
# 11720
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
'''
a = int(input())
b = input()
result = 0

for i in range(a):
  result += int(b[i])
  i += 1

print(result)