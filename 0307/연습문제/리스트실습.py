"""
3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오 
    insert()로 맨 앞에 새로운 친구 추가
    insert()로 3번째 위치에 새로운 친구 추가
    append()로 마지막에 친구 추가
"""
friends = ['aaa', 'bbb', 'ccc', 'ddd']
friends.insert(0,'abc')
friends.insert(2,'qwe')
friends.append('zzz')
print(friends)

"""
리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
    두 번째 요소를 17로 수정
    리스트에 4, 5, 6을 추가
    첫 번째 요소 제거
    리스트를 요소 순서대로 배열하기
    인덱스 3에 25넣기
"""

myList = [1,2,3]
myList[1] = 17
addlist = [4,5,6]
myList = myList + addlist
myList.pop(0)
myList.sort()
myList.insert(3, 25)
print(myList)