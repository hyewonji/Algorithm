'''
64cm 막대를 더 작은 막대로 자른다음에, 풀로 붙여서 길이가 Xcm인 막대를 만들려고 한다.

1. 가지고 있는 막대의 길이를 모두 더한다. 
   (처음에는 64cm 막대 하나만 가지고 있다.)
   이때, 합이 X보다 크다면, 아래와 같은 과정을 반복한다.
  1. 가지고 있는 막대 중 길이가 가장 짧은 것을 절반으로 자른다.
  2. 만약, 위에서 자른 막대의 절반 중 하나를 버리고 남아있는 막대의 길이의 합이 X보다 크거나 같다면, 위에서 자른 막대의 절반 중 하나를 버린다.
  
2. 이제, 남아있는 모든 막대를 풀로 붙여서 Xcm를 만든다.
'''


n = 64
X = int(input())
a = []
a.append(n)

while True:
  if sum(a) > X:
    m = min(a)
    if sum(a) - m/2 >= X:
      a.remove(m)
      a.append(m/2)
    else:
      a.remove(m)
      a.append(m/2)
      a.append(m/2)
  elif sum(a) == X :
    break
  
print(len(a))
