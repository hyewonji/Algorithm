'''
직사각형의 왼쪽 아래꼭지점 : (0,0), 
직사각형의 오른쪽 위꼭지점 :(w,h)
직사각형 내부의 점 (x,y)가 직사각형을 탈춝하기 위한 최단거리 구하기
'''

x, y, w, h = map(int,input().split())

print(min(x,y,(w-x),(h-y)))
