'''
03. k 번째 큰 수 
'''

import sys
sys.stdin=open("input.txt","rt")
n, k=map(int, input().split())
a=list(map(int, input().split()))
# set이라는 자료구조는 중복을 제거한다.
res=set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
# set자료 구조에는 sort 기능이 없다. 그래서 list 화 시켜준다.
res=list(res)
res.sort(reverse=True)
print(res[k-1])
