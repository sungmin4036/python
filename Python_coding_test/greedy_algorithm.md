- 그리디 알고리즘(탐욕법)

: 현재 상황에서 지금 당장 좋은 것만 고르는 방법

- 이반적인 그리디 알고리즘은 문제를풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
- 그리디 해법은 그 정당성 분석이 중요
- 단순히 가장 좋아 보이는 것을 반복적으로 선태갷도 최적의 해를 구할수 있는지 검토
- 일반적인 상황에서 그리디 알고리즘은 최적의 해를 보장할 수 없을 떄가 많습니다.
- 하지만 코딩 테스트에서의 대부분 긜디 문제는 탐욕법으로 얻은 해가 최적의 해가 되는 상황에서, 이를 추론 할수 있어야 풀리도록 출제

<br>
<br>
<br>

---

ㅁ<h3> <문제> 거스름돈 </h3>

: 음식점의 계산을 도와주는 점원, 카운터에는 거스름돈으로 사용할돈 500, 100, 50, 10원짜리 동전이 무한히 존재한다고 가정

손님에게 서슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하시오.

---

ㅁ 문제 해결 아이디어

- 최적의 해를 빠르게 구하기 위해서 가장 큰 화폐 단위부터 돈을 거술러 준다.
- N원을 거슬러 줘야 할 때, 가장 먼저 500원으로 거슬러 줄 수 있을 만큼 거슬러준다.
- 이후에 100, 50, 10원짜리 동전을 차례대로 거슬러 줄수 있을 만큼 거슬러 주면 된다.

---

ㅁ 정당성 분석

- 가장 큰 화폐 단위부터 돈을 거슬러 주는 것이 최적의 해를 보장하는 이유는 무엇인가?
  - 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올수 없기 떄문
- 만약 800원을 거슬러 주어야 하는데 화폐 단위가 500, 400, 100원일 경우는? (500원은 400원의 배수가 아니므로 적정성이 달라진다.)
  - 그리디 아록리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할수 있어야 한다.

```
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin   # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)
```
ㅁ 시간 복잡도

- 화페의 종류가 K 라고 할떄, 시간 복작도는 O(K)
- 이 알고리즘의 시간복잡도는 거슬러줘야 하는 금액과는 무관하며, 동전의 총 종류에만 영향을 받는다.

--

<br>
<br>
<br>
<br>
<br>


ㅁ<h3> <문제> 1이 될 떄까지 </h3>

![image](https://user-images.githubusercontent.com/62640332/150688808-8e9ed3b7-9c9a-42bd-8524-e8ab1a8c096e.png)

![image](https://user-images.githubusercontent.com/62640332/150790277-1f1455f1-5e12-4c1b-95a0-9e36b9d9ebdf.png)

![image](https://user-images.githubusercontent.com/62640332/150790320-110ef705-292f-4a63-9691-c16defc94e67.png)

---
ㅁ 정당성 분석

- 가능하면 최대한 많이 나누느 작업이 최적의 해를 항상 보장할수 있을까?
- N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일수 있다
- 다시 말해 K가 2이상이기만 하면, K로 나누는 것이 1을 뺴는 것보다 항상 빠르게 N을 줄일수 있다
  - 또한 N은 항상 1에 도달하게 된다(최적의해 성립)
  

```
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k       # n이 k 나누어 떨어지지 않을떄 가장 가까운 k 의값 찾기 가능
    result += (n - target)      # 연산을 하는 총 횟수
    n = target                  
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

```


<br>
<br>
<br>
<br>

![image](https://user-images.githubusercontent.com/62640332/150791812-d858b3e6-fdea-4503-92f7-d6666c2d32ce.png)

![image](https://user-images.githubusercontent.com/62640332/150792109-7ab1db4f-7cda-4129-9ce0-39d2baa851c3.png)

---

ㅁ 문제 해결 아이디어

- 대부분의 경우 + 보다 x가 더 값을 크게 만든다
- 다만 두 수중에 하나라도 0 또는 1 인경우 곱하기 보다는 더하기가 더 효율적이다.
- 따라서 두수에 대한 연산을 수행시, 두수 중에서 하나라도 1이하인 경우에는 더하며, 두수 모두가 2이상인 경우에 곱하면 정답 이다.

---

```
dataa = input()

#첫 번쨰 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data));
    # 두 수 중에서 하나라도 0 or 1인경우 곱하기 보다는 더하기 수행

    num = int(data[i])    
    if num <= 1 or result <= 1:
      result += num
    else:
      result *= num

print(result)
```


---

<br>
<br>
<br>
<br>
<br>

![image](https://user-images.githubusercontent.com/62640332/150792896-d720a9a6-f301-4069-a47e-650df2c3e1c6.png)

![image](https://user-images.githubusercontent.com/62640332/150793054-7c9a986f-5868-4cc9-8293-63a8c40c3265.png)

![image](https://user-images.githubusercontent.com/62640332/150793127-7d17d1c0-8271-49de-a3c3-48b6452bde03.png)

![image](https://user-images.githubusercontent.com/62640332/150793471-a0114161-d0d7-498f-8a5e-41301caf9950.png)

![image](https://user-images.githubusercontent.com/62640332/150793527-cb1295e7-7e9b-4864-b53b-0cba268dc8e5.png)


---
```
n = int(intput()) 
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: #공포도를 낮은 것부터 하나씩 확인
  count += 1  # 현재 그룹에 해당 모험가를 포함 시키기
  if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1   # 총 그룹의 수 증가시키기
    count = 0     # 현재 그룹에 포함된 모험가의 수 초기화

print(result)     # 총 그룹의 수 출력    
``` 