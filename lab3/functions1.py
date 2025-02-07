#1 function grams to ounces
def grams_to_ounces(grams):
    return grams * 28.34952

a = int(input("Введите вес в граммах: "))
print(f"Вес в унциях: {grams_to_ounces(a)}")


#2 function Farenheit temperature
def farenheit_to_celsius(farenheit):
    return (farenheit - 32) * 5 / 9

a = int(input("Введите температуру в Фаренгейтах: "))
print(f"Температура в Цельсиях: {farenheit_to_celsius(a)}")


#3 function Classic Puzzle
def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return "No solution"

def count_chicken_rabbit(numheads, numlegs):
    solution = solve(numheads, numlegs)
    if solution == "No solution":
        print("No solution")
    else:
        print(f"Куриц: {solution[0]}, кроликов: {solution[1]}")

a, b = int(input("Введите количество голов: ")), int(input("Введите количество ног: "))
count_chicken_rabbit(a, b)


#4 function Prime Numbers
def prime(numbers):
    return [x for x in numbers if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 1000000, 124, 123, 23, 1000001]
print(f"Простые числа: {prime(numbers)}")


#5 function permutation of string
import itertools

def permute_string(string):
    return list(itertools.permutations(string))
s = input("Введите что угодно: ")
print(f"Возможные перестановки: {permute_string(s)}")


#6 function permutation of words
def permute_words(words):
    return list(itertools.permutations(words))
words = input("Введите слова через пробел: ").split()
print(f"Возможные перестановки: {permute_words(words)}")


#7 function container with 3 number
def has_33(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


#8 function with spy
def spy_game(numbers):
    code = [0, 0, 7, 'x']
    for num in numbers:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

print(
spy_game([1,2,4,0,0,7,5]), 
spy_game([1,0,2,4,0,5,7]),
spy_game([1,7,2,0,4,5,0])
)


#9 function volume of sphere
def volume_sphere(radius):
    return 4 / 3 * 3.14 * radius ** 3

a = int(input("Введите радиус сферы: "))
print(f"Объем сферы: {volume_sphere(a)}")


#10 function unique numbers
def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique

list1 = [1, 2, 3, 3, 3, 3, 4, 5]
list2 = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]

print(unique_list(list1), unique_list(list2))


#11 function palindrom
def palindrome(string):
    return string == string[::-1]

s = input("Введите строку: ")
print(f"{palindrome(s)}")


#12 function histogram
def histogram(items):
    for n in items:
        output = ""
        times = n
        while times > 0:
            output += "*"
            times -= 1
        print(output)

histogram([4, 9, 7])


#13 function Guess the Number
def guess_number(name):
    import random
    number = random.randint(1, 20)
    guess = 0
    count = 0
    while guess != number and guess != "exit":
        guess = input("Take a guess: ")
        if guess == "exit":
            break
        guess = int(guess)
        count += 1
        if guess < number:
            print("your number is too low")
        elif guess > number:
            print("your number is too high")
        else:
            print(f"Good job {name}! You guessed my number in {count} guesses!")

name = input("What is your name? ")
print(f"Hello {name}, i'm thinking of a number between 1 and 20.")
guess_number(name)


#14 Comments
#jojojojojojojojojokjojojojoj


