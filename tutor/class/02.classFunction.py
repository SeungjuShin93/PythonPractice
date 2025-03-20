# 딕셔너리와 함수를 활용하면 조금 더 깔끔해짐

# 챔피언 생성 함수
def create_champion(name, hp, damage):
    print(f"{name}이(가) 생성되었습니다! (체력: {hp}, 공격력: {damage})")
    return {"name": name, "hp": hp, "damage": damage}

# 공격 함수


def attack(champ, target):
    print(f"{champ['name']}이(가) {target}을(를) 기본 공격합니다! [공격력 {champ['damage']}]")


# yone_name = "요네"
# yone_hp = 550
# yone_damage = 65
# malphite_name = "말파이트"
# malphite_hp = 800
# malphite_damage = 70
# pyke_name = "파이크"
# pyke_hp = 600
# pyke_damage = 68
# 챔피언 생성
yone = create_champion("요네", 550, 65)
malphite = create_champion("말파이트", 800, 70)
pyke = create_champion("파이크", 600, 68)
print("-" * 30)  # 구분선

# 요네 행동
attack(yone, "적 챔피언")
print("-" * 30)  # 구분선

# 말파이트 행동
attack(malphite, "미니언")
print("-" * 30)  # 구분선

# 파이크 행동
attack(pyke, "적팀 서포터")
print("-" * 30)  # 구분선
