from datetime import date
# datetime은 날짜와 시간 관련 도구들이있는 모듈, 도서관(라이브러리)
# datetime안에 date, time, datetime 등 여러가지 도구(클래스)가 있음

# datetime은 큰 책장이라면 date는 그 안에있는 책(기능)

day1 = date(2024, 1, 1)
day2 = date(2025, 5, 20)
today = date.today()

print(type(day1))
print(day1)


def 디데이(목표날짜, 오늘날짜):
    print((목표날짜 - 오늘날짜).days)


디데이(day2, today)


# 질문, abs(), int(), print() 등은 파이썬이 기본으로 갖고 있는 기능 제공 함수
# 주방에 늘 있는 숟가락, 젓가락 같은 존재 - 자주 써서 성능을 위해 가볍게 하기 위함

# date, datetime, math, random 같은 건 표준 라이브러리
# 믹서기나 토스터기 등 필요할때만 꺼내쓰는 애들

# 모든 기능을 미리 불러오면 파이썬이 무거워짐, 최적화를 위한 시스템이라고 보면 됨
