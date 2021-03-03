1) У вас есть список my_list с значениями типа int.
Распечатать те значения, которые больше 100.
Задание выполнить с помощью цикла for.

my_list=10,20,100,150,160,111,210
for index in (my_list):
    if index > 100:
        print(index)


2) У вас есть список my_list с значениями типа int, и пустой список my_results.
Добавить в my_results те значения, которые больше 100.
Распечатать список my_results.
Задание выполнить с помощью цикла for.

my_list=[10,20,100,150,160,111,210]
my_results= []
for index in (my_list):
    if index > 100:
        my_results= index
        print(my_results)



3) У вас есть список my_list с значениями типа int.
Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
Количество элементов в списке можно получить с помощью функции len(my_list)

my_list=[2]
my_len= len(my_list)
my_len1= str (my_len)

for index in (my_len1):
    if my_len < 2:
        print (my_list+[0])
    else:
        print((my_list[-2]) + (my_list)[-1])


Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
Вы приводите это value к типу float и выводите результат выражения value ** -1.
Написать программу, которая вычисляет данное выражение и
# корректно обрабатывает возможные исключения.


value = input ("Введите число с точкой:")
value = float (value)
try:
    new_value = value ** -1
except ():
    print(new_value)


5) У вас есть список my_list с значениями типа int, и пустой список my_results.
Добавить в my_results те значения из my_list для которых сумма индекса и значения будет четной.
Пример. [1,11,20,100]
Ответ [11, 20], потому что индекс 1 + значение 11 это 12 - четное, индекс 2 + значение 20 это 22 - четное


my_list = [1,11,20,100]
my_results = []
for key, value in enumerate (my_list):
    my_summ= key+value
    if my_summ % 2==0:
        my_results.append(value)
print((my_results))


6) У вас есть два списка my_list_1 и my_list_2 равной длинны.
Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу (можно range, можно enumerate).
# Например для списков [1, 3] и [2, 4]:

my_list_1 = [1,3]
my_list_2 = [2,4]
for value in enumerate (my_list_1 and my_list_2):
    # for value in enumerate(my_list_2):
        print(value)



7) У вас есть строка my_string = '0123456789'.
Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
Задание нужно выполнить ТОЛЬКО через цикл в цикле

my_string = '0123456789'
my_list = []
for symb_1 in my_string:
	for symb_2 in my_string:
            my_summ = symb_1+symb_2
            my_list.append(my_summ)
print(my_list)










