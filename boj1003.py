import sys
input = sys.stdin.readline

Cnt0=[1,0]+[0 for i in range(39)] #1까지만 기재
Cnt1=[0,1]+[0 for i in range(39)] #역시 1까지만 기재

for i in range(2,41): #2부터 40까지 bottom-up 방식으로 채워나감
    Cnt0[i] = Cnt0[i-1] + Cnt0[i-2] # fibo(x) = fibo(x-1) + fibo(x-2) 형식의 점화식 
    Cnt1[i] = Cnt1[i-1] + Cnt1[i-2] 
    
for i in range(int(input())):
    x=int(input())
    print(Cnt0[x],Cnt1[x]) # N번째 값 출력