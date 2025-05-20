# 리스트의 짝수 번째 숫자 더하기
arr = [10, 1, 30, 2, 50, 3, 70, 4]
result = 0
new_arr = arr[1::2]
print(new_arr)
for char in new_arr:
    result += char
print(result)

# 주어진 코드가 다르다면
result = 0
for i in range(1, len(arr), 2):
    result += arr[i]
print(result)

# 또 다르다면
result = 0
for i in range(len(arr)):
    if i % 2 == 1:
        result += arr[i]
print(result)

# 다른 예제
result = 0
for i in range(1, len(arr) + 1):
    if (i + 1) % 2 == 0:
        result += arr[i]
print(result)


# 소문자의 갯수
str1 = "HelloWorld"
count = 0

for i in range(0, len(str1)):
    if str1[i].islower():
        count += 1

print(count)

# 특수문자 출력
str1 = "apple"
str2 = "banana"
print(str1 + "%" + str2)
print(f'{str1}&{str2}')

print("!@#$%^&*()")


# 두 문자열 중 영어사전 순으로 뒤에 오는 문자열
str1 = 'apple'
str2 = 'banana'
print(str1 if str1 > str2 else str2)

# 한 글자씩 증가하는 문자열
str1 = 'apple'
for i in range(0, len(str1)):
    for j in range(i + 1):
        print(str1[j], end="")
    print(end=" ")
print()

result = ""
for i in range(0, len(str1)):
    result += str1[i]
    print(result, end=" ")
print()
# k에 3씩 더하여 작은 순으로 n개
k = 7
n = 10

result = k
for i in range(n):
    print(result + (i * 3), end=" ")
print()

# 7보다 이전에 있는 숫자의 갯수
# index 함수를 아느냐?
arr = [10, 20, 30, 40, 50, 7, 60, 70, 80, 90]
print(arr.index(7))

# index 함수 기억 안 난다면
count = 0
for char in arr:
    if char == 7:
        print(count)
        break
    else:
        count += 1
print(count)

# in range가 기억이 났다면
count = 0
for i in range(0, len(arr)):
    if arr[i] == 7:
        print(count)
        break
    else:
        count += 1
print(count)

# 숫자 두개, 더 작은 수
num1 = 20
num2 = 30
if num1 > num2:
    print(num1)
else:
    print(num2)

# - * 교차 출력
n = 5
for i in range(n):
    print((n - i) * "*" + (i + 1) * "-", end="")

# 두 수의 절대값 출력
num1 = 20
num2 = 30
print(abs(num1 - num2))
