# 챔피언 생성 함수
def create_champion(name, hp, damage, q, w, e, r):
    print(f"{name}이(가) 생성되었습니다! (체력: {hp}, 공격력: {damage})")
    return {"name": name, "hp": hp, "damage": damage, "skills": {"Q": q, "W": w, "E": e, "R": r}}

# 공격 및 스킬 사용 함수


def attack(champ, target):
    print(f"{champ['name']}이(가) {target}을(를) 기본 공격합니다! [공격력 {champ['damage']}]")


def use_skill(champ, key, target):
    if key in champ["skills"]:
        print(
            f"{champ['name']}이(가) {target}에게 '{champ['skills'][key]}' 스킬을 사용합니다!")
    else:
        print(f"{champ['name']}에게 해당 키({key})의 스킬이 없습니다.")


# 챔피언 생성
malphite = create_champion("말파이트", 800, 70, "지진의 파편",
                           "천둥 소리", "지면 강타", "멈출 수 없는 힘")
yone = create_champion("요네", 550, 65, "몰아치는 강풍", "영혼 가르기", "운명의 길", "운명 봉인")
pyke = create_champion("파이크", 600, 68, "뼈 작살", "유령 잠수", "망자의 물살", "깊은 바다의 처형")
print("-" * 30)  # 구분선

# 요네 행동
attack(yone, "적 챔피언")
use_skill(yone, "Q", "적 챔피언")
use_skill(yone, "W", "적 챔피언")
use_skill(yone, "E", "적 챔피언")
use_skill(yone, "R", "적 챔피언")
print("-" * 30)  # 구분선

# 말파이트 행동
attack(malphite, "미니언")
use_skill(malphite, "Q", "적팀 원딜")
use_skill(malphite, "W", "적팀 원딜")
use_skill(malphite, "E", "적팀 원딜")
use_skill(malphite, "R", "적팀 원딜")
print("-" * 30)  # 구분선

# 파이크 행동
attack(pyke, "적팀 서포터")
use_skill(pyke, "Q", "적팀 서포터")
use_skill(pyke, "W", "적팀 서포터")
use_skill(pyke, "E", "적팀 서포터")
use_skill(pyke, "R", "적팀 서포터")
print("-" * 30)  # 구분선
