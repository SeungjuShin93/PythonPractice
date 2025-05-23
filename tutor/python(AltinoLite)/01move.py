# 장치 및 프린터
# ALTINO-L~~~~
# 하드웨어 - 직렬 링크(COM10) 뒤에 숫자 기억
# 적힌 번호를 port='com10' 수정해줌

from AltinoLite import *  # 알티노 라이트를 제어할 수 있는 함수를 포함한 파이썬 모듈

Open('com11')  # Open 함수로 시리얼 통신 시작

Go(300, 300)  # 알티노 라이트 300속도로 전진
# Go(-500, -500)

delay(1000)  # 1초간 지연
# delay(2000)

Go(0, 0)  # 알티노 라이트 멈춤

Close()  # Close 함수로 시리얼 통신 종료
