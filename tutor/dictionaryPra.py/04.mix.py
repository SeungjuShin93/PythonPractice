# 과일 가게 정보 (가격만 저장)
fruit_shop = {
    "사과": 1000,
    "배": 1500,
    "귤": 800,
    "포도": 2000,
    "복숭아": 1200
}

# 플레이어 정보 (딕셔너리로 잔액, 구매한 과일 정보 관리)
player = {
    "잔액": 5000,  # 시작 잔액
    "구매한 과일": []
}

# 게임 시작
print("과일 가게에 오신 것을 환영합니다.")
print("현재 잔액:", player["잔액"])
print("\n과일 목록:")

# 과일 목록 출력
fruit_names = list(fruit_shop.keys())  # 과일 이름을 리스트로
fruit_prices = list(fruit_shop.values())  # 과일 가격을 리스트로

# 과일 이름과 가격 출력
for i in range(len(fruit_names)):
    print(f"{fruit_names[i]}: {fruit_prices[i]}원")

#! fruit_shop.items()를 사용하여 과일 이름과 가격을 한 번에 가져옴
# for fruit, price in fruit_shop.items():
#     print(f"{fruit}: {price}원")

# 과일 구매 루프
# 현재 구매한 과일, 남은잔액 표시, 입력을 받음
# 종료시 while문 종료, 존재하지 않은 과일일 때 continue
# 있는 과일이라면, 그 과일의 가격에 대한 변수와 가격
# 잔액이 부족한 경우 처리
# 구매에 성공했다면 -> 잔액 차감, 구매한과일 추가
# 구매 완료 문구 출력
while True:
    print("\n현재 구매한 과일:", player["구매한 과일"])
    print("남은 잔액:", player["잔액"])

    # 플레이어 입력 받기
    choice = input("\n구매할 과일 이름을 입력하세요 (종료하려면 '종료' 입력): ")

    if choice == "종료":
        print("과일 가게를 떠납니다. 게임 종료.")
        break

    if choice not in fruit_shop:
        print("존재하지 않는 과일입니다. 다시 입력하세요.")
        continue

    fruit_price = fruit_shop[choice]

    if player["잔액"] < fruit_price:
        print("잔액이 부족합니다. 다른 과일을 선택하세요.")
        continue

    # 과일 구매 처리
    player["잔액"] -= fruit_price
    player["구매한 과일"].append(choice)

    print(f"{choice}을(를) 구매했습니다.")

print("\n게임이 끝났습니다. 구매한 과일 목록:")
for fruit in player["구매한 과일"]:
    print(f"- {fruit}")

print("남은 잔액:", player["잔액"])
