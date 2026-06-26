# Python 기초 정리 (강의노트)

> 교재 + 오늘 실습 코드 + 강의 메모를 통합하여 정리한 내용입니다.

---

# 1. 수식(Expression)의 구성 요소

파이썬의 대부분의 코드는 **수식을 계산하여 변수에 저장**하는 형태이다.

```python
변수 = 수식
variable = expression
```

수식(Expression)은 다음 4가지 요소로 구성된다.

| 구성요소          | 설명           | 예시                        |
| ------------- | ------------ | ------------------------- |
| Literal(값)    | 직접 사용하는 값    | `10`, `"Python"`          |
| Variable(변수)  | 데이터를 저장하는 공간 | `a`, `score`              |
| Operator(연산자) | 값을 계산        | `+`, `-`, `*`, `/`        |
| Function(함수)  | 특정 기능 수행     | `sum()`, `max()`, `len()` |

예제

```python
a = 10          # Literal
b = a           # Variable
c = a + b       # Operator
d = sum([a,b])  # Function
```

---

# 2. 자료형(Container)

여러 개의 데이터를 저장하는 자료형이다.

```python
list
tuple
set
dictionary
```

예제

```python
numbers = [10,20,30]

student = ("홍길동",20)

fruit = {"apple","banana","orange"}

person = {
    "이름":"홍길동",
    "나이":20
}
```

---

# 3. 입력(Input)

키보드에서 데이터를 입력받는 함수이다.

```python
a = input()
```

숫자를 입력받을 때는 형변환을 한다.

```python
a = int(input("첫 번째 숫자 : "))
b = int(input("두 번째 숫자 : "))
```

실습에서는 입력받은 두 정수의 사칙연산을 출력하였다.

---

# 4. 출력(Output)

출력 함수

```python
print()
```

f-string

```python
print(f"a + b = {a+b}")
print(f"a * b = {a*b}")
```

---

# 5. 산술연산자

| 연산자 | 설명  |
| --- | --- |
| +   | 더하기 |
| -   | 빼기  |
| *   | 곱하기 |
| /   | 나누기 |
| //  | 몫   |
| %   | 나머지 |
| **  | 제곱  |

예제

```python
a+b
a-b
a*b
a/b
a//b
a%b
a**b
```

---

# 6. 리스트(List)

리스트 생성

```python
numbers = [10,20,30,40,50]
```

합계

```python
sum(numbers)
```

평균

```python
sum(numbers)/len(numbers)
```

최대값

```python
max(numbers)
```

최소값

```python
min(numbers)
```

---

# 7. 리스트 인덱스(Index)

첫 번째 요소

```python
numbers[0]
```

마지막 요소

```python
numbers[-1]
```

예제

```python
fruit = ["사과","바나나","포도"]

print(fruit[0])
print(fruit[-1])
```

---

# 8. Dictionary

Key와 Value 형태로 데이터를 저장한다.

생성

```python
person = {
    "이름":"홍길동",
    "나이":20,
    "학과":"컴퓨터공학과"
}
```

접근

```python
print(person["이름"])
print(person["나이"])
```

---

# 9. Boolean

논리형(True / False)

```python
True
False
```

예제

```python
a = True
b = False

a &= b

print(a)
```

---

# 10. 조건문(if)

기본 문법

```python
if 조건식:
    실행문
elif 조건식:
    실행문
else:
    실행문
```

예제

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")
```

---

# 11. 오늘 실습

## 실습 1

두 개의 정수를 입력받아

* 덧셈
* 뺄셈
* 곱셈
* 나눗셈

출력하기

---

## 실습 2

정수 5개를 입력받아

* 합계
* 평균
* 최대값
* 최소값

출력하기

---

## 실습 3

과일 이름을 입력받아

* 첫 번째 과일
* 마지막 과일

출력하기

---

# 추가 정리 (강의 메모)

> 아래 내용은 위 내용과 중복되지 않는 메모만 정리한 것이다.

---

# 데이터 → 정보 → 지식

요리사 비유

```
재료(Input Data)

↓

요리(Process)

↓

완성된 음식(Output Information)

↓

Knowledge
```

* **Data** : 원재료
* **Process** : 데이터를 가공하는 과정
* **Information** : 처리 결과
* **Knowledge** : 결과를 분석하여 다음 행동을 결정하는 것

예)

> "이 음식은 간이 부족하네. 다음에는 소금을 조금 더 넣어야겠다."

즉, **정보를 활용하여 판단하는 단계가 Knowledge**이다.

---

# 연산자 우선순위

```
1. **
2. 단항연산 (+ - ~)
3. * / // %
4. + -
5. << >>
6. &
7. ^
8. |
9. 비교연산
10. not
11. and
12. or
13. 대입연산
```

---

# 제어문(Control Statement)

프로그램의 실행 순서를 제어하는 문장이다.

## 선택문

```python
if
match-case
```

## 반복문

```python
for
while
```

> Python에는 `do-while` 문이 존재하지 않는다.

## 반복 제어문

```python
break
continue
```

## 함수 종료

```python
return
```

---

# 들여쓰기(Indentation)

Python에서는 `{}` 대신 **들여쓰기**로 코드 블록을 구분한다.

```python
if score >= 90:
    print("A")
    print("Excellent")
```

들여쓰기가 맞지 않으면 `IndentationError`가 발생한다.
