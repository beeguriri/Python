# 1부터 45까지의 수 중에서 6개를 선택하여 로또 번호를 만드는 프로그램

import random

pick = set()
while len(pick)<6:
    pick.add(random.randint(1,45))

print(sorted(pick))
# sorted 하면 결과 list로 반환

fruits = ['apple', 'banana', 'cherry', 'date']
