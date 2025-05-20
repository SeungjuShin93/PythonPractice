import random  # 파이썬 표준 라이브러리에 포함된 "모듈

주사위 = random.randint(1, 6)
print("주사위 눈:", 주사위)

친구들 = ["지민", "현우", "수아", "윤호"]
당첨자 = random.choice(친구들)

print("오늘의 당번은:", 당첨자)
