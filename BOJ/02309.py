'''
일곱 난장이

일곱 난쟁이의 키의 합이 100이 된다.
입력받은 9명중 일곱난쟁이만 찾아 오름차순으로 출력하는 프로그램을 작성해라.


for문이 2개이상 중첩될 때 한번에 빠져나오는 법:
error를 발생시며 except구문으로 넘어가게 한다.
'''

arr = [int(input()) for _ in range(9)]

excess = sum(arr)-100

try:
  for i in range(len(arr)-1):
    for j in range(1,len(arr)):
      if arr[i]+arr[j] == excess:
        del arr[i]
        del arr[j-1]

        raise NotImplementedError
except:
  for i in sorted(arr): print(i)
