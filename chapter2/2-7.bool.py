# 불 자료형
# 불 자료형은 어떻게 사용할까?
a = True
b = False
print(type(a))
print(type(a))

a = 1 == 1
print(a)
a = 1 == 2
print(a)
a = 1 > 2
print(a)
a = 1 < 2
print(a)

#! 📌 파이썬에서 True(참)와 False(거짓)으로 평가되는 값들
# 문자열 (빈 문자열 제외)
print(bool("python"))  # ✅ True
print(bool(""))        # ❌ False

# 리스트 (빈 리스트 제외)
print(bool([1, 2, 3]))  # ✅ True
print(bool([]))         # ❌ False

# 튜플 (빈 튜플 제외)
print(bool((1, 2, 3)))  # ✅ True
print(bool(()))         # ❌ False

# 딕셔너리 (빈 딕셔너리 제외)
print(bool({'a': 1}))  # ✅ True
print(bool({}))        # ❌ False

# 숫자 (0 제외)
print(bool(1))  # ✅ True
print(bool(0))  # ❌ False

# None 값 (항상 False)
print(bool(None))  # ❌ False

if "python":
    print("문자열이 비어있지 않음!")  # 실행됨

if not []:
    print("빈 리스트는 거짓!")  # 실행됨


a = [1, 2, 3, 4]
while a:
    print(a)
    print(a.pop())
