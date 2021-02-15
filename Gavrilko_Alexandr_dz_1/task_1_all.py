
# Task 1

print('Task 1')
duration = 3245366
sec = duration % 60
minute = duration // 60
hour = minute // 60
minute_res = minute - (hour * 60)
day = duration // 86400
hour_res = hour - (day * 24)

if day != 0:
	print(f'{day} дн {hour_res} час {minute_res} мин {sec} сек')
elif hour_res != 0:
	print(f'{hour_res} час {minute_res} мин {sec} сек')
elif minute_res != 0:
	print(f'{minute_res} мин {sec} сек')
else:
	print(f'{sec} сек')

# Task 2

print('Task 2')
number = 19
while number < 1000:
    if number % 2 == 1:
        number_cub = number ** 3
        val_1 = number_cub % 10
        val_2 = (number_cub % 100) // 10
        val_3 = (number_cub // 100) % 10
        val_4 = (number_cub // 1000) % 10
        val_5 = (number_cub // 10000) % 10
        val_6 = (number_cub // 100000) % 10
        val_7 = (number_cub // 1000000) % 10
        val_8 = (number_cub // 10000000) % 10
        val_9 = (number_cub // 100000000) % 10
        summ = val_1 + val_2 + val_3 + val_4 + val_5 + val_6 + val_7 + val_8 + val_9
        if summ % 7 == 0:
            print('число: ', number, '  куб: ', number_cub , '  sum: ', summ)
            number += 1
        else:
            number += 1
    else:
        number += 1

# Task 3

print('Task 3')
number = 0
while number < 21:
	if number == 1:
        	print(number, 'процент')
	        number += 1
	elif 2 <= number <= 4:
	        print(number, 'процента')
	        number += 1
	elif 20 >= number > 4 or number == 0:
       		print(number, 'процентов')
	        number += 1 








