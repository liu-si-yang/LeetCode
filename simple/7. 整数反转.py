'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

# 方法一:转换成字符串,转置str[::-1]
class Solution_1:
    def reverse(x:int):
        sign = x < 0
        # print('sign:',sign)
        x_str = str(abs(x))
        # print('x_str:',x_str)
        x_result = x_str[::-1]
        # print('x_result:',x_result)
        x_int = int(x_result) * (-1 if sign else 1 )
        # print('x_int:',x_int)
        # print('2**31:',2**31)
        # print('-2**31-1:', -2**31-1)
        # print(x_int > 2**31 or x_int < -2**31-1)
        if x_int > 2**31 or x_int < -2**31-1:
            return 0
        else:
            return  x_int

print(Solution_1.reverse( -321))

print('-------------------------------------------')
# 方法二
class Solution_2:
     def reverse (x : int):
         num = 0
         while (x != 0):
             temp = x % 10
             num = num*10 + temp
             x = int(x/10)
         if x > 0 & x < 2**31:
             return num
         elif x < 0 & x > -2**31-1:
             return -num
         else:
             return 0

print(Solution_2.reverse(-321))



















