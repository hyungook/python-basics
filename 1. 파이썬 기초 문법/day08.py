'''
리스트와 내장함수(1)

'''

import random as r

a=[]

# print(a)
b=list()
# print(b)


a=[1,2,3,4,5]
# print(a)
# print(a[0])

b=list(range(1, 11))
# print(b)

c=a+b
# print(c)


print(a)
# append = 추가
a.append(6)
print(a)

# insert = 특정 위치에 삽입
a.insert(3,7)
print(a)

# pop() = 맨 뒤에 있는 값을 제거
# pop(3) = 3번째 있는 값을 제거
a.pop()
print(a)
a.pop(3)
print(a)

# remove(4) = '4'를 찾아서 삭제
a.remove(4)
print(a)

# index(5) = '5' 를 찾아 list 배열 안에서 몇 번째에 있는지 출력
print(a.index(5))



a=list(range(1,11))
print(a)
# sum(a) = 인자값 안에 있는 모든 값을 합한다.
print(sum(a))
# max(a) = 인자값 안에서 가장 큰 값을 찾는
print(max(a))
# min(a) = 인자값 안에서 가장 작은 값을 찾는
print(min(a))

print(min(7,5))
print(min(7,5, 3))



print(a)
# random
# suffle = 섞는 함수
r.shuffle(a)
print(a)
# .sort() = 오름차순 정렬
a.sort()
print(a)
# .sort(reverse=True)
a.sort(reverse=True)
print(a)




# .clear() = 초기화
a.clear()
print(a)