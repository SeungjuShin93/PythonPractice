from AltinoLite import *  # 알티노 라이트를 제어할 수 있는 함수를 포함한 파이썬 모듈

Open('com11')  # Open 함수로 시리얼 통신 시작

Light(0x01)
# Light(0x02)
delay(1000)
Light(0)


Close()  # Close 함수로 시리얼 통신 종료
