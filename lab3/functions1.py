#1 function grams to ounces
def grams_to_ounces(grams):
    return grams * 28.3495231

grams_input = float(input("Введите вес в граммах: "))
print("Вес в унциях:", grams_to_ounces(grams_input))

#2 function Farenheit temperature
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

fahrenheit_input = float(input("Введите температуру в Фаренгейтах: "))
print("Температура в Цельсиях:", fahrenheit_to_celsius(fahrenheit_input))


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
def filter_prime(numbers):
    primes = []
    for x in numbers:
        if x > 1:
            is_prime = True
            for i in range(2, x):
                if x % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(x)
    return primes

nums_input = input("Введите числа через пробел: ").split()
nums_list = [int(num) for num in nums_input]
print("Простые числа:", filter_prime(nums_list))


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
        print('*' * n)
hist_input = input("Введите числа для гистограммы через пробел: ").split()
hist_numbers = [int(num) for num in hist_input]
histogram(hist_numbers)


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


