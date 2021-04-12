'''
Day 01

변수명 정하기
1) 영문과 숫자, _로 이루어진다.
2) 대소문자를 구분한다.
3) 문자나, _로 시작한다.
4) 특수문자를 사용하면 안된다.(if, for 등)

'''

a=1
A=2
A1=3
#2b=4
print(a,A,A1)
a,b,c=3,2,1
print(a,b,c)

#값 교환
a,b=10, 20
print(a,b)
a,b=b,a
print(a,b)

#변수 타입
a=12345
print(type(a))
a=12.123456789123456789
# 실수형은 8byte를 넘어가면 데이터가 소실된다.
print(a)
print(type(a))
a='student'
print(a)
print(type(a))



# 출력 방식
print("number")
a,b,c=1,2,3
print(a,b,c)
print("number :",a,b,c)
# seperate = sep=''
print(a,b,c, sep='')
print(a,b,c, sep='\n') # 줄바꿈

print(a, end=' ') # 줄바꾸기 없앰
print(b, end=' ')
print(c)

