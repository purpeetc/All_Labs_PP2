first_file = "/Users/aliakimbaj/Desktop/damndamndamn.txt"
second_file  = "/Users/aliakimbaj/Desktop/holyholyholy.txt"

a = open(first_file, "r")
b = open(second_file, "w+")
for i in a: 
    b.write(i)
print(b.read())
print("File copyied successfully! File copyed from a to b")