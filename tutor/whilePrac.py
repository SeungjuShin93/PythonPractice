# 말파이트의 공격력
malphite_attacks = {
    "기본공격": 10,
    "지진의파편": 70,
    "천둥소리": 30,
    "지면강타": 50,
    "멈출수없는힘": 100
}

# 요네의 체력
yone_health = 200

# 전투 시작
while yone_health > 0:
    # 공격 선택
    attack = input(
        "어떤 공격을 하실건가요?\n(기본공격, 지진의파편, 천둥소리, 지면강타, 멈출수없는힘): ").strip()

    # 선택한 공격이 맞는지 확인
    if attack in malphite_attacks:
        yone_health -= malphite_attacks[attack]
        if yone_health < 0:
            yone_health = 0
        print(
            f"{attack}[공격력 : {malphite_attacks[attack]}]으로 요네를 공격하였습니다!\n현재 남아있는 요네의 체력은 {yone_health}입니다.\n")
    else:
        print("잘못 입력하였습니다. 다시 입력해주세요.")
        continue

    # 요네의 체력이 0 이하이면 전투 종료
    if yone_health <= 0:
        print("요네가 전사하였습니다! 전투 종료!")
        break


'''
동영상 제공
말파이크의 공격을 딕셔너리 형태로 만듬
key 값에 "기본공격"
value에 10

이런식으로

지진의파편 - 70
천둥소리 - 30
지면강타 - 50
멈출수없는힘 - 100

설정

요네체력 설정 - 200

요네가 죽을때까지
input으로 원하는 공격을 입력
해당 공격을 받으면 요네는 체력이 깎임
0이하가 되면 종료

5가지 공격 이외의 것을 입력하면
다시 입력하라는 메세지 출력

(추가 미션 - 어려우면 포기)
혹여나 체력이 20인데 멈출수없는힘을 맞으면 체력이 -80이 되는데 이럴경우에는 체력이 0으로 표시
'''
