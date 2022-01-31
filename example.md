ㅁ sorted example

```
['a', 'b', 'd' , 'f', 'z']

>>> b = 'zbdaf'
>>> "".join(sorted(b))
'abdfz'
```
\# sort() 함수는 None 리턴 및 리스트 자체를 정렬하는 `제자리 정렬`

```
>>> c = ['ccc', 'aaa', 'd', 'bb']
>>> sorted(c, key=len)
['d', 'bb', 'ccc', 'aaaa']
```

```
a = ['cde', 'cfc', 'abc']
def fn(s):
    return s[0], s[-1]

print(sorted(a, key=fn))
-----------------------
['abc', 'dfc', 'def']
```

ㅁ 슬라이싱 과 인덱스 조회
```
s = '12345'

s[1:3] ------------- 23
s[3]   ------------- 4
```


