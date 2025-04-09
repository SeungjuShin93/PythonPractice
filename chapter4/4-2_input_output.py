# 사용자 입출력
#! input 사용하기
a = input()

print("너가 입력한 것 : " + a)


#! 프롬프트를 띄워 사용자 입력받기
number = input("숫자를 입력하세요: ")
print(number)
print(type(number))


#! print 자세히 알기
a = 123
print(a)
a = "Python"
print(a)
a = [1, 2, 3]
print(a)


#! 큰따옴표로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short")  # 1번
print("life"+"is"+"too short")  # 2번


#! 문자열 띄어쓰기는 쉼표로 한다
print("life", "is", "too short")


#! 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')
# 재미
print()
for i in range(10):
    print(i, end='ㅋㅋ')
