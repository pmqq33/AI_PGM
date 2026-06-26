
# 🐍 Python - 리스트 (List)

> 작성일: 2026-06-26  
> 태그: `#Python` `#List` `#자료구조`

---

## 📌 리스트란?

리스트(List)는 여러 개의 값을 **순서대로** 저장할 수 있는 자료구조입니다.  
파이썬에서 가장 많이 사용되는 자료형 중 하나로, **수정(mutable)이 가능**합니다.

```python
fruits = ["사과", "바나나", "체리"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # 서로 다른 타입도 담을 수 있음
```

---

## 🔧 리스트 생성

```python
# 빈 리스트 생성
empty1 = []
empty2 = list()

# 값이 있는 리스트
nums = [10, 20, 30]

# list()로 변환
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
```

---

## 📐 인덱싱과 슬라이싱

```python
fruits = ["사과", "바나나", "체리", "딸기", "포도"]

# 인덱싱 (0부터 시작)
print(fruits[0])   # 사과
print(fruits[-1])  # 포도 (뒤에서 첫 번째)

# 슬라이싱 [시작:끝:간격]
print(fruits[1:3])   # ['바나나', '체리']
print(fruits[:2])    # ['사과', '바나나']
print(fruits[2:])    # ['체리', '딸기', '포도']
print(fruits[::2])   # ['사과', '체리', '포도'] (2칸씩)
print(fruits[::-1])  # 리스트 역순
```

---

## ✏️ 리스트 수정

```python
nums = [1, 2, 3]

# 값 변경
nums[0] = 10        # [10, 2, 3]

# 슬라이싱으로 여러 값 변경
nums[1:3] = [20, 30]  # [10, 20, 30]
```

---

## 🛠️ 주요 메서드

| 메서드 | 설명 | 예시 |
|--------|------|------|
| `append(x)` | 끝에 요소 추가 | `lst.append(5)` |
| `insert(i, x)` | 인덱스 i에 요소 삽입 | `lst.insert(1, 99)` |
| `extend(iterable)` | 다른 리스트 이어붙이기 | `lst.extend([6, 7])` |
| `remove(x)` | 첫 번째 x 제거 | `lst.remove(3)` |
| `pop(i)` | 인덱스 i 요소 제거 & 반환 | `lst.pop(0)` |
| `index(x)` | x의 인덱스 반환 | `lst.index(5)` |
| `count(x)` | x의 개수 반환 | `lst.count(2)` |
| `sort()` | 오름차순 정렬 (원본 변경) | `lst.sort()` |
| `reverse()` | 역순 정렬 (원본 변경) | `lst.reverse()` |
| `copy()` | 얕은 복사 | `lst2 = lst.copy()` |
| `clear()` | 모든 요소 제거 | `lst.clear()` |

```python
lst = [3, 1, 4, 1, 5, 9, 2]

lst.append(6)          # [3, 1, 4, 1, 5, 9, 2, 6]
lst.sort()             # [1, 1, 2, 3, 4, 5, 6, 9]
lst.sort(reverse=True) # [9, 6, 5, 4, 3, 2, 1, 1]
print(lst.count(1))    # 2
```

---

## 🔁 리스트 순회

```python
colors = ["red", "green", "blue"]

# 기본 for문
for color in colors:
    print(color)

# 인덱스와 함께 순회
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# while문으로 순회
i = 0
while i < len(colors):
    print(colors[i])
    i += 1
```

---

## ⚡ 리스트 컴프리헨션

반복문과 조건문을 한 줄로 간결하게 표현하는 문법입니다.

```python
# 기본 형태: [표현식 for 변수 in 반복가능객체]
squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# 조건 필터링
evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

# 중첩 반복
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
# [(1, 3), (1, 4), (2, 3), (2, 4)]
```

---

## ⚠️ 얕은 복사 vs 깊은 복사

```python
import copy

original = [1, 2, [3, 4]]

# 얕은 복사 - 중첩 리스트는 참조를 공유함
shallow = original.copy()
shallow[2][0] = 99
print(original)  # [1, 2, [99, 4]] ← 영향받음!

# 깊은 복사 - 완전히 독립적인 복사본
deep = copy.deepcopy(original)
deep[2][0] = 0
print(original)  # [1, 2, [99, 4]] ← 영향 없음
```

---

## 🧩 유용한 내장 함수

```python
nums = [3, 1, 4, 1, 5, 9]

len(nums)        # 6 - 길이
sum(nums)        # 23 - 합계
min(nums)        # 1 - 최솟값
max(nums)        # 9 - 최댓값
sorted(nums)     # [1, 1, 3, 4, 5, 9] - 새 정렬 리스트 반환 (원본 유지)
list(reversed(nums))  # [9, 5, 1, 4, 1, 3] - 역순 새 리스트
```

---

## 💡 핵심 정리

- 리스트는 **순서 있음**, **중복 허용**, **수정 가능**
- 인덱스는 **0**부터 시작, 음수 인덱스로 뒤에서 접근 가능
- `sort()`는 원본을 변경, `sorted()`는 새 리스트를 반환
- 중첩 리스트 복사 시 `copy.deepcopy()` 사용 권장
- **리스트 컴프리헨션**으로 코드를 간결하게 작성 가능

---

*📚 다음 학습 예정: 튜플(Tuple), 딕셔너리(Dictionary)*
