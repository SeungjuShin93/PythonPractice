# 집합 자료형
# 집합(set)은 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형

#! 집합 자료형은 어떻게 만들까?
s1 = set([1, 2, 3])  # 리스트를, set이라는 함수로 감쌌음
print(type(s1))
print(s1)
# set([1,2,3])과 {1,2,3} 은 같음
s1 = {1, 2, 3}
print(type(s1))
print(s1)

# 문자열을 입력하여 만들 수도 있다
s2 = set("Hello")
print(type(s2))
print(s2)  # {'l', 'e', 'H', 'o'}
# 결과가 왜 이상하지? => 중복을 허용하지 않는다.
# 순서가 없다(Unordered).
# ? set은 중복을 허용하지 않는 특징 때문에 데이터의 중복을 제거하기 위한 필터로 종종 사용된다.

# set 자료형에 저장된 값을 인덱싱으로 접근 불가능
#! 만약 set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후에 해야 한다.
s1 = set([1, 2, 3])
l1 = list(s1)
print(l1)
print(l1[0])
t1 = tuple(s1)
print(t1)
print(t1[0])

#! 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
# s1 & s2 와 s1.intersection(s2)는 동일 함
print(s1.intersection(s2))

#! 합집합 구하기
print(s1 | s2)
# s1 | s2 와 s1.union(s2)는 동일 함
print(s1.union(s2))

#! 차집합 구하기
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))

#! 집합 자료형 관련 함수
# 값 1개 추가하기 - add
s1 = set([1, 2, 3])
print(s1)
s1.add(4)
print(s1)

#! 값 여러 개 추가하기 - update
s1 = set([1, 2, 3])
print(s1)
s1.update([4, 5, 6])
print(s1)
# 아래 결과는? 퀴즈 - 중복 적용 X
s1.update([4, 4, 4, 5, 5, 6])
print(s1)
# 아래 결과는? 퀴즈
# s1.add([4, 4, 4, 5, 5, 6]) #? TypeError: unhashable type: 'list'

#! 특정 값 제거하기 - remove
s1 = set([1, 2, 3])
print(s1)
s1.remove(2)  # % 주의, 인덱스가 아니라 2를 말함
print(s1)

# 참고
li = [1, 2, 2, 3, 3, 3, 3, 4]
# 리스트에서 중복을 제거하고 싶으면 아래 처럼 활용 가능
li = list(set(l1))
print(li)  # [1, 2, 3], 근데 순서가 완전 보장되는 건 아님 (대부분 유지)
