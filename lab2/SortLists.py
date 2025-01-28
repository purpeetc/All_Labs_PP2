def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#фанк ддолжен находить самые близкие числа к- 50 по списку