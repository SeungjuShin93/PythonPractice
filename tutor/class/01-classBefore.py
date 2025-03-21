# 요네 챔피언 정보
yone_name = "요네"
yone_hp = 550
yone_damage = 65

# 말파이트 챔피언 정보
malphite_name = "말파이트"
malphite_hp = 800
malphite_damage = 70

# 파이크 챔피언 정보
pyke_name = "파이크"
pyke_hp = 600
pyke_damage = 68


# 챔피언 생성 메시지 출력
print(f"{yone_name}이(가) 생성되었습니다! (체력: {yone_hp}, 공격력: {yone_damage})")
print(f"{malphite_name}이(가) 생성되었습니다! (체력: {malphite_hp}, 공격력: {malphite_damage})")
print(f"{pyke_name}이(가) 생성되었습니다! (체력: {pyke_hp}, 공격력: {pyke_damage})")
print("-" * 30)  # 구분선


# 공격 사용 함수
def attack(name, damage, target):
    print(f"{name}이(가) {target}을(를) 기본 공격합니다! [공격력 {damage}]")


# 요네 행동
attack(yone_name, yone_damage, "적 챔피언")
print("-" * 30)  # 구분선


# 말파이트 행동
attack(malphite_name, malphite_damage, "미니언")
print("-" * 30)  # 구분선

# 파이크 행동
attack(pyke_name, pyke_damage, "적팀 서포터")
print("-" * 30)  # 구분선
