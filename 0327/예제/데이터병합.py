import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

result = pd.concat([df1, df2], axis=0, ignore_index=True)
# axis 0: 행방향, 1: 열방향

print(result)
print("==========================")

# merge는 key를 기준으로
left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})

result = pd.merge(left, right, on='key')
print(result)
print("==========================")

result2 = pd.merge(left, right, on='key', how='inner')
print(result2)
print("==========================")

result3 = pd.merge(left, right, on='key', how='outer')
print(result3)
print("==========================")

result4 = pd.merge(left, right, on='key', how='left')
print(result4)
print("==========================")

result5 = pd.merge(left, right, on='key', how='right')
print(result5)
print("==========================")

# join은 index를 기준으로
# 예시 데이터
left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']},
                    index=['K0', 'K1', 'K2', 'K3'])
right = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']},
                     index=['K0', 'K1', 'K2', 'K3'])

# 인덱스를 기준으로 병합
result = left.join(right)
print(result)
