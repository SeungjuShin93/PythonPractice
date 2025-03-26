'''
튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.

리스트는 [], 튜플은 ()으로 둘러싼다.
리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.
'''
# Mutabel - (리스트, 딕셔너리, 집합)
# Immutable - (정수, 실수, 문자열, 튜플)

#! 튜플은 어떻게 만들까?
t1 = ()
print(t1)
print(type(t1))
# <class 'tuple'>

# 하나의 값만 적어도 , (콤마) 적어줘야 함
t2 = (1,)
print(t2)
print(type(t2))

# 괄호를 적는 것을 권장 (헤깔림)
t3 = (1, 2, 3)
print(t3)
print(type(t3))

# 괄호를 적지 않으면, 기본적으로 튜플로 됨
t4 = 1, 2, 3
print(t4)
print(type(t4))

# 튜플안에 또 다른 튜플이 들어갈 수 있음
t5 = ('a', 'b', ('ab', 'cd'))
print(t5)
print(type(t5))

#! 튜플의 요솟값을 지우거나 변경하려고 하면 어떻게 될까?
# 1. 튜플 요솟값을 삭제하려 할 때
t1 = (1, 2, 'a', 'b')
# del t1[0] #? TypeError: 'tuple' object doesn't support item deletion

# 2. 튜플 요솟값을 변경하려 할 때
t1 = (1, 2, 'a', 'b')
# t1[0] = 'c' #? TypeError: 'tuple' object does not support item assignment

#! 튜플 다루기
# 1. 인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 2. 슬라이싱하기
t1 = (1, 2, 'a', 'b')
print(t1[1:])
print(t1)  # 실제로 자르는 것이 아니라, 그 부분만 보여주는 것

# 3. 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2  # 새로운 튜플을 생성 (t1을 변형하는 게 아님), 실제 더하기는 안됨
# t1 = t1 + t2 는 가능, 새로운 튜플을 t1에 다시 대입
print(t3)

# 4. 튜플 곱하기
t3 = t2 * 3
t2 = (3, 4)
print(t3)  # 새로운 튜플을 대입

# 5. 튜플 길이 구하기
t1 = (1, 2, 'a', 'b')
print(len(t1))
