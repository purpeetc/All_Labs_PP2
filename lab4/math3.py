import math
n = int(input("num of sides: "))
s = int(input("length og each side: "))
area = (n*s**2) / (4 * math.tan(math.pi / n)) 
print(int(round(area,2)))