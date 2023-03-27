import pandas as pd

# 샘플 데이터 생성
data = {
    'text': ['Hello, World!', 'Pandas is great', 'Python is awesome']
}
df = pd.DataFrame(data)

# 문자열 처리 작업
df['lower'] = df['text'].str.lower()  # 모든 문자를 소문자로 변환
df['words'] = df['text'].str.split()  # 공백을 기준으로 단어 분할
df['no_punctuation'] = df['text'].str.replace('[^\w\s]', '', regex=True)  # 구두점, 기호 제거
df['word_count'] = df['text'].str.split().str.len()  # 단어 개수 계산

print(df)
print(df.iloc[:, 1:])
