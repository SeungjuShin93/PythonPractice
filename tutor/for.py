
# print("2단 입니다.")
# print(2 * 1)
# print(2 * 2)
# print(2 * 3)
# print(2 * 4)
# print(2 * 5)
# print(2 * 6)
# print(2 * 7)
# print(2 * 8)
# print(2 * 9)
# print("3단 입니다.")
# print(3 * 1)

for i in range(2, 10):
    print(f"{i}단 입니다")
    for j in range(1, 10):
        print("%d * %d = %d" % (i, j, i*j))
