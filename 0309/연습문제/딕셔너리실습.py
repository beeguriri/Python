days = {'January':31, 'February':28, 'March':31, 'April':30,'May':31, 'June':30, 
        'July':31, 'August':31,'September':30, 'October':31, 'November':30, 'December':31}

#사용자가 월을 입력하면 해당 월에 일수를 출력하라
string = input('월을 입력하세요.')
print(days[string.title()])
# 대소문자 무시하기 위함

#알파벳 순서로 모든 월을 출력하라
days_key = list(days.keys())
print(sorted(days_key))

#일수가 31인 월을 모두 출력하라
for day in days:        #키값 출력
    if days[day] ==31 :
        print(day)

#월의 일수를 기준으로 오름차순(key-value)으로 쌍을 출력하라
#key와 value의 위치를 바꾸고 정렬 후 다시 key와 value의 위치를 바꿈
days_item = days.items()    #리스트로 바꿈
days_item = [ (day, month) for (month, day) in days_item]
days_item.sort() # 또는 days_item = sorted(days_item)
days_item = [ (month, day) for (day, month) in days_item]
print(days_item)


#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month = input('월을 입력하세요. (예시 : Jan, Feb)')
for m in days:
    if m[0:3]==month.title():
        print(days[m])



