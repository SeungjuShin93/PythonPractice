# 주어진 상황에서 반복 -> while
# 여러개의 리스트, 문자열 등에서 뽑아서 쓸때 -> for

# 1. 전형적인 for 문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)


# 2. for 문의 응용
marks = [90, 25, 67, 45, 80]   # 학생들의 시험 점수 리스트

number = 0   # 학생에게 붙여 줄 번호
for mark in marks:   # 90, 25, 67, 45, 80을 순서대로 mark에 대입
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# 4. for 문과 continue 문
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# 5. for 문과 함께 자주 사용하는 range 함수
a = range(10)  # range(10)은 0부터 10 미만의 숫자를 포함하는 range 객체
print(a)

# range 함수의 예시 살펴보기
add = 0
for i in range(1, 11):
    add = add + i

print(add)

# 4번과 동일
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

# for와 range를 이용한 구구단2
for i in range(1, 10):        # 1번 for문
    for j in range(2, 10):   # 2번 for문
        if (j*i < 10):
            print(j*i, end="  ")
        else:
            print(j*i, end=" ")
    print('')

# for와 range를 이용한 구구단3
for i in range(2, 10):
    print(f"{i}단 시작")
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print('')

# 리스트 컴프리헨션 사용하기 - 패션코딩, 실전에서 아예 안써도 됨
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

# 위의 코드를 아래 코드로 멋있?게 쓸 수 있음
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print(result)

# 또 다른 예제
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# 또 다른 예제2
result = [x*y for x in range(2, 10)
          for y in range(1, 10)]
print(result)
'''
result = []
fox x in range(2,10):
  for y in range(1,10):
    result.append(x*y)
'''
