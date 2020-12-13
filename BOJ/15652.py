'''
Backtraking

N과 M이 주어졌을 때, 길이가 M인 수열을 다음의 규칙에 맞게 구하여라

1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 된다.
3. 고른 수열은 비내림차순이어야 한다.
   비내림차순 : 길이가 K인 수열 A가 A1 ≤ A2 ≤ … ≤ AK-1 ≤ AK를 만족하는 것.
'''

N, M = map(int, input().split())
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        solve(depth+1, i, N, M)
        out.pop()

solve(0, 0, N, M)
