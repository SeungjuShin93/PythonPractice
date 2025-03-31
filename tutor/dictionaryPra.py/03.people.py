# 사람 정보 딕셔너리
people = {
    "홍길동": {
        "키": 175,
        "몸무게": 70,
        "취미": "축구",
        "좋아하는 과목": "수학",
        "특기": "노래"
    },
    "김철수": {
        "키": 160,
        "몸무게": 55,
        "취미": "독서",
        "좋아하는 과목": "영어",
        "특기": "글쓰기"
    },
    "이영희": {
        "키": 165,
        "몸무게": 60,
        "취미": "영화 감상",
        "좋아하는 과목": "과학",
        "특기": "춤"
    }
}


# keys()를 사용해 사람들의 이름 출력
print("사람들의 이름:")
for name in people.keys():
    print(name)

# values()를 사용해 사람들의 정보 출력
print("\n사람들의 정보:")
for info in people.values():
    print(
        f"키: {info['키']}cm, 몸무게: {info['몸무게']}kg, 취미: {info['취미']}, 좋아하는 과목: {info['좋아하는 과목']}, 특기: {info['특기']}")


# 사람 정보 출력
for name, info in people.items():
    print(f"{name}:")
    print(f"  키: {info['키']}cm")
    print(f"  몸무게: {info['몸무게']}kg")
    print(f"  취미: {info['취미']}")
    print(f"  좋아하는 과목: {info['좋아하는 과목']}")
    print(f"  특기: {info['특기']}\n")
