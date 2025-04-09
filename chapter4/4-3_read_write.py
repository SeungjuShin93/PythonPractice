# # 파일 읽고 쓰기

# # '''
# # 파일_객체 = open(파일_이름, 파일_열기_모드)

# # r	읽기 모드: 파일을 읽기만 할 때 사용한다.
# # w	쓰기 모드: 파일에 내용을 쓸 때 사용한다. (덮어 쓰기가 됨)
# # a	추가 모드: 파일의 마지막에 새로운 내용을 추가할 때 사용한다.
# # '''


# # 기본 구조
# f = open("새파일.txt", 'w')
# f.close()

# # 기존 디렉토리에 생성 - 상대 경로
# f = open("chapter4/새파일.txt", 'w')
# f.close()

# # 기존 디렉토리에 생성 - 절대 경로
# f = open("/Users/shins/OneDrive/Desktop/PythonWorkspace/chapter4/새파일2.txt", 'w')
# f.close()


# #! 참고
# '''
# 방법 1. /(슬래시) 쓰기 — 가장 간단하고 안전함
# 방법 2. 역슬래시 \ 두 번 쓰기
# 방법 3. 문자열 앞에 r 붙이기 (raw string) - 백슬래시와 r을 사용
# 방법 3 예시 - f = open(r"C:\새파일2.txt", 'w')
# '''


#! chapter4에 doit 폴더에 새파일 만들고 내용 쓰기
# 글자가 깨진 경우 - 인코딩이 깨짐
# f = open("/Users/shins/OneDrive/Desktop/PythonWorkspace/chapter4/doit/new.txt", 'w')
f = open("/Users/shins/OneDrive/Desktop/PythonWorkspace/chapter4/doit/new.txt",
         'w', encoding='UTF-8')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 반복되는 주소 변수로 만들기
file_path = "chapter4/doit/new.txt"


# #! 파일을 읽는 여러 가지 방법
# # ? readline 함수 이용하기
# f = open(file_path, 'r', encoding="UTF-8")
# line = f.readline()
# print(line)
# f.close()


# ? 여러 줄 읽기
# 한 줄씩 읽어 출력할 때 줄 끝에 \n 문자가 있으므로 빈 줄도 같이 출력됨.
# readline()은 더 이상 읽을 줄이 없을 경우, 빈 문자열('')을 리턴함
f = open(file_path, 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()


# ? 입력받기
# while True:
#     data = input()
#     if not data:
#         break
#     print(data)


#! readlines 함수 사용하기
# readlines 함수는 파일의 모든 줄을 읽어서 각각의 줄을 요소로 가지는 리스트를 리턴
f = open(file_path, 'r', encoding="UTF-8")
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()


#! 줄 바꿈(\n) 문자 제거하기
f = open(file_path, 'r', encoding="UTF-8")
lines = f.readlines()
for line in lines:
    line = line.strip()  # 줄 끝의 줄 바꿈 문자를 제거한다.
    # line = line.replace('\n', '')  # replace 도 활용 가능
    print(line)
f.close()


#! read 함수 사용하기
# f.read()는 파일의 내용 전체를 문자열로 리턴
# read.py
f = open(file_path, 'r', encoding="UTF-8")
data = f.read()
print(data)
f.close()


#! 파일 객체를 for 문과 함께 사용하기
# 파일 객체(f)는 기본적으로 위와 같이 for 문과 함께 사용하여 파일을 줄 단위로 읽을 수 있음
f = open(file_path, 'r', encoding="UTF-8")
for line in f:
    print(line)
f.close()


#! 파일에 새로운 내용 추가하기
# 쓰기 모드('w')로 파일을 열 때 이미 존재하는 파일을 열면 그 파일의 내용이 모두 사라지게 된다. 하지만 원래 있던 값을 유지하면서 단지 새로운 값만 추가해야 할 경우도 있다. 이런 경우에는 파일을 추가 모드('a')로 열면 된다
f = open(file_path, 'a', encoding="UTF-8")
for i in range(11, 20):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()


#! with 문과 함께 사용하기
# 파일을 열면(open) 항상 닫아(close) 주어야 한다. 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 파이썬의 with 문이 바로 이런 역할
# as f에서 f는 지역변수
with open(file_path, "w") as f:
    f.write("Life is too short, you need python")
