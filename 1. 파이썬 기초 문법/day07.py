'''

문자열과 내장함수

'''

msg="It is Time"
# upper() = 모두 대문자로 변환하는 함
print(msg.upper())
# lower() = 모두 소문자로 변환하는 함
print(msg.lower())
print(msg)

tmp=msg.upper()
print(tmp)
# find('?') = '?' 를 찾는 함수
print(tmp.find('T'))
# count('?') = '?'가 몇 번 있는지 확인하는 함수
print(tmp.count('T'))
print(msg)
# slice = [a:?] = a 부터 ? 번째 글자를 출력
print(msg[:2])
print(msg[3:5])

# len() = 공백 포함한 글자 수
print(len(msg))

for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')

print()


# 대문자만 출력 (.isupper)
for x in msg:
    if x.isupper():
        print(x, end=' ')
print()


# 소문자만 출력 (.islower)
for x in msg:
    if x.islower():
        print(x, end=' ')
print()


# 공백 제거 후 출력 (.isalpha)
for x in msg:
    if x.isalpha():
        print(x, end='')
print()


tmp='AZ'
# ord() = 아스키 넘버 출력 (A = 65 / Z = 90)
for x in tmp:
    print(ord(x))


tmp='az'
for x in tmp:
    print(ord(x))


# chr = 아스키 넘버에 대응하는 문자 출력
tmp=65
print(chr(tmp))