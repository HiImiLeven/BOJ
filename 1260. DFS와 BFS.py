from collections import deque
N,M,V=map(int,input().split())

dfsLog=[]
bfsLog=[]
queue=deque([])

def dfs(graph,v,visited):
    global dfsLog
    dfsLog.append(v)
    visited[v]=True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph,i,visited)
            
def bfs(graph,v,visited):
    global queue
    visited[v]=True
    queue.append(v)
    while queue: 
        x=queue.popleft()
        bfsLog.append(x)
        for i in graph[x]:
            if visited[i] == False:
                visited[i]=True
                queue.append(i)
                

visited=[]+[False for i in range(N+1)]
graph=[]+[[] for i in range(N+1)]

for i in range(M):
    x=list(map(int,input().split()))
    graph[x[0]].append(x[1])
    graph[x[1]].append(x[0])
for i in range(1,N+1):
    graph[i]=sorted(graph[i])
    
dfs(graph,V,visited)
print(" ".join(list(map(str,dfsLog))))
visited=[]+[False for i in range(N+1)]
bfs(graph,V,visited)
print(" ".join(list(map(str,bfsLog))))

