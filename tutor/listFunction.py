# 리스트 관련 함수
# 리스트에 요소 추가하기 - append
# append(x)는 리스트의 맨 마지막에 x를 추가하는 함수
a = [1, 2, 3]
a.append(4)
print(a)
# 아래와 같음
a = [1, 2, 3]
a += [4]
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트에 리스트 추가도 가능
a.append([5, 6])
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트 정렬 - sort, sort안에 어떤 알고리즘이 있을텐데 그걸 sort()로 실행
# 리스트의 요소를 순서대로 정렬해 준다.
a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a', 'c', 'b']
a.sort()
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트 뒤집기 - reverse
# 현재의 리스트를 그대로 거꾸로 뒤집음
a = ['a', 'c', 'b']
a.reverse()
print(a)

# 정렬을 하고 역순으로 정리하려면?
a.sort()
a.reverse()
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 인덱스 반환 - index
# index(x) 함수는 리스트에 x 값이 있으면 x의 인덱스 값(위칫값)을 리턴
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트에 요소 삽입 - insert
# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수
# append는 제일 뒤에 추가, insert는 원하는 인덱스에 추가
a = [1, 2, 3]
a.insert(0, 4)
# a.insert(1, 4)
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트 요소 제거 - remove
# remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
# a.remove(3) # 한 번 더 실행하면 다시 3이 삭제
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 퀴즈
# a = [1, 2, 3, 1, 2, 3] 을 뒤에서 3을 삭제하려면?
a = [1, 2, 3, 1, 2, 3]
a.reverse()
a.remove(3)
a.reverse()
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트 요소 끄집어 내기 - pop (리턴 값이 있음, 중요)
# pop()은 리스트의 맨 마지막 요소를 리턴하고 그 요소는 삭제
# pop(x)는 리스트의 x번째(인덱스) 요소를 리턴하고 그 요소는 삭제
a = [1, 2, 3]
print(a.pop())
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트에 포함된 요소 x의 개수 세기 - count
# count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 리턴
a = [1, 2, 3, 1]
print(a.count(1))
print("=" * 25 + " 구분선 " + "=" * 25)

# 리스트 확장 - extend
# extend(x)에서 x에는 리스트만 올 수 있으며 원래의 a 리스트에 x 리스트를 더함
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
print("=" * 25 + " 구분선 " + "=" * 25)

# 참고
# extend와 append의 차이
a = [1, 2, 3]
a.append([4, 5])
print(a)
# append는 [4, 5] 리스트가 추가,
# extend는 4와 5가 펼쳐져서 추가되었음

# 즉, a.extend[4,5]는 a += [4, 5]와 동일
