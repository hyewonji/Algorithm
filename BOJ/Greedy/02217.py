import sys

N = int(input())
lists = list(sys.stdin.readline().rstrip() for _ in range(N))
r_lists = sorted(map(int,lists))[::-1]
r = r_lists[0]

if N != 1:
  for i in range(1,N):
    if r <= r_lists[i]*(i+1):
      r = r_lists[i]*(i+1)

print(r)
