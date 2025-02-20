def even_number (n):
    for i in range (0,n+1): 
        if i % 2 == 0:
            yield str(i) #yield functions is like return and print. We need str for using join operator
             
n = int(input("Enter a number: "))
result = ",".join(even_number (n))
print("Even numbers: ", result)