'''
함수 만들기

** 복습

'''

'''

# def = 함수 키워드
def add(a,b):
    c=a+b
    print(c)

add(3,2)



def add(a,b):
    c=a+b
    return c

x=add(3,2)
# print(add(3,2))
print(x)



def add(a,b):
    c=a+b
    d=a-b
    return c,d

print(add(3,2))


'''

def isPrime(x):
    for i in range(2, x):
        if x%i==0:
            return False
    return True

a=[12,13,7,19]

for y in a:
    if isPrime(y):
        print(y, end=' ')