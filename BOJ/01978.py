'''
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성해라.

첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
'''

N = int(input())
# N개의 수를 실수로 변환시켜 배열에 넣는다.
arr = list(map(int, input().split()))
count = 0

for i in range(N):
  # arr[i] <= 1 인 경우는 다음 for 문에서 range범위 이탈로 자동으로 실행되지 않지만, 코드를 잘 이해하기 위해 작성해줬다.
  if arr[i] <= 1:
    continue
  if arr[i] == 2 or arr[i] == 3:
    count += 1
  for j in range(2,(arr[i]//2)+1):
    # 약수가 발견되면 for문을 나온다.
    if (arr[i]%j) == 0:
      break
    # j가 arr[i]//2가 되도록 for문이 실행된것은 약수가 없다는 뜻이다.
    if j == arr[i]//2:
      count += 1

print(count)
