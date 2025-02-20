def num(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield str(i)

n = int(input("enter the number: "))
res = ",".join(num(n))
print(res)