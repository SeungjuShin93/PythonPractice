'''
__init__()은 생성자(constructor).
객체가 생성될 때 자동으로 실행되는 함수.
주로 객체의 **초기값(속성)**을 설정할 때 사용.
'''


# 챔피언 클래스 정의
class Champion:
    def __init__(self, name, hp, damage, q, w, e, r):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.skills = {"Q": q, "W": w, "E": e, "R": r}
        print(f"{self.name}이(가) 생성되었습니다! (체력: {self.hp}, 공격력: {self.damage})")

    def attack(self, target):
        print(f"{self.name}이(가) {target}을(를) 기본 공격합니다! [공격력 {self.damage}]")

    def use_skill(self, key, target):
        if key in self.skills:
            print(
                f"{self.name}이(가) {target}에게 '{self.skills[key]}' 스킬을 사용합니다!")
        else:
            print(f"{self.name}에게 해당 키({key})의 스킬이 없습니다.")


# 챔피언 생성
malphite = Champion("말파이트", 800, 70, "지진의 파편", "천둥 소리", "지면 강타", "멈출 수 없는 힘")
yone = Champion("요네", 550, 65, "몰아치는 강풍", "영혼 가르기", "운명의 길", "운명 봉인")
pyke = Champion("파이크", 600, 68, "뼈 작살", "유령 잠수", "망자의 물살", "깊은 바다의 처형")
print("-" * 30)  # 구분선

# 요네 행동
yone.attack("적 챔피언")
yone.use_skill("Q", "적 챔피언")
yone.use_skill("W", "적 챔피언")
yone.use_skill("E", "적 챔피언")
yone.use_skill("R", "적 챔피언")
print("-" * 30)  # 구분선

# 말파이트 행동
malphite.attack("미니언")
malphite.use_skill("Q", "적팀 원딜")
malphite.use_skill("W", "적팀 원딜")
malphite.use_skill("E", "적팀 원딜")
malphite.use_skill("R", "적팀 원딜")
print("-" * 30)  # 구분선

# 파이크 행동
pyke.attack("적팀 서포터")
pyke.use_skill("Q", "적팀 서포터")
pyke.use_skill("W", "적팀 서포터")
pyke.use_skill("E", "적팀 서포터")
pyke.use_skill("R", "적팀 서포터")
print("-" * 30)  # 구분선
