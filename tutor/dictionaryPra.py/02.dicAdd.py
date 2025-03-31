friend_ages = {
    "철수": 12,
    "영희": 11,
    "민수": 13
}

# 새로운 친구 추가
friend_ages["아섬"] = 13

print(friend_ages)

friend_ages["철수"] = 13  # 철수의 나이를 12 → 13으로 변경

print(friend_ages)
# {'철수': 13, '영희': 11, '민수': 13}

del friend_ages["영희"]  # 영희 삭제

print(friend_ages)
# {'철수': 13, '민수': 13}
