# # 자판기 커피
# coffee = 5
# while True:
#     money = int(input("돈을 넣어 주세요: "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print(f"거스름돈 {money - 300}를 주고 커피를 줍니다.")
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print(f"남은 커피의 양은 {coffee}개 입니다.")
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break


print('출력')
print('출력2')


coffee = 3
coffee_price = 300
while True:
    money = int(input)
    if money == 300:
        print("커피를 줍니다")
        coffee -= 1
    elif money < 300:
        change = money -= coffee
        money -= coffee

        print("거스름돈을 주고 커피를 준다")
        coffee -= 1
    elif coffee == 0:
        print("커피가 다 떨어짐")

    else:
        print(f'{money}원을 다시 돌려준다')
