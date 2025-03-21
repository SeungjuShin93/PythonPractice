# 문자열 관련 함수들


# 1. 문자 개수 세기 - count 함수로 문자열 중 문자 b의 개수를 리턴
print("1번 예제")
a = "hobby"
result = a.count('b')
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 2. 위치 알려 주기 1 - find
# find 함수로 문자열 중 문자 b가 처음으로 나온 위치를 반환
# 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환
a = "Python is the best choice"
result = a.find('b')
print(result)
result = a.find('k')
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 3. 위치 알려 주기 2 - index
# index 함수로 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환
# 만약 찾는 문자나 문자열이 존재하지 않는다면 오류가 발생
a = "Life is too short"
result = a.index('t')
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)
# result = a.index('k') # 오류 발생
# print(result)

# 4. 문자열 삽입 - join
result = ",".join('abcd')
print(result)
result = "-".join('abcd')
print(result)
result = ",".join(['a', 'b', 'c', 'd'])
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 5. 소문자를 대문자로 바꾸기 - upper
a = "hi"
result = a.upper()
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 6. 대문자를 소문자로 바꾸기 - lower
a = "HI"
result = a.lower()
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 7. 왼쪽 공백 지우기 - lstrip
a = " hi "
result = a.lstrip()
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 8. 오른쪽 공백 지우기 - rstrip
a = " hi "
result = a.rstrip()
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 9. 양쪽 공백 지우기 - strip
a = " hi "
result = a.strip()
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 10. 문자열 바꾸기 - replace
a = "Life is too short"
result = a.replace("Life", "Your leg")
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 11. 문자열 나누기 - split
# split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면
# 공백([Space], [Tab], [Enter])을 기준으로 문자열을 나누어 준다
a = "Life is too short"
result = a.split()
print(result)

# 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는
# 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다
b = "a:b:c:d"
result = b.split(':')
print(result)
print("=" * 25 + " 구분선 " + "=" * 25)

# 12. 착각하기 쉬운 문자열 함수
a = 'hi'
result = a.upper()
# print(result) # 결과는 "HI" 인데,
# print(a) # 의 결과는 ? "hi" or "HI"

# a의 값을 "HI" 자체로 변경하게 하려면?
# a = a.upper()
