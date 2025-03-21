# 요네 정보
yone_name = "요네"
yone_hp = 550
yone_damage = 65
yone_q = "몰아치는 강풍"
yone_w = "영혼 가르기"
yone_e = "운명의 길"
yone_r = "운명 봉인"

# 말파이트 정보
malphite_name = "말파이트"
malphite_hp = 800
malphite_damage = 70
malphite_q = "지진의 파편"
malphite_w = "천둥 소리"
malphite_e = "지면 강타"
malphite_r = "멈출 수 없는 힘"

# 파이크 정보
pyke_name = "파이크"
pyke_hp = 600
pyke_damage = 68
pyke_q = "뼈 작살"
pyke_w = "유령 잠수"
pyke_e = "망자의 물살"
pyke_r = "깊은 바다의 처형"

# 챔피언 생성 메시지 출력
print(f"{malphite_name}이(가) 생성되었습니다! (체력: {malphite_hp}, 공격력: {malphite_damage})")
print(f"{yone_name}이(가) 생성되었습니다! (체력: {yone_hp}, 공격력: {yone_damage})")
print(f"{pyke_name}이(가) 생성되었습니다! (체력: {pyke_hp}, 공격력: {pyke_damage})\n")
print("-" * 30)  # 구분선

# 공격 및 스킬 사용 함수


def attack(name, damage, target):
    print(f"{name}이(가) {target}을(를) 기본 공격합니다! [공격력 {damage}]")


def use_skill(name, skill, target):
    print(f"{name}이(가) {target}에게 '{skill}' 스킬을 사용합니다!")


# 요네 행동
attack(yone_name, yone_damage, "적 챔피언")
use_skill(yone_name, yone_q, "적 챔피언")
use_skill(yone_name, yone_w, "적 챔피언")
use_skill(yone_name, yone_e, "적 챔피언")
use_skill(yone_name, yone_r, "적 챔피언")
print("-" * 30)  # 구분선

# 말파이트 행동
attack(malphite_name, malphite_damage, "미니언")
use_skill(malphite_name, malphite_q, "적팀 원딜")
use_skill(malphite_name, malphite_w, "적팀 원딜")
use_skill(malphite_name, malphite_e, "적팀 원딜")
use_skill(malphite_name, malphite_r, "적팀 원딜")
print("-" * 30)  # 구분선

# 파이크 행동
attack(pyke_name, pyke_damage, "적팀 서포터")
use_skill(pyke_name, pyke_q, "적팀 서포터")
use_skill(pyke_name, pyke_w, "적팀 서포터")
use_skill(pyke_name, pyke_e, "적팀 서포터")
use_skill(pyke_name, pyke_r, "적팀 서포터")
print("-" * 30)  # 구분선
