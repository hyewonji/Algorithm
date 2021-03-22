'''
N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성해라.
'''

N = int(input())

def permutation(N):

  arr = [ i+1 for i in range(N)] 
  last_arr =  arr[::-1]

  print(*arr)

  while arr != last_arr:
    k = N-2

    # 순열 뒤에서부터 arr[k]<arr[k-1]인 경우를 찾는다
    while True:
      if arr[k]<arr[k+1]:
        l = N-1

        # arr[k] 뒤에 오는 숫자 중, arr[k]보다 크고 가장 먼 인덱스 l을 찾는다.
        # arr[k]와 arr[l]을 바꿔준다.
        # arr[k] 뒤에 있는 숫자들을 뒤집는다.
        while True:
          if arr[k]<arr[l]:
            prop = arr[k]
            arr[k] = arr[l]
            arr[l] = prop
            arr[k+1:]=arr[k+1:][::-1]
            print(*arr)
            break
          else:
            l -= 1
        break
      else: 
        k -= 1

permutation(N)
