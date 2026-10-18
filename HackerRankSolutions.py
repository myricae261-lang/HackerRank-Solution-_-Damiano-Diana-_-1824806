# ============================================================
# PROBLEM 1 - Introduction
# ============================================================


# say hello world with python

my_string = "Hello, World!"
print(my_string)

# python_if_else

import random

n = int(input())

if n % 2 != 0:
    print("Weird")

elif 2 <= n <= 5:
    print("Not Weird")

elif 6 <= n <= 20:
    print("Weird")

else:
    print("Not Weird")
    
# Arithmetic_Operators

a = int(input())
b = int(input())
print (a+b)
print(a-b)
print(a*b)

# python_division

a = int(input())
b = int(input())
print(a//b)
print(a/b)

# loops

n = int(input())

vettore = list(range(n))

for numero in vettore:
    print(numero ** 2)

# write function

def is_leap(year):
    leap = False

    if (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0):
        leap = True

    return leap

year = int(input())
print(is_leap(year))

# print function

n = int(input())
vettore = list(range(1,n+1))
for numero in vettore:
    print(numero, end="")
    
    
# ============================================================
# PROBLEM 1 - Basic Data Types
# ============================================================

# find runner up score

n=int(input())
arr = list ( map(int, input().split())   )
arr2 = sorted(set(arr))
runner_up = arr2[-2]
print(runner_up)

# nested lists

NOME = 0
VOTO = 1

n = int(input())
studenti = []

for _ in range(n):
    nome = input()
    voto = float(input())
    studenti.append([nome, voto])

minimo = min(studenti, key=lambda studente: studente[VOTO])

studenti = [
    studente
    for studente in studenti
    if studente[VOTO] != minimo[VOTO]
]

minimo = min(studenti, key=lambda studente: studente[VOTO])

for studente in sorted(studenti):
    if studente[VOTO] == minimo[VOTO]:
        print(studente[NOME])
    
# finding the percentage

n = int(input())

student_marks = {}

for _ in range(n):
    dati = input().split()

    nome = dati[0]
    voti = list(map(float, dati[1:]))

    student_marks[nome] = voti

query_name = input()

voti_richiesti = student_marks[query_name]

media = sum(voti_richiesti) / len(voti_richiesti)

print(f"{media:.2f}")

# lists

n = int(input())

my_list = []

for _ in range(n):
    comando = input().split()

    if comando[0] == "insert":
        i = int(comando[1])
        e = int(comando[2])
        my_list.insert(i, e)

    elif comando[0] == "print":
        print(my_list)

    elif comando[0] == "remove":
        e = int(comando[1])
        my_list.remove(e)

    elif comando[0] == "append":
        e = int(comando[1])
        my_list.append(e)

    elif comando[0] == "sort":
        my_list.sort()

    elif comando[0] == "pop":
        my_list.pop()

    elif comando[0] == "reverse":
        my_list.reverse()

#tuples

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))


# ============================================================
# PROBLEM 1 - Strings
# ============================================================

# string split and join

print("-".join(input().split()))

# whats your name

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


first_name = input()
last_name = input()
print_full_name(first_name, last_name)

# mutations 

def mutate_string(string, position, character):
    letters = list(string)
    letters[position] = character
    return "".join(letters)


s = input()
i, c = input().split()

s_new = mutate_string(s, int(i), c)

print(s_new)

# find a string

def count_substring(string, sub_string):
    counting=0
    for index in range(len(string)):
        if sub_string == string[index:len(sub_string)+index]:
            counting = counting +1
    return counting
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# string validators

s=input()

risultato=[]
for indice in range(len(s)):
     risultato.append(s[indice].isalnum())
print(True in risultato)
    
risultato = []
for indice in range(len(s)):
    risultato.append(s[indice].isalpha())
print(True in risultato)

risultato = []
for indice in range(len(s)):
    risultato.append(s[indice].isdigit())
print(True in risultato)

risultato = []
for indice in range(len(s)):
    risultato.append(s[indice].islower())
print(True in risultato)

risultato = []
for indice in range(len(s)):
    risultato.append(s[indice].isupper())
print(True in risultato)

# text_alignment

thickness = int(input())
c = "H"

for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

# text wrap

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# designer door mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = input().split()
n = int(n)
m = int(m)

for i in range(n // 2):
    motivo = ".|." * (2 * i + 1)
    print(motivo.center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n // 2 - 1, -1, -1):
    motivo = ".|." * (2 * i + 1)
    print(motivo.center(m, "-"))
    
# string formatting

def print_formatted(number):
    w = len(f"{number:b}")
    for i in range(1, number + 1):
        print(f"{i:{w}d} {i:{w}o} {i:{w}X} {i:{w}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# alphabet rangoli

def print_rangoli(size):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    righe = []

    for i in range(size):
        lettere = alfabeto[size - 1:i:-1] + alfabeto[i:size]
        riga = "-".join(lettere).center(4 * size - 3, "-")
        righe.append(riga)

    for riga in righe[:0:-1] + righe:
        print(riga)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# capitalize

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    parole = s.split(" ")

    for i in range(len(parole)):
        parole[i] = parole[i][:1].upper() + parole[i][1:]

    return " ".join(parole)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
    
# the minion game

def minion_game(string):
    kevin = 0
    stuart = 0
    n = len(string)

    for i in range(n):
        if string[i] in "AEIOU":
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
# merge the tools

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        risultato = ""

        for lettera in string[i:i + k]:
            if lettera not in risultato:
                risultato += lettera

        print(risultato)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
# swap case

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
# ============================================================
# PROBLEM 1 - Sets
# ============================================================

# tuples

n = int(input())
t = tuple(map(int, input().split()))
print(hash(t))

# introduction to sets

def average(array):
    arr2=set(array)
    result = sum(arr2)/len(arr2)
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
# No! Idea

n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

conteggio = 0

for numero in arr:
    if numero in A:
        conteggio += 1
    elif numero in B:
        conteggio -= 1

print(conteggio)

# symmetric difference

m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))

for elemento in sorted(M.symmetric_difference(N)):
    print(elemento)

# set.add()

n = int(input())
paesi = set()

for i in range(n):
    paesi.add(input())

print(len(paesi))

# set.discard() remove() and pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    comando = input().split()

    if comando[0] == "pop":
        s.pop()
    elif comando[0] == "remove":
        s.remove(int(comando[1]))
    elif comando[0] == "discard":
        s.discard(int(comando[1]))

print(sum(s))

# ============================================================
# PROBLEM 1 - Collections
# ============================================================

# DefaultDict Tutorial
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    d[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in d:
        print(*d[word])
    else:
        print(-1)

# Collections.namedtuple()
from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

total_marks = 0
for _ in range(n):
    student = Student(*input().split())
    total_marks += int(student.MARKS)

print(f"{total_marks / n:.2f}")

# Collections.OrderedDict()
from collections import OrderedDict

n = int(input())
od = OrderedDict()

for _ in range(n):
    *item, price = input().split()
    item_name = " ".join(item)
    price = int(price)
    
    if item_name in od:
        od[item_name] += price
    else:
        od[item_name] = price

for item, net_price in od.items():
    print(item, net_price)

# Word Order
from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]

counts = Counter(words)

print(len(counts))
print(*counts.values())



# ============================================================
# PROBLEM 1 - date and time
# ============================================================


# time delta

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    date1 = datetime.strptime(t1, fmt)
    date2 = datetime.strptime(t2, fmt)
    return str(int(abs((date1 - date2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

# ============================================================
# PROBLEM 1 - errors and execptions
# ============================================================

# Exceptions

# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

# ============================================================
# PROBLEM 1 - Built - ins
# ============================================================

# zipped!

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split())

marks = []

for _ in range(x):
    marks.append(list(map(float, input().split())))

for student_marks in zip(*marks):
    print(f"{sum(student_marks) / x:.1f}")

# athlete sort 

#!/bin/python3
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda row: row[k])

    for row in arr:
        print(*row)



# ============================================================
# PROBLEM 1 - Regex and Parsing
# ============================================================

# Regex Substitution
import re

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        line = input()
        line = re.sub(r'(?<= )&&(?= )', 'and', line)
        line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
        print(line)

# Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# Validating phone numbers
import re

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        number = input().strip()
        if re.match(r'^[789]\d{9}$', number):
            print("YES")
        else:
            print("NO")

# Validating and Parsing Email Addresses
import re
import email.utils

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        line = input().strip()
        name, email_addr = email.utils.parseaddr(line)
        if re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email_addr):
            print(line)

# Validating Credit Card Numbers
import re

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        cc = input().strip()
        if re.match(r"^[456](\d{15}|\d{3}(-\d{4}){3})$", cc) and not re.search(r"(\d)\1{3,}", cc.replace('-', '')):
            print("Valid")
        else:
            print("Invalid")

# Validating UID
import re

if __name__ == '__main__':
    n = int(input().strip())
    for _ in range(n):
        uid = input().strip()
        if re.match(r'^(?=(?:[a-zA-Z0-9]*[A-Z]){2})(?=(?:[a-zA-Z0-9]*\d){3})(?!.*(.).*\1)[a-zA-Z0-9]{10}$', uid):
            print("Valid")
        else:
            print("Invalid")

# ============================================================
# PROBLEM 1 - XML
# ============================================================

# XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth = max(maxdepth, level + 1)
    for child in elem:
        depth(child, level + 1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
    
# ============================================================
# PROBLEM 1 - Closures and Decorators
# ============================================================

# Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    
# ============================================================
# PROBLEM 1 - Numpy
# ============================================================

# Min and Max
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.max(numpy.min(arr, axis=1)))

# Sum and Prod
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)
print(numpy.prod(numpy.sum(arr, axis=0)))

# Dot and Cross
import numpy

n = int(input())
A = numpy.array([input().split() for _ in range(n)], int)
B = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(A, B))

# Shape and Reshape
import numpy

print(numpy.array(input().split(), int).reshape(3, 3))

# Transpose and Flatten
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(arr))
print(arr.flatten())

# Concatenate
import numpy

n, m, p = map(int, input().split())
array_1 = numpy.array([input().split() for _ in range(n)], int)
array_2 = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((array_1, array_2), axis=0))



# ============================================================
# PROBLEM 2 - birthday cake candles
# ============================================================


def birthdayCakeCandles(candles):
    conteggio = 0
    massimo = max(candles)

    for numero in range(len(candles)):
        if candles[numero] == massimo:
            conteggio += 1

    return conteggio


n = int(input())
candles = list(map(int, input().split()))
conteggio = birthdayCakeCandles(candles)
print(conteggio)

# ============================================================
# PROBLEM 2 - number line jumps
# ============================================================



x1, v1, x2, v2 = map(int, input().split())

if x2 > x1 and v1 > v2:
    if (x2 - x1) % (v1 - v2) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
    
# ============================================================
# PROBLEM 2 - viral advertising
# ============================================================

n = int(input())

def contamipiace(giorno):
    x = 5
    totale = 0

    for i in range(giorno):
        like = x // 2
        totale += like
        x = like * 3

    return totale

print(contamipiace(n))

# ============================================================
# PROBLEM 2 - recursive digit sum
# ============================================================


def superDigit(n, k):
    totale = sum(int(cifra) for cifra in n) * k

    while totale >= 10:
        totale = sum(int(cifra) for cifra in str(totale))

    return totale


n, k = input().split()
print(superDigit(n, int(k)))


# ============================================================
# PROBLEM 2 - insertion sort part 1 
# ============================================================


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    valore = arr[-1]

    for numero in sorted(range(len(arr)), reverse=True):
        if numero > 0 and valore < arr[numero - 1]:
            arr[numero] = arr[numero - 1]
            print(*arr)
        else:
            arr[numero] = valore
            print(*arr)
            break


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
    

# ============================================================
# PROBLEM 2 - insertion sort part 2
# ============================================================


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1, n):
        j = i

        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

        print(*arr)

        
     
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



