'''
10진법수 N, 변환할 진법 B가 주어짐
B진법으로 변환한 수를 출력
'''

N, B = list(map(int,input().split()))
a = ''

while True:
  if N%B >=10:
    a += chr(N%B+ord('A')-10)
    N=int(N/B)
  else:
    a += str(N%B)
    N=int(N/B)
  if N==0:
    break

print(a[::-1])
