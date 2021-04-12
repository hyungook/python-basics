'''
람다 함수
(익명함수)
'''

'''

def plus_one(x):
    return x+1
print(plus_one(1))


#람다함수 lambda
plus_two=lambda x: x+2
print(plus_two(1))


'''

def plus_one(x):
    return x+1

a=[1,2,3]
print(list(map(plus_one, a)))
# lambda함수
print(list(map(lambda x:x+1, a)))