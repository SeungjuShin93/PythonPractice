from copy import copy
# 자료형의 값을 저장하는 공간, 변수

# 변수, 주소:2026043360, a
# 메모리, 주소:2026043360, 값: 1 (객체)

# =는 (assignment) 할당의 개념

# 변수란?
a = [1, 2, 3]
print(id(a))  # 2502916612992
# id는 주소값을 보는 함수

#! 리스트를 복사하고자 할 때
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

#  동일한 객체를 가리키고 있는지에 대해서 판단하는 파이썬 명령어 is
print(a is b)

a[1] = 4
print(a)
print(b)  # b도 [1, 4, 3] 이 나옴

#! b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 만들 수는 없을까?
# 1. [:] 이용하기
# 리스트 전체를 가리키는 [:]을 사용해서 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 이용하기 - 최상단에 (from copy import copy) 추가
a = [1, 2, 3]
b = copy(a)
print(b)
print(b is a)  # False


# 3. copy 함수 사용하기
# 리스트 자료형의 자체 함수인 copy 함수를 사용해도 copy 모듈을 사용하는 것과 동일한 결과
a = [1, 2, 3]
b = a.copy()
print(b is a)  # False

#! 변수를 만드는 여러 가지 방법
# ? 튜플로 a, b에 값을 대입
# a = 'python'
# b = 'life'
# 위 처럼 만들기 귀찮으니 아래 처럼 만들 수 있음
(a, b) = 'python', 'life'
print(a, b)
# 튜플은 괄호 생략 가능
a, b = ('python', 'life')
print(a, b)
print(type(a))

# ? 리스트로 변수를 만들 수 있음
[a, b] = ['python', 'life']

# ? 같은 값을 넣고 싶을 때 아래 처럼 가능
a = b = 'python'

# ? 두 변수의 값을 매우 간단하게 바꿀 수 있음
# 다른언어는 temp를 만들어서 해야 함, 파이썬에서 제공하는 매우 편리한 기능
a = 3
b = 5
a, b = b, a
print(a, b)
