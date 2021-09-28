import math 

def two_to_ten(num,system_num=2):
    remainder = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    num = str(num)
    power = num.find('.') - 1 if '.' in num else len(num) - 1
    num = num.replace('.', '')
    result = 0
    for i in range(len(num)):
        result += remainder[num[i]] * system_num ** power
        power -= 1
    return result

def ten_to_system(num, system_num=2):
    remainder = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    whole = int(num)
    fractional = float(num) % 1
    result = "." 
    while whole >= system_num:
        result += str(remainder[whole % system_num])
        whole //= system_num
    result += str(remainder[whole % system_num])
    result = result[::-1] 
    while fractional > 0:  
        temp_fractional, temp_whole= math.modf(fractional * system_num)
        fractional = temp_fractional
        result += str(remainder[int(temp_whole)])
    return result



num = 6578.7567
print(f"num: {num},\nresult 2 in 10: {ten_to_system(num)}, \
\nresult 10 in 2: {two_to_ten(ten_to_system(num, 16), 16)}, \
\nresult 10 in 16: {ten_to_system(num, 16)}")
