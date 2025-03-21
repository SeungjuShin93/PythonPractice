# 문자열 포매팅 따라 하기
'''
문자열 포맷 코드
%s	문자열(String)
%c	문자 1개(character)
%d	정수(Integer)
%f	부동소수(floating-point)
%o	8진수
%x	16진수
%%	Literal % (문자 % 자체)'
'''
# 1. 숫자 바로 대입
string = "I eat %d apples." % 3
print(string)

# 2. 문자열 바로 대입
string = "I eat %s apples." % "five"
print(string)

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
string = "I eat %d apples." % number
print(string)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
string = "I ate %d apples. so I was sick for %s days." % (number, day)
print(string)

# 5. 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
string = "Error is %d%%." % 98
print(string)

# 6. 소수점 표현하기
number = "%0.4f" % 3.42134234  # 소수점 넷째자리 까지
print(number)