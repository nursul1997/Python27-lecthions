"====================================Числа====================================="
import math
number = 5
print(type(number)) #<class 'int'>

string = '5'
c = int('10')
print(type(c))

number = 10.5
print(type(number))
print(0.1 + 0.1 + 0.1 +0.1 + 0.1 + 0.1 + 0.1 + 0.1 +0.1 + 0.1) #0.9999999999999999

from decimal import Decimal
#  number = Decimal('0.1 + 0.1 + 0.1 +0.1 + 0.1 + 0.1 + 0.1 + 0.1 +0.1 + 0.1')
print(int(number))
# надо через строку

#bin
number = bin(10)
print(number)
numberc = int(number,2)

# complex
number = complex(10,3)
print(number) #(10+3j)

"==============================Операции на числах==========================="
#сложение(+) вычитание(-) умножение(;) деление(/ - деление .0  // - без остатка )
# остаток от деления (%)
# возведение в степень(** or pow(a,b)) pow(2,3,4) = 0 остаток от деления(4) 
# модуль числа(abs)
# divmod целочисленное деление и остаток 
# sqrt - нахождение квадратного корня

''
h = 513
floor = 2.7
print(h/floor)
''