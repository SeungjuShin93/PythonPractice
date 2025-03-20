# 문자열 자료형

# 1. 타입 확인
a = "Life is too short, You need Python"
print(type(a))

# 2. 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
say = '"Python is very easy." he says.'
print(say)
say2 = "\"Python is very easy.\" he says."
print(say2)
food = 'Python\'s favorite food is perl'
print(food)

# 3. 여러 줄인 문자열을 변수에 대입하고 싶을 때
multiline = "Life is too short\nYou need python"
print(multiline)
multiline2 = '''Life is too short
You need python'''
print(multiline2)

# 4. 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

# 5. 문자열 곱하기
print(head * 3)

# 6. 문자열 곱하기를 응용하기
print("=" * 50)
print("My Program")
print("=" * 50)

# 7. 문자열 길이 구하기
string = "Life is too short, You need Python"
print(len(string))

# 8. 문자열 인덱싱과 슬라이싱 - 인덱스는 0번 부터 시작
str = "Life is too short, You need Python"
print(str[3])
# -0은 0과 같아서 str[-0]은 str[0]과 동일
print(str[-3])

# 9. 문자열 슬라이싱
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


# 10. 문자열 슬라이싱 활용 (퀴즈)
data = "20250318Rainy"

date = data[:8]
weather = data[8:]
print(date)
print(weather)