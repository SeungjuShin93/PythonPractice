# def 함수_이름(매개변수):
#     수행할_문장1
#     수행할_문장2
#     ...

# 아래는 함수의 정의
def add(a, b):  # 매개변수
    return a + b


# 함수의 사용 - 소괄호
a = 3
b = 4
c = add(a, b)  # add(3, 4)의 리턴값을 c에 대입 - 인수
print(c)

# 용어 정리 (혼용해서 많이 씀)
# 매개변수(parameter) - 함수에서 정의되어 사용되는 변수 (=인자, 파라미터)
# 인수(arguments) - 함수를 호출할 때 건네주는 변수
# 리턴값을 결괏값, 출력값, 반환값, 돌려 주는 값


# ? 일반적인 함수 - 입력값이 있고 리턴값이 있는 함수가 일반적인 함수
# def 함수_이름(매개변수):
#     수행할_문장
#     ...
#     return 리턴값
def add(a, b):
    result = a + b
    return result


a = add(3, 4)
print(a)


# ? 입력값이 없는 함수
def say():
    return 'Hi'


a = say()  # 매개변수를 넣으면 오류
print(a)


# ? 리턴값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))


a = add(1, 2)
print(a)  # None이 출력, 리턴 값이 없음


# ? 입력값도, 리턴값도 없는 함수
def say():
    print('Hi')


say()


#! 매개변수를 지정하여 호출하기
def sub(a, b):
    return a - b


result = sub(3, 1)
print(result)
result2 = sub(a=7, b=3)  # a에 7, b에 3을 전달
print(result2)
result3 = sub(b=7, a=3)  # b에 7, a에 3을 전달
print(result3)


#! 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
# def 함수_이름(*매개변수):
#   수행할_문장
#   ...
def add_many(*args):
    result = 0
    for i in args:
        result = result + i   # *args에 입력받은 모든 값을 더한다.
    return result


result = add_many(1, 2, 3)
print(result)
result2 = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result2)


# 단일 + 여러 개
def add_mul(choice, *args):
    if choice == "add":   # 매개변수 choice에 "add"를 입력받았을 때
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":   # 매개변수 choice에 "mul"을 입력받았을 때
        result = 1
        for i in args:
            result = result * i
    return result


result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result2 = add_mul('mul', 1, 2, 3, 4, 5)
print(result2)


# 키워드 매개변수, kwargs, ** 별 2개는 key, value 즉 딕셔너리 형태로
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1)
print_kwargs(name='foo', age=3)


#! 함수의 리턴값은 언제나 하나이다
def add_and_mul(a, b):
    return a+b, a*b
# a+b와 a*b라는 값2개가 리턴 되는 것이 아닌, 튜플값 하나인 (a+b, a*b)로 리턴


result = (7, 12)
print(result)

# 만약 이 하나의 튜플 값을 2개의 값으로 분리하여 받고 싶다면
result1, result2 = add_and_mul(3, 4)

# 만약 리턴문을 두개 쓴다면?


def add_and_mul(a, b):
    return a+b
    return a*b


result = add_and_mul(2, 3)
print(result)  # 2+3을 한 5만 나옴

# 즉 함수는 return문을 만나는 순간 결괏값을 돌려준 다음 함수를 빠져나가게 된다.


#! return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)


say_nick('승주님')
say_nick('아섬님')
say_nick('바보')


#! 매개변수에 초깃값 미리 설정하기
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("홍길동", 27)
say_myself("홍길동", 27, True)
say_myself("홍길선", 27, False)


# 기본 값을 나타내는 함수는 제일 뒤로 나와야 함
# 초기화하고 싶은 매개변수는 항상 뒤쪽에 놓아야 함
def say_myself(name, man=True, age=22):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself("홍길선", False, 22)


#! 함수 안에서 선언한 변수의 효력 범위
# def vartest(a)에서 입력값을 전달받는 매개변수 a는 함수 안에서만 사용하는 변수일 뿐, 함수 밖의 변수 a와는 전혀 상관음
# 지역변수, 전역변수
a = 1


def vartest(a):
    a = a + 1
# def vartest(hello):
#     hello = hello + 1
# 왼쪽은 지역변수, 오른쪽에는 매개변수
# 함수 안에서 사용하는 매개변수는 함수 밖의 변수 이름과는 전혀 상관없음


vartest(a)
print(a)  # 1


# 다른 예시 - 오류
'''
def vartest(test):
    test = test + 1
    # 오른쪽 test는 3을 받아서, 왼쪽 지역변수 test에는 4가 됨
vartest(3)
print(test) # 그런데 test는 없기 때문에 오류가 남
'''


#! 함수 안에서 함수 밖의 변수를 변경하는 방법
# ? 1. return 사용하기
a = 1


def vartest(a):
    a = a + 1
    return a


# vartest(a) # 이렇게만 쓰면 적용 안됨
a = vartest(a)
print(a)


#!? 2. global 명령어 사용하기, 권장하지 않음
b = 1


def vartest():
    global b
    b = b+1


vartest()
print(b)


# 문자열
c = "hello"


def vartest(c):
    c = c + 'hi'


vartest(c)
print(c)


#!? 헤깔릴 수 있는 것, mutable(리스트, 딕셔너리, 집합), immutable(정수, 실수, 문자열, 튜플)
d = [1, 2, 3]


def vartest(d):
    d.append(5)


vartest(d)
print(d)


#! lambda 예약어 - 패션 코딩
# 함수_이름 = lambda 매개변수1, 매개변수2, ... : 매개변수를_이용한_표현식
# 원래 함수
def add(a, b):
    return a + b


result = add(3, 4)
print(result)


# lambda 람다 활용
# add = lambda a, b: a+b
result = add(3, 4)
print(result)


# lambda 람다 활용2 - 함수 이름을 짓기 싫을 때
a = [lambda a, b: a+b, lambda a, b: a * b]
print(a[0](3, 4))
print(a[1](3, 4))
