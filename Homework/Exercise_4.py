# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти '))
if (number < 1 or number > 4):
    print('Нет такой четверти!')
elif (number == 1):
    print('Диапазон возможных координат X > 0 и y > 0') 
elif (number == 2):
    print('Диапазон возможных координат X < 0 и y > 0') 
elif (number == 3):
    print('Диапазон возможных координат X < 0 и y < 0') 
elif (number == 4):
    print('Диапазон возможных координат X > 0 и y < 0') 
 
 
 
 
 
 
 
#  if(num == 1) Console.WriteLine("Координаты X > 0 и y > 0");
#  else if(num == 2) Console.WriteLine("Координаты X < 0 и y > 0");
#  else if(num == 3) Console.WriteLine("Координаты X < 0 и y < 0");
#  else if(num == 4) Console.WriteLine("Координаты X > 0 и y < 0");
