'''
리스트와 내장함수(2)

'''

a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
# len() = 값의 개수
print(len(a))

for i in range(len(a)):
    print(a[i], end=' ')
print()


for x in a:
    print(x, end=' ')
print()


for x in a:
    if x%2==1:
        print(x, end=' ')
print()


# enumerate(a) = index + value 값을 묶어서 출력
for x in enumerate(a):
    print(x)
print()

# 튜플은 값 변경이 안된다.
b=(1,2,3,4,5)
print(b[0])
# b[0]=7 => X


for x in enumerate(a):
    print(x[0], x[1])
print()


for index, value in enumerate(a):
    print(index, value)
print()



# all - 전체가 참이면 yes , 하나라도 거짓이면 no
if all(60>x for x in a):
    print("Yes")
else:
    print("No")


# any - 일부 / 전체 거짓이어야 no
if any(15>x for x in a):
    print("Yes")
else:
    print("No")