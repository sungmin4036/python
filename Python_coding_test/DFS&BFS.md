- 탐색(Search)란? 많은 양의 데이터 중에서 우너하는 데이터를 찾느 과정을 말합니다.
- 대표적인 그래프 탐색 알고리즘으로 DFS와 BFS가 있습니다.
- DFS/BFS는 코딩 테스트에서 매우 자주 등장하는 유형이다.

ㅁ 스택 자료구조
- 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)
- 입구와 출구가 동일한 형태로 스택을 시각화 할수 있습니다.

```
삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력   / [1, 3, 2, 5]
print(stack) # 최하단 원소부터 출력         / [5, 2, 3, 1]
```

<br>
<br>

ㅁ 큐 자료구조

- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태로 시각화 가능

```
삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제(7)-삽입(1)-삽입(4)-삭제(4)

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 / deque([3, 7, 1, 4])
queue.reverse() # 역순
print(queue) # 나중에 들어온 원소부터 출력 / deque([4, 1, 7, 3])
```

<br>
<br>

- 재귀 함수(Recursive Function)
: 자기 자신을 다시 호출하는 함수

- 단순한 형태의 재귀 함수 예제
  - '재귀 함수를 호출하빈다.' 라는 문자열을 무한히 출력
  - 어느 정도 출력하다가 최대 재귀 깊이 초과 메세지가 출력

```
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recusive_function()

recursive_function()
```

- 재귀 함수를 문제 풀이에서 사용시 재귀 함수의 종료 조건을 반드시 명시해야 합니다.
- 종료 조건을 명시하지 않으면 함수가 무한히 호출 될수 있습니다.
  - 종료 조건 포함한 재귀함수 예제

```
def recursive_funciton(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_function(i + 1)
    print(i, '번쨰 재귀함수를 종료합니다.')

recursive_funciton(1)
```

<br>
<br>
<br>

ㅁ 팩토리얼 구현 예제
- n! = 1 * 2 * 3 * 4 * ... * (n - 1) * n


```
# 반복적으로 구현한 n!
def factorial_iterative(n):        
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
       result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):        
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n - 1)

# 각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
```

<br>
<br>
<br>

![image](https://user-images.githubusercontent.com/62640332/150995519-db2b1f02-4f4d-4472-a1c7-520cf9ad55ba.png)

---

ㅁ 재귀 함수 사용의 유의사항

- 재귀 함수를 잘 활용하면 복잡한 알고리즘으로 간결하게 작성 가능
    - 단 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될수 있다.
- 모든 재귀 함수는 반복문을 이요하여 동일한 기능 구현할수 있다.
- 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
  - 그래서 스택을 사용할 떄 구현한 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

<br>
<br>
<br>

ㅁ DFS (Depth-First Search)

- DFS는 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작 과정은 다음과같다.

    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
    2. 스택의 초상단 노드에 바움ㄴ하지 않는 인접한 노드가 하나라도 이씅면 그 노드를 스택에 넣고 방문 처리한다. 방문하지 않는 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
    3. 더 이상 2번의 과정을 수행할 수 없을 떄까지 반복한다.

![image](https://user-images.githubusercontent.com/62640332/150996662-87660efd-26a4-4d0d-aa2b-ea3a5df37538.png)

![image](https://user-images.githubusercontent.com/62640332/150996807-b7623f53-50d1-4c6a-a9b9-f7d128b2c674.png)

![image](https://user-images.githubusercontent.com/62640332/150996851-e662c87c-b939-496f-9dcd-21bf796fe6ba.png)

![image](https://user-images.githubusercontent.com/62640332/150996933-e29a04b2-fe0e-455e-a50e-8feda0a1531c.png)

![image](https://user-images.githubusercontent.com/62640332/150997017-c1fe1b01-262a-4ebc-9f12-9ee719db2d24.png)

![image](https://user-images.githubusercontent.com/62640332/150997083-215f0c1f-be19-49b7-b5e4-a9f4e71f89ad.png)

![image](https://user-images.githubusercontent.com/62640332/150997176-576b4152-e4b7-415b-978f-991b02d8ff21.png)


![image](https://user-images.githubusercontent.com/62640332/150997242-859f5558-db6a-4cd8-80e4-942546cd6b58.png)

```
# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

------------------------
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7,],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문도니 정보를 표현 (1차원 리스트)
visited =[Fase] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

