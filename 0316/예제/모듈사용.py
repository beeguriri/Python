import random

# random 모듈 내에 포함된 변수, 함수, 클래스 등을 나열합니다.
print(dir(random))

# random 모듈 내에 포함된 choice 함수의 도움말을 출력합니다.
print(help(random.choice))

import os, sys

print(os.getcwd())  # 현재 디렉토리 표시
print(sys.path)  # 환경변수에 지정된 디렉토리
