'''
__init__()은 생성자(constructor).
객체가 생성될 때 자동으로 실행되는 함수.
주로 객체의 **초기값(속성)**을 설정할 때 사용.
'''


class Champion:
    def __init__(self, , , ):
        self. =
        self. =
        self. =
        print(f"{self.}이(가) 생성되었습니다! (체력: {self.}, 공격력: {self.})")

    def attack(, ):
        print(f"{}이(가) {}을(를) 기본 공격합니다! [공격력 {}]")


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
yone = Champion("", , )
malphite = Champion("", , )
pyke = Champion("", , )
print("-" * 30)  # 구분선

# 요네 행동
yone.attack("적 챔피언")
print("-" * 30)  # 구분선

# 말파이트 행동
malphite.attack("미니언")
print("-" * 30)  # 구분선

# 파이크 행동
pyke.attack("적팀 서포터")
print("-" * 30)  # 구분선
