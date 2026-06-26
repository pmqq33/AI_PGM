# 🐍 Python 기초 학습 정리

> 작성일: 2026-06-26  
> 태그: `#Python` `#print` `#문자열포맷팅` `#input` `#list`

---

## 1. print() 함수와 이스케이프 문자

`print()`는 화면에 값을 출력하는 함수입니다.  
문자열은 `"큰따옴표"` 또는 `'작은따옴표'` 모두 사용 가능합니다.

```python
print("Hello python")
print('Hello python')
```

`\n`은 **줄바꿈** 이스케이프 문자입니다.  
`"""삼중따옴표"""` 안에서도 줄바꿈을 표현할 수 있습니다.

```python
# \n으로 줄바꿈
print("고구마\n감자\n토마토\n양파\n마늘\n대파")

# 삼중따옴표 + \n 혼합
print("""H\ne\nl\nl\no""")
```

**출력 결과:**
```
고구마
감자
토마토
양파
마늘
대파
```

---

## 2. 문자열 포맷팅 - % 방식

`%d`, `%f`, `%s` 등의 **포맷 지정자**로 변수를 문자열에 삽입합니다.

| 지정자 | 의미 |
|--------|------|
| `%d` | 정수 (int) |
| `%f` | 실수 (float) |
| `%s` | 문자열 (string) |
| `%.2f` | 소수점 2자리까지 표시 |

```python
a = 3
str1 = "Sample python string"

print("I eat %d apples." % a)
# I eat 3 apples.

print("I eat %d apples and %f oranges." % ((1+2), 3.141592))
# I eat 3 apples and 3.141592 oranges.

print("I eat %d apples and %.2f oranges." % ((1+2), 3.141592))
# I eat 3 apples and 3.14 oranges.

print("example string : %s" % str1)
# example string : Sample python string
```

> 💡 **포인트:** 변수가 2개 이상이면 `% (값1, 값2)` 처럼 **괄호로 묶어서** 전달합니다.

---

## 3. 문자열 포맷팅 - 3가지 방법 비교

같은 출력을 세 가지 방법으로 표현할 수 있습니다.

```python
# 방법 1: f-string (가장 권장, Python 3.6+)
print(f"I eat {3} apples and {5} oranges.")

# 방법 2: % 포맷팅
print("I eat %d apples and %d oranges." % (3, 5))

# 방법 3: .format() 메서드
print("I eat {0} apples and {1} oranges.".format(3, 5))
```

**세 가지 모두 동일한 출력:**
```
I eat 3 apples and 5 oranges.
```

> 💡 **권장:** `f-string`이 가장 읽기 쉽고 간결해서 현재 가장 많이 사용됩니다.

---

## 4. input() 함수 - 사용자 입력 받기

`input()`은 키보드로부터 값을 입력받는 함수입니다.  
입력값은 기본적으로 **문자열(str)** 이므로, 숫자로 사용하려면 `int()` 또는 `float()`으로 변환해야 합니다.

```python
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

print(f"You entered: {a} and {b}")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
```

**실행 예시 (입력: 10, 3):**
```
You entered: 10 and 3
a + b = 13
a - b = 7
a * b = 30
a / b = 3.3333333333333335
```

---

## 5. 리스트 활용 - input() + list

`input()`으로 받은 값들을 **리스트에 저장**하고 `sum()`, `max()`, `min()` 등으로 분석합니다.

### 5-1. 숫자 5개 입력 → 통계 계산

```python
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))

numlist = [num1, num2, num3, num4, num5]

print(f"합: {sum(numlist)}")
print(f"평균: {sum(numlist)/len(numlist)}")
print(f"최대값: {max(numlist)}")
print(f"최소값: {min(numlist)}")
```

**실행 예시 (입력: 10, 20, 30, 40, 50):**
```
합: 150
평균: 30.0
최대값: 50
최소값: 10
```

### 5-2. append()로 리스트에 값 추가

```python
b = []

list1 = input("Enter first fruit: ")
b.append(list1)
list2 = input("Enter second fruit: ")
b.append(list2)
list3 = input("Enter third fruit: ")
b.append(list3)

print(f"첫 번째 과일: {b[0]}")
print(f"마지막 과일: {b[-1]}")
```

**실행 예시 (입력: apple, banana, cherry):**
```
첫 번째 과일: apple
마지막 과일: cherry
```

> 💡 **포인트:** `append()`로 빈 리스트에 값을 하나씩 추가할 수 있습니다.  
> `b[-1]`은 리스트의 **마지막 요소**를 가리킵니다.

---

## 💡 핵심 정리

| 개념 | 핵심 내용 |
|------|-----------|
| `print()` | `"` 또는 `'` 모두 사용 가능, `\n`으로 줄바꿈 |
| 문자열 포맷팅 | f-string > .format() > % 순으로 권장 |
| `input()` | 반환값은 항상 `str` → 숫자는 `int()` 변환 필요 |
| 리스트 + 내장함수 | `sum()`, `len()`, `max()`, `min()` 활용 |
| `append()` | 빈 리스트에 값을 순서대로 추가 |

---

*📚 다음 학습 예정: 조건문(if), 반복문(for, while)*
