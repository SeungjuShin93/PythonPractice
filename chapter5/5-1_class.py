#! 계산기 프로그램을 만들며 클래스 알아보기
result = 0


def add(num):
    global result
    result += num  # 결괏값(result)에 입력값(num) 더하기
    return result  # 결괏값 리턴


print(add(3))
print(add(4))


#
# calculator2.py
result1 = 0
result2 = 0


def add1(num):  # 계산기1
    global result1
    result1 += num
    return result1


def add2(num):  # 계산기2
    global result2
    result2 += num
    return result2


print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


#
# calculator3.py
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))


#
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result


#! 클래스와 객체
class Cookie:
    pass


a = Cookie()
b = Cookie()


#! 사칙 연산 클래스 만들기
a = FourCal()
a.setdata(4, 2)
a.add()
a.mul()
a.sub()
a.div()


#! 클래스 구조 만들기
class FourCal:
    pass


a = FourCal()
type(a)


#! 객체에 연산할 숫자 지정하기
a.setdata(4, 2)


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


def setdata(self, first, second):   # 메서드의 매개변수
    self.first = first              # 메서드의 수행문
    self.second = second


#! setdata 메서드의 매개변수
a = FourCal()
a.setdata(4, 2)

#! 메서드를 호출하는 또 다른 방법
a = FourCal()
FourCal.setdata(a, 4, 2)

a = FourCal()
a.setdata(4, 2)

#! setdata 메서드의 수행문


def setdata(self, first, second):   # 메서드의 매개변수
    self.first = first              # 메서드의 수행문
    self.second = second            # 메서드의 수행문


self.first = 4
self.second = 2

a = FourCal()
a.setdata(4, 2)
a.first
4
a.second
2

a = FourCal()
b = FourCal()

a.setdata(4, 2)
a.first

b.setdata(3, 7)
b.first

a.first


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second


#! 더하기 기능 만들기
a = FourCal()
a.setdata(4, 2)
a.add()


class FourCal:
    def setdata(self, first, second):
        self.first = first
    self.second = second

    def add(self):
        result = self.first + self.second
        return esult


a = FourCal()
a.setdata(4, 2)

a.add()


def add(self):
    result = self.first + self.second
    return result


result = self.first + self.second

result = a.first + a.second

a.add()


#! 곱하기, 빼기, 나누기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
a.add()

a.mul()

a.sub()

a.div()

b.add()

b.mul()

b.sub()
b.div()
0.


#! 생성자
a = FourCal()
a.add()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 6, in add
# AttributeError: 'FourCal' object has no attribute 'first'


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

#


def __init__(self, first, second):
    self.first = first
    self.second = second


#
a = FourCal()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'


a = FourCal(4, 2)


a = FourCal(4, 2)
a.first
a.second


a = FourCal(4, 2)
a.add()
a.div()


#!  클래스의 상속
class MoreFourCal(FourCal):
    pass


a = MoreFourCal(4, 2)
a.add()
a.mul()
a.sub()
a.div()


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


a = MoreFourCal(4, 2)
a.pow()
a.add()


#! 메서드 오버라이딩
a = FourCal(4, 0)
a.div()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     result = self.first / self.second
# ZeroDivisionError: division by zero


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second


a = SafeFourCal(4, 0)
a.div()


#! 클래스변수
class Family:
    lastname = "김"


Family.lastname

a = Family()
b = Family()
a.lastname
b.lastname

Family.lastname = "박"
a.lastname
b.lastname


#! 클래스변수와 동일한 이름의 객체변수를 생성하면?
a.lastname = "최"
a.lastname
Family.lastname
b.lastname
