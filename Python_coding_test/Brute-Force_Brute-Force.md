구현(Implementation), 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정

problem - thinking - solution

흔히 알고리즘 대회에서 구현 유형의 문제란?
: 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 것을 지칭합니다.

- 구현의 예시
  - 알고리즘은 간단한데 코드가 지나치게 길어지는 문제
  - 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
  - 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
  - 적절한 라이브러리를 찾아서 사용해야 하는 문제


![image](https://user-images.githubusercontent.com/62640332/150795157-6a06fb3a-01d8-4479-b039-5782727e23f5.png)


![image](https://user-images.githubusercontent.com/62640332/150795419-29733dc3-e8ba-4c0f-8b6b-ffc54728c171.png)

---

![image](https://user-images.githubusercontent.com/62640332/150795779-ebba6deb-cd56-4845-9e84-c4a41bed05b5.png)

![image](https://user-images.githubusercontent.com/62640332/150796017-fd91eff4-ee10-4496-a911-cc65c994a293.png)


![image](https://user-images.githubusercontent.com/62640332/150796106-962197e7-a844-464a-b84f-9bb7b3c4eb6b.png)

---

ㅁ문제 해결 아이디어

- 이 문제는 요구사항대로 충실히 구현하면 되는 문제다
- 일련의 명렁에 따라서 개체를 차례대로 이동시진다는 점에서 시뮬레이션 유형으로도 분류 되며, 구현이 중요한 대표적인 문제 유형
  - 다만 알고리즘 교ㅐ잔 문제 풀이 사이트에 따라서 다르게 일컬을 수 있으므로, 
  
  코딩 테스트에서의 시뮬레이션 유혀으 구현 유형, 완전 탐색 유형은 서로 유사한 점이 많다.

```
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

```
<br>
<br>
<br>
<br>
<br>
---

 
![image](https://user-images.githubusercontent.com/62640332/150796871-5f596e29-eedb-492e-a37b-6a497eb2c52e.png)


![image](https://user-images.githubusercontent.com/62640332/150796961-b759085e-4441-4770-8a10-51ed3aa6fc8d.png)

---
ㅁ 문제 해결 아이디어

- 가능한 모든 시각의 경우를 하나씩  모두 세서 풀 수 있는 문제
- 하루는 86,400초 이므로, 00시 00분 00초 ~ 23시 59분 59초 까지의 모든 경우의 수가 56,400
  - 24 * 60 * 60 = 86,400
- 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되는지 확인하면 된다.
- 이러한 유형은 완전 탐색(Brute Forcing) 문제 유형이라고 한다.
  - 가능한 경우의 수를 모두 검사해 보는 방법

```
h = int (intput())

count = 0
fo i in range(h + 1):
  for j in range(60):
    for k in range(60):
      # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
      if '3' in str(i) + str(j) + str(k)
        count +=1

pirnt(count)
```
---

<br>
<br>
<br>
<br>
<br>
<br>
<br>

![image](https://user-images.githubusercontent.com/62640332/150797715-e803ab5f-9f30-4e8b-b09c-12bf7aacd259.png)

![image](https://user-images.githubusercontent.com/62640332/150797806-a741bc56-87d1-4613-bb86-32424acf6f7d.png)

![image](https://user-images.githubusercontent.com/62640332/150797935-a9f7f41d-a614-4f55-927c-2ec391359bdc.png)

![image](https://user-images.githubusercontent.com/62640332/150797973-f4b82d0d-0136-429a-8e14-048b2756f103.png)

---

ㅁ 문제 해결 아이디어

- 요구사항 대로 충실히 구현하면 되느 문제
- 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동 가능한지 확인
  - 리스트를 이용하여 8가지 벡터 정의하기


```
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)

```

<br>
<br>
<br>
<br>
<br>

![image](https://user-images.githubusercontent.com/62640332/150798478-002737b7-5bfd-4467-a648-479ce640e472.png)

![image](https://user-images.githubusercontent.com/62640332/150798659-193e5880-4371-4185-ae24-0ca611bbd737.png)

---
ㅁ 문제 해결 아이디어

- 요구사항대로 충실히 구현하면 되는 문제
- 문자열이 입력시 문자를 하나씩 확인
  - 숫자인 경우 따로 합계
  - 알파벳은 경우 별도의 리스트에 저장
- 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답

```
data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
  # 알파벳 일경우 리스트에 삽입
  if x.isalpha():
    result.append(x)
  #숫자는 따로 더하기
  else:
    value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 노재 않하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최정 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
```