'''
조건문 if(분기, 중첩)

'''

'''

x=7
if x==7:
    print("Lucky") # 들여쓰기가 중요하다. 기본 4칸
    print("O")

y=5
if y!=7:
    print("X")

    

x=15
if x>=10:
    if x%2==1:
        print("10이상의 홀수")
    

x=9
if x>0:
    if x<10:
        print("10보다 작은 자연수")



# 논리연산자
x=7
if x>0 and x<10:
    print("10보다 작은 자연수")



x=7
if 0<x<10:
    print("10보다 작은 자연수")



#분기문
x=10
if x>0:
    print("양수")
else:
    print("음수")


'''

#다중if문
x=92
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')

# 별개의 문장
if x>=90:
    print('A')
if x>=80:
    print('B')
if x>=70:
    print('C')
