from typing import NewType


n=int(input())
vector=list(map(int, input().split()))
newList=vector[::-1]
for i in newList:
    print(i, end=' ')