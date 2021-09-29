import math 
import time

def base_to_ten(num, system_base=2):
    remainder = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    num = str(num)
    sign = 1
    if num.find('-') >= 0:
        sign = -1
        num = num.replace('-', '')
    power = num.find('.') - 1 if '.' in num else len(num) - 1
    num = num.replace('.', '')
    result = 0
    for i in range(len(num)):
        result += remainder[num[i]] * system_base ** power
        power -= 1
    return result * sign

def ten_to_base(num, system_base=2):
    remainder = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    whole = int(abs(num))
    fractional = float(abs(num)) % 1
    result = "." if fractional != 0 else "" 
    while whole >= system_base:
        result += str(remainder[whole % system_base])
        whole //= system_base
    result += str(remainder[whole % system_base])
    result = ('' if num >= 0 else '-') + result[::-1] 
    while fractional > 0:  
        temp_fractional, temp_whole = math.modf(fractional * system_base)
        fractional = abs(temp_fractional)
        result += str(remainder[int(temp_whole)])
    return result


def translation(num, in_base, out_base):
    return ten_to_base(base_to_ten(num, in_base), out_base)


def result_data(text_url):
    with open(text_url) as f:
        num = f.readlines()
    start_time = time.time()
    for i in range(len(num)):
        num[i] = num[i].replace('\n', '')
        num[i] = translation(num[i], 10, 2)
        num[i] = translation(num[i], 2, 16)
        num[i] = float(translation(num[i], 16, 10))
    end_time = time.time() - start_time
    result_sum = sum(num)
    return end_time, result_sum


def result_time_sum(text):
    result_time, result_sum = result_data(text)
    print("data: ", text)
    print(f'Сумма всех десятичных чисел после завершения цикла преобразований: {result_sum}')
    print(f'Время программы в миллисекундах:  {result_time*1000}ms')

text1 = "data10.txt"
text2 = "data11.txt"

result_time_sum(text1)
result_time_sum(text2)

