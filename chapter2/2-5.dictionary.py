# 딕셔너리 자료형
# 다른 언어 - Hash, Map, Object, JSON

# 딕셔너리는 중괄호 {} 사용
# Key와 Value로 이루어짐
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(type(dic))  # <class 'dict'>

a = {1: 'hi'}
print(a)
a = {'a': [1, 2, 3]}
print(a)

#! 딕셔너리 쌍 추가, 삭제하기
# 딕셔너리 쌍 추가하기
a = {1: 'a'}

# 추가
a[2] = 'b'
print(a)

# 꼭 숫자가 아니어도 됌
a['name'] = 'pey'
print(a)

# 리스트도 추가 가능
a[3] = [1, 2, 3]
print(a)

#! 딕셔너리 요소 삭제하기
# del 함수를 사용해서 del a[key]를 입력하면 지정한 Key에 해당하는 {Key: Value} 쌍이 삭제됨
del a[1]
print(a)
del a['name'], a[3]  # 여러개 한번에 삭제도 가능
print(a)
# print(a[3]) # KeyError: 3, 없는 거 찾으면 키에러 나옴

#! 딕셔너리를 사용하는 방법
# 딕셔너리에서 Key를 사용해 Value 얻기
# 어떤 Key의 Value를 얻기 위해서는 '딕셔너리_변수_이름[Key]'를 사용해야 한다.
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])

dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

#! 딕셔너리 만들 때 주의할 사항
# Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시
# 동일한 Key가 2개 존재할 경우, 1: 'a' 쌍이 무시
a = {1: 'a', 1: 'b'}  # 덮어 씌어져서 마지막 key만 남음
print(a)

'''
또 1가지 주의해야 할 점은 Key에 리스트는 쓸 수 없다는 것이다. 하지만 튜플은 Key로 쓸 수 있다. 딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는(mutable) 값인지, 변하지 않는(immutable) 값인지에 달려 있다. 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.
'''
# a = {[1, 2]: 'hi'}
# print(a) #!? TypeError: unhashable type: 'list'

#! 딕셔너리 관련 함수
# Key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
# 출력 결과물
# dict_keys(['name', 'phone', 'birth'])
'''
점프 투 파이썬
파이썬 3.0 이후 버전의 keys 함수, 어떻게 달라졌나?
파이썬 2.7 버전까지는 a.keys() 함수를 호출하면 dict_keys가 아닌 리스트를 리턴한다. 리스트를 리턴하기 위해서는 메모리 낭비가 발생하는데, 파이썬 3.0 이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 리턴하도록 변경되었다. 다음에 소개할 dict_values, dict_items 역시 파이썬 3.0 이후 버전에서 추가된 것들이다. 만약 3.0 이후 버전에서 리턴값으로 리스트가 필요한 경우에는 list(a.keys())를 사용하면 된다. dict_keys, dict_values, dict_items 객체는 리스트로 변환하지 않더라도 기본적인 반복 구문(예: for 문)에서 사용할 수 있다.
'''
print(list(a.keys()))
# 출력 결과물
# ['name', 'phone', 'birth']

# dict_keys 객체는 다음과 같이 사용할 수 있다. 리스트를 사용하는 것과 별 차이는 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수는 수행할 수 없다.
for k in a.keys():
    print(k)

#! Value 리스트 만들기 - values
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.values())

#! Key, Value 쌍 얻기 - items
# items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 리턴
# a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.items())

#! Key: Value 쌍 모두 지우기 - clear
a.clear()
print(a)

#! Key로 Value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a['name'])
print(a.get('phone'))
print(a['phone'])
# a.get('name')은 a['name']을 사용했을 때와 동일한 결괏값을 리턴한다.
# a['nokey']처럼 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우, a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 리턴한다는 차이가 있다
print(a.get('nokey'))  # None
# print(a['nokey']) #? KeyError: 'nokey'

#! 딕셔너리 안에 찾으려는 Key가 없을 경우, 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때는 get(x, '디폴트 값')을 사용하면 편리하다.
print(a.get('nokey', 'foo'))  # 'nokey'가 없어서 foo 를 반환

#! 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print('name' in a)
print('email' in a)

# 리스트는 딕셔너리의 인덱스가  0, 1, 2 라고 시작하는 딕셔너리라고 생각해도 이해가 좋을듯, 메서드는 다르지만, 개념은 비슷
# ex
a = [1, 2, 3]
a = {0: 1, 1: 2, 2: 3}
print(a[1])
