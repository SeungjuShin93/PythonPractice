# 친구 나이 딕셔너리
friend_ages = {
    "철수": 12,
    "영희": 11,
    "민수": 13
}

# keys()를 사용하여 친구 이름(키)만 출력
print("친구 이름들:")
for name in friend_ages.keys():
    print(name)

# values()를 사용하여 친구 나이만 출력
print("\n친구 나이들:")
for age in friend_ages.values():
    print(age)

# items()를 사용하여 친구 이름과 나이 출력
print("\n친구 이름과 나이:")
for name, age in friend_ages.items():
    print(f"{name}: {age}세")


# 전화번호부 딕셔너리
phone_book = {
    "엄마": "010-1234-5678",
    "아빠": "010-9876-5432",
    "친구": "010-5555-6666"
}

# keys()를 사용하여 전화번호부 이름만 출력
print("\n전화번호부 이름들:")
for name in phone_book.keys():
    print(name)

# values()를 사용하여 전화번호만 출력
print("\n전화번호부 전화번호들:")
for phone in phone_book.values():
    print(phone)

# items()를 사용하여 전화번호부 이름과 전화번호 출력
print("\n전화번호부 이름과 전화번호:")
for name, phone in phone_book.items():
    print(f"{name}: {phone}")


# 메뉴 가격 딕셔너리
menu = {
    "김밥": 3000,
    "라면": 4000,
    "떡볶이": 5000
}

# keys()를 사용하여 메뉴 이름만 출력
print("\n메뉴 이름들:")
for dish in menu.keys():
    print(dish)

# values()를 사용하여 메뉴 가격만 출력
print("\n메뉴 가격들:")
for price in menu.values():
    print(price)

# items()를 사용하여 메뉴 이름과 가격 출력
print("\n메뉴 이름과 가격:")
for dish, price in menu.items():
    print(f"{dish}: {price}원")
