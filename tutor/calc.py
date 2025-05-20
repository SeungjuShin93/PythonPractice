def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0으로 나눌 수 없습니다."


num1 = int(input("첫 번째 수 입력 : "))
num2 = int(input("두 번째 수 입력 : "))
print(f"결과는 : {add(num1, num2)}")
# print("결과는 : ", add(num1, num2))


# a = int(input("첫 번째 수 입력: "))
# c = input("연산자 입력 (+, -, *, /): ")
# b = int(input("두 번째 수 입력: "))

# if c == "+":
#     result = add(a, b)
# elif c == "-":
#     result = subtract(a, b)
# elif c == "*":
#     result = multiply(a, b)
# elif c == "/":
#     result = divide(a, b)
# else:
#     result = "올바른 연산자를 입력하세요."

# print("결과:", result)
