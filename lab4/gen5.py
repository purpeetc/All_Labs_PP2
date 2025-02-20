def number(n):
    while n >= 0: 
        yield n  
        n = n-1
a = int(input())
for i in number(a):
    print(i, end=" ")