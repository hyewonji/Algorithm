'''
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 순서대로 K번째 사람을 제거한다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
요세푸스 순열을 구하는 프로그램을 작성하라.
'''


N, K = map(int,input().split())
circle = [i+1 for i in range(N)]

n = 0
removed = []
for i in range(N):
  n = (n + K - 1) % len(circle)
  removed.append(f'{circle[n]}')
  del circle[n]
  
# ', '.join(removed) : ', '와 각 string을 이어주는 역할을 한다.
# 대괄호를 제거하고 출력하기 위함
print(f'<{', '.join(removed)}>')
