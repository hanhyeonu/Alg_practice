from random import randrange

# --- 08-1. 빈 배열을 준비하고 루프를 돌면서 초기화하기 ---
squares_1 = []
for i in range(10):
    squares_1.append(i ** 2)

print('-- 빈 배열을 준비하고 루프를 돌면서 초기화하기 --')
print(f'{squares_1=}')

# --- 08-2. List Comprehension 이용하기 ---
squares_2 = [i ** 2 for i in range(10)]
print('\n-- List Comprehension 이용하기 --')
print(f'{squares_2=}')

# --- 08-3. map 이용하기 ---
def func(n):
    return n ** 2

squares_3 = list(map(func, range(10)))  # list()로 변환해서 바로 출력 가능
print('\n-- map 이용하기 --')
print(f'{squares_3=}')
print('map 결과 개별 출력: ', end='')
for sq in squares_3:
    print(sq, end=', ')
print()

# --- 08-4. map 결과는 실제 배열과는 다르므로 list 형태로 변환해서 사용 ---
squares_4 = list(map(func, range(10)))
print('\n-- map 결과는 실제 배열과는 다르다 --')
print('   (배열을 위한 메모리가 할당되지 않으므로 list 형태가 필요할 경우 변환해서 사용) --')
print(f'{squares_4=}')

# --- 08-5. map에 전달할 함수는 lambda 키워드를 써서 인라인으로 작성 가능하다 ---
squares_5 = list(map(lambda x: x**2, range(10)))
print('\n-- map에 전달할 함수는 lambda 키워드를 써서 인라인으로 작성 가능하다 --')
print(f'{squares_5=}')

# --- 08-6. 3x4 = 12개의 빈 배열을 만들고 알파벳 26자를 랜덤하게 배치 ---
dim3 = [[[] for _ in range(3)] for _ in range(4)]  # 3열x4행 의 12개의 빈 배열 준비
print(f'\nbefore: {dim3=}')
for i in range(26):
    ch = chr(ord('a') + i)
    x, y = randrange(3), randrange(4)  # 12개 배열 중 하나를 랜덤하게 선택
    dim3[y][x].append(ch)  # 선택된 배열에 문자 추가
print(f'after: {dim3=}\n')

# --- 08-7. Python은 class 생성자와 함수 호출 문법 구조가 같으므로 class 이름도 map에 쓸 수 있다 ---
class Game:
    def __init__(self, name):
        self.name = name
    def __repr__(self):  # 객체가 문자열로 표현될 때 호출됨
        return f'Game("{self.name}")'

games = list(map(Game, "helloworld"))
print('-- class 생성자와 map 사용 예시 --')
print(f'{games=}')
