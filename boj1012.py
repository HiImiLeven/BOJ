import sys
input=sys.stdin.readline
def search(ground,x,y):
    global M,N
    if y<0 or x<0 or x>M-1 or y>N-1:
        return False
    elif ground[y][x]==1:
        ground[y][x]=0
        search(ground,x+1,y)
        search(ground,x-1,y)
        search(ground,x,y+1)
        search(ground,x,y-1)
        
for i in range(int(input())):
    M,N,K = map(int,input().split())
    ground = [[0 for i in range(M)] for i in range(N)]
    for j in range(K):
        x,y = map(int,input().split())
        ground[y][x]=1
    checksum=0
    for a in range(N):
        for b in range(M):
            if ground[a][b]==1:
                search(ground,b,a)
                checksum+=1
    print(checksum)
