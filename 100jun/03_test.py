
# for 문

'''
# 2739

N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
출력형식과 같게 N*1부터 N*9까지 출력한다.
'''

a = int(input())

for i in range (1, 10):
    print(a, '*',i,'=', a*i)


'''
# 10950
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

각 테스트 케이스마다 A+B를 출력한다.
'''

t = int(input())

for i in range(t):
    a,b = map(int, input().split())
    print(a + b)


'''
# 8393
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

1부터 n까지 합을 출력한다.
'''

n = int(input())
a = int(0)

for i in range(n+1):
    a += i
    
print(a)


'''
# 15552

# sys and sys.stdin.readline()  => 공부

# sys.stdin.readline()
'''

import sys

t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(a + b)







