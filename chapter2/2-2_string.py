# 문자열 자료형

a = "Life is too short, You need Python"
b = "a"
c = "123"
print(type(a))


# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
say = '"Python is very easy." he says.'
say2 = "\"Python is very easy.\" he says."
food = 'Python\'s favorite food is perl'
print(say)
print(say2)
print(food)


# 여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = "Life is too short\nYou need python"
multiline2 = '''
... Life is too short
... You need python
... '''
print(multiline)
print(multiline2)


# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)


# 문자열 곱하기
print(head * 3)


# 문자열 곱하기를 응용하기
print("=" * 50)
print("My Program")
print("=" * 50)


# 문자열 길이 구하기
text = "Life is too short, You need Python"
print(len(text))


# 문자열 인덱싱과 슬라이싱 - 인덱스는 0번 부터 시작
str = "Life is too short, You need Python"
print(str[3])
# -0은 0과 같아서 str[-0]은 str[0]과 동일
print(str[-3])


# 문자열 슬라이싱
string = "Life is too short, You need Python"
result = a[0] + a[1] + a[2] + a[3]
print(result)
# 위에를 아래 표현으로 쉽게 슬라이싱 가능
# a[ : ]
# a[이상:미만:간격]
print(string[0:4])  # 0부터 4이전인 3까지 출력
print(string[19:])  # 뒤에를 생략하면 끝까지 출력
print(string[::2])  # [::2] 처음부터 끝까지 2칸 간격으로 출력
print(string[19:-7])  # 19번부터 -7 이전까지 (-7이 Python 앞에 공백이니 d까지 출력)
print(string[::-1])  # 역순으로 출력


# 문자열 슬라이싱 활용
receivedData = "20250318Rainy"
date = receivedData[:8]
weather = receivedData[8:]
print(date)
print(weather)


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
ex1 = "I eat %d apples." % 3
print(ex1)

# 2. 문자열 바로 대입
ex2 = "I eat %s apples." % "five"
print(ex2)

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
ex3 = "I eat %d apples." % number
print(ex3)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
ex4 = "I ate %d apples. so I was sick for %s days." % (number, day)
print(ex4)

# 5. 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
ex5 = "Error is %d%%." % 98
print(ex5)


# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백 - 거의 안씀
eex1 = "%10s" % "hi"  # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬
print(eex1)
eex2 = "%-10sjane." % 'hi'  # 전체 길이가 10개, hi를 왼쪽에 채움 그리고 나서 jane이 등장
print(eex2)

# 2. 소수점 표현하기
eex3 = "%0.4f" % 3.42134234  # 소수점 넷째자리 까지
print(eex3)


# format 함수를 사용한 포매팅
# 1. 숫자 바로 대입하기
exex1 = "I eat {0} apples".format(3)
print(exex1)

# 2. 문자열 바로 대입하기
exex2 = "I eat {0} apples".format("five")
print(exex2)

# 3. 숫자 값을 가진 변수로 대입하기
number = 3
exex3 = "I eat {0} apples".format(number)
print(exex3)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
exex4 = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(exex4)

# 5. 이름으로 넣기
exex5 = "I ate {number} apples. so I was sick for {day} days.".format(
    number=10, day=3)
print(exex5)

# 6. 인덱스와 이름을 혼용해서 넣기
exex6 = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(exex6)

# 7~9 왼쪽,오른쪽,가운데 정렬 - 거의 안씀
strings = "{0:<10}".format("hi")  # 왼쪽 정렬
print(strings)
strings2 = "{0:>10}".format("hi")  # 오른쪽 정렬
print(strings2)
strings3 = "{0:^10}".format("hi")  # 가운데 정렬
print(strings3)

# 10. 공백 채우기 - 거의 안씀, 터미널로 게임 만들 때?? CLI프로그램 쓰일 지도(옛날 감성)
strings4 = "{0:=^10}".format("hi")
print(strings4)
strings5 = "{0:!<10}".format("hi")
print(strings5)

# 11. 소수점 표현하기
float = 3.42134234
print("{0:0.4f}".format(float))
float2 = "{0:10.4f}".format(float)
print(float2)

# 12. { 또는 } 문자 표현하기
ands = "{{ and }}".format()
print(ands)  # 중괄호를 적용하기 위해 중괄호를 두개 씀


# f 문자열 포매팅 - 이게 제일 중요, 3.6버전 이상에서 가능
# 1. 기본
name = '홍길동'
age = 30
sstring = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(sstring)
sstring2 = f'나의 이름은 {name}입니다. 나이는 {age + 1}입니다.'
print(sstring2)
sstring3 = f'나의 이름은 {name}입니다. 나이는 {age * 2}입니다.'
print(sstring3)

# 2. 정렬
sstring4 = f'{"hi":<10}'  # 왼쪽 정렬
print(sstring4)
sstring5 = f'{"hi":>10}'  # 오른쪽 정렬
print(sstring5)
sstring6 = f'{"hi":^10}'  # 가운데 정렬
print(sstring6)

# 3. 공백 채우기
sstring7 = f'{"hi":=^10}'  # 가운데 정렬하고 '=' 문자로 공백 채우기
print(sstring7)
sstring8 = f'{"hi":!<10}'  # 왼쪽 정렬하고 '!' 문자로 공백 채우기
print(sstring8)

# 4. 소수점
y = 3.42134234
results = f'{y:0.4f}'  # 소수점 4자리까지만 표현
print(results)
results2 = f'{y:10.4f}'  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
print(results2)

# 5. {} 중괄호 출력
curl = f'{{ and }}'
print(curl)

# 6. f 문자열을 사용하여 금액에 콤마(,) 삽입하기 - 이런건 검색, 외우지 말자
comma = f"난 {1500000:,}원이 필요해"
print(comma)