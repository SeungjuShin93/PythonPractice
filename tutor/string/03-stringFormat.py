# format 함수를 사용한 포매팅
# 1. 숫자 바로 대입하기
string = "I eat {0} apples".format(3)
print(string)

# 2. 문자열 바로 대입하기
string = "I eat {0} apples".format("five")
print(string)

# 3. 숫자 값을 가진 변수로 대입하기
number = 3
string = "I eat {0} apples".format(number)
print(string)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
string = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(string)

# 5. 이름으로 넣기
string = "I ate {number} apples. so I was sick for {day} days.".format(
    number=10, day=3)
print(string)

# 6. 인덱스와 이름을 혼용해서 넣기
string = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(string)

# 7. 소수점 표현하기
float = 3.42134234
print("{0:0.4f}".format(float))

# 8. { 또는 } 문자 표현하기
ands = "{{ and }}".format()
print(ands)  # 중괄호를 적용하기 위해 중괄호를 두개 씀

string = "I ate {{ {0} }} apples. so I was sick for {day} days.".format(
    10, day=3)
print(string)