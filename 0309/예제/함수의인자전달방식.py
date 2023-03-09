# 인자의 순서와 조합 사용 예시
def print_numbers(a, b, *args, c=10, d=20):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")
    print(f"args: {args}")

# 함수 호출
# 인자 전달 순서를 반드시 지켜야함
# 위치인자(a,b) -> 가변인자(*args) -> 기본값인자(c=10, d=20)
print_numbers(1, 2, 3, 4, 5, c=30, d=40)
# 출력 결과: a: 1, b: 2, c: 30, d: 40, args: (3, 4, 5)
