#1.1      Class with getString and printString
class mystr:
    def __init__(self):
        self.string = ""
    
    def getString(self):
        self.string = input("Напишите что-то: ")
    
    def printString(self):
        print(self.string.upper())

obj = mystr()
obj.getString()
obj.printString()



#1.2 Class with Shape and her child-class Square
class shape:
    def area(self):
        return 0

class square(shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2

square = square(95)
print(f"Площадь квадрата: {square.area()}")



#1.3 Class Rectangle which inherits from Shape
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rectangle = rectangle(4, 6)
print(f"Площадь прямоугольника: {rectangle.area()}")



#1.4 Class Point
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Координаты точки: ({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other_point):
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

point1 = Point(2, 3)
point2 = Point(5, 7)

point1.show()
point1.move(4, 6)
point1.show()
print(f"Расстояние между точками: {point1.dist(point2)}")



#1.5 Class for bank account
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Пополнение на {amount}. Текущий баланс: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
            print(f"Снятие {amount}. Текущий баланс: {self.balance}")

account = Account("Steve", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)



#1.6 Filtering prime numbers
is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x**0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

prime_numbers = list(filter(is_prime, numbers))
print(f"Простые числа: {prime_numbers}")