money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

money = False
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

#! 들여쓰기 방법 알아보기
'''
if 문을 만들 때는 if 조건문: 바로 다음 문장부터 if 문에 속하는 모든 문장에 들여쓰기(indentation)를 해야 한다. 다음 예를 보면 조건문이 참일 경우 ‘수행할_문장1’을 들여쓰기했고 ‘수행할_문장2’와 ‘수행할_문장3’도 들여쓰기했다. 다른 프로그래밍 언어를 사용해 온 사람들은 파이썬에서 ‘수행할_문장’을 들여쓰기하는 것을 무시하는 경우가 많으므로 더 주의해야 한다.
'''

# indent_error.py
money = True
if money:
    print("택시를")
print("타고")
# print("가라") # 에러,

# 아래는 어떤 뜻?
money = True
if money:
    print("택시를")
print("타고")
print("가라")

#! 조건문 다음에 콜론(:)을 잊지 말자!
# if 조건문 뒤에는 반드시 콜론(:)이 붙는다.
# 어떤 특별한 의미가 있다기보다는 파이썬의 문법 구조이다.

#! 조건문이란 무엇인가?
money = True
if money:
    pass
    # money는 True이기 때문에 조건이 참이 되어 if 문 다음 문장을 수행한다.

#! 📌 파이썬 비교 연산자 (Comparison Operators)
x = 10
y = 20
# x가 y보다 작다.
print(x < y)   # ✅ True (10 < 20)
# x가 y보다 크다.
print(x > y)   # ❌ False (10 > 20)
# x와 y가 같다.
print(x == y)  # ❌ False (10 == 20)
# x와 y가 같지 않다.
print(x != y)  # ✅ True (10 != 20)
# x가 y보다 크거나 같다.
print(x >= y)  # ❌ False (10 >= 20)
# x가 y보다 작거나 같다.
print(x <= y)  # ✅ True (10 <= 20)

# 퀴즈 - 만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라. (보유 금액 2000)
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#! and, or, not
# 퀴즈 - 돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라.
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#! in, not in
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

# 퀴즈 - 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라.
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#! 조건문에서 아무 일도 하지 않게 설정하고 싶다면? - pass 사용
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#! 다양한 조건을 판단하는 elif
# 퀴즈 - 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")
# elif 사용
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

#! if 문을 한 줄로 작성하기 - 가능하나 권장은 굳이?, 실용 보단 패션느낌
pocket = ['paper', 'money', 'cellphone']
# if 'money' in pocket: pass
# else: print("카드를 꺼내라")

#! 조건부 표현식
score = 100
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)
# 위와 아래는 같음 - 패션 코딩
score = 100
message = "success" if score >= 60 else "failure"
print(message)

# 조건부 표현식(패션 코딩)은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.
