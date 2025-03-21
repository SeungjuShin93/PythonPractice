# f 문자열 포매팅 - 이게 제일 중요, 3.6버전 이상에서 가능
# 1. 기본
name = '홍길동'
age = 30
string = f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
print(string)
string = f'나의 이름은 {name}입니다. 나이는 {age + 1}입니다.'
print(string)
string = f'나의 이름은 {name}입니다. 나이는 {age * 2}입니다.'
print(string)

# 2. 소수점
y = 3.42134234
results = f'{y:0.4f}'  # 소수점 4자리까지만 표현
print(results)

# 3. {} 중괄호 출력
curl = f'{{ and }}'
print(curl)
string = f'나의 이름은 {{{name}}}입니다. 나이는 {age * 2}입니다.'
print(string)

# 4. f 문자열을 사용하여 금액에 콤마(,) 삽입하기 - 이런건 검색, 외우지 말자
comma = f"난 {1500000:,}원이 필요해"
print(comma)
