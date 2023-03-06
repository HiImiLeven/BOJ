import sys
input = sys.stdin.readline
N=int(input())

for i in range(N):
    x = list(map(int,input().split()))
    range = x[1]-x[0]-2
    print(range)