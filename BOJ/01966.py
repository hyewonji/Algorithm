'''
문제유형 : 큐

각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

첫째줄에 테스트 케이스의 개수가 주어진다.
테스트 케이스는 두 줄로 주어진다.
  첫째줄 : queue 내부 문서의 개수 n, 몇번째로 출력되는지 알고싶은 문서의 인덱스 m
  둘째줄 : 문서의 중요도
'''

test_num = int(input())

for i in range(test_num):
  count = 0
  n, m = map(int, input().split())
  queue = map(int, input().split())
  queue = [(v,idx) for (idx,v) in enumerate(queue)]
  
  while True:
    if queue[0][0] == max(queue, key = lambda x: x[0])[0]:
      count += 1
      if queue[0][1] == m:
        print(count)
        break
      else:
        queue.pop(0)
    else: 
      queue.append(queue.pop(0))
