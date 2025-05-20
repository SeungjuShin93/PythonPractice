# 문제 1: 두 수의 합 구하기
num1 = int(input())
num2 = int(input())
print(num1 + num2)

# 입력 예시:
# 5
# 3
# 출력: 8

# 문제 2: 더 긴 문자열 찾기
str1 = input()
str2 = input()

if len(str1) > len(str2):
    print(str1)
else:
    print(str2)

# 입력 예시:
# HelloWorld
# Programmingisfun
# 출력: Programmingisfun

# 문제 3: 거꾸로 된 직각 삼각형 출력
n = int(input())
for i in range(n, 0, -1):
    print('*' * i)

# 입력: 5
# 출력:
# *****
# ****
# ***
# **
# *

# 다른 풀이
n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# 문제 4: 큰따옴표 붙이기
string = input()
print(f'"{string}"')

# 입력: HelloWorld
# 출력: "HelloWorld"

# 다른 풀이
str1 = input()
print('"' + str1 + '"')

# 문제 5: 절댓값 출력
num = int(input())
print(abs(num))

# 입력: -13
# 출력: 13

# 다른 풀이
num1 = int(input())
if num1 < 0:
    print(-num1)
    # num1 = -num1
    # num1 * -1
else:
    print(num1)

# 문제 6: 두 수 비교 (같으면 합, 다르면 차)
a = int(input())
b = int(input())
if a == b:
    print(a + b)
else:
    # print(abs(a - b))
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)

# 입력: 7, 10
# 출력: 3

# 문제 7: 1부터 n까지 출력
n = int(input())
for i in range(1, n + 1):
    print(i)

# 입력: 5
# 출력:
# 1
# 2
# 3
# 4
# 5

# 문제 8: 인접한 수의 차 출력
n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 1):
    print(arr[i] - arr[i + 1])

# 입력:
# 4
# 1 3 6 2
# 출력:
# -2
# -3
# 4

# 다른풀이 map 안쓰고
n = int(input())  # 숫자의 개수 입력
input_line = input()  # 한 줄로 된 숫자들 입력
str_numbers = input_line.split()  # 공백 기준으로 나누기

# 숫자들을 정수로 하나씩 바꿔서 리스트에 담기
arr = []
for s in str_numbers:
    arr.append(int(s))

# 인접한 두 수의 차 출력
for i in range(n - 1):
    print(arr[i] - arr[i + 1])

# 다른풀이 2 split를 모른 경우
n = int(input())  # 숫자의 개수 입력
arr = []  # 숫자를 저장할 리스트

# 숫자들을 한 줄씩 입력받기
for _ in range(n):
    num = int(input())  # 숫자 하나 입력
    arr.append(num)

# 인접한 두 수의 차 출력
for i in range(n - 1):
    print(arr[i] - arr[i + 1])


# 문제 9: 숫자 거꾸로 출력
n = input()
print(n[::-1])

# 입력: 12345
# 출력: 54321

# 문제 9: 다른 풀이 - 숫자 거꾸로 출력 (슬라이싱 없이)
n = input()      # 문자열로 숫자 입력
reversed_n = ''  # 거꾸로 저장할 문자열 변수

for ch in n:
    reversed_n = ch + reversed_n  # 앞쪽에 붙이기

print(reversed_n)


# 문제 10: 문자열에서 '1'의 개수 세기
s = input()
print(s.count('1'))

# 입력: 4156721

# 출력: 2

# 다른 풀이
s = input()  # 문자열 입력
count = 0    # '1'의 개수를 저장할 변수

for ch in s:
    if ch == '1':
        count += 1

print(count)
