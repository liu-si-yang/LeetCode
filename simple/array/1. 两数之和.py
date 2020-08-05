'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

# https://www.cnblogs.com/benjamin77/p/9980564.html

num_list = [2,7,11,15]
target = 26
result_list = []

# 方法一
class Solution_1:
    def twoSum_1( num_list, target):
        # print('list长度',len(num_list))
        for i in  range(len(num_list)):
            # print('i:',i)
            for j in range(i+1 ,len(num_list)):
                # print('j:', j)
                if target == num_list[i] + num_list[j]:
                    result_list.append(i)
                    result_list.append(j)
                    return result_list
                # else:
                #     print('无相应结果')
print( Solution_1.twoSum_1(num_list,target))


# 方法二

# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
# 语法 : enumerate(sequence, [start=0])

class Solution_2:
    def twoSum_2(num_list,target):
        for index, value in enumerate(num_list):
            next_index=index+1
            if target - value in num_list[next_index:]:
                # list index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
                # 语法 : list.index(x[, start[, end]])
                # print('next_index:',next_index)
                # print('num_list[next_index:]:',  num_list[next_index:])
                # print(num_list[next_index:].index(target-value))
                return [index,num_list[next_index:].index(target-value)+next_index]

print(Solution_2.twoSum_2(num_list,target))


# 方法三
dict = {}
class Solution_3:
    def twoSum_3(num_list,target):
        for i  in range(len(num_list)):
            if target-num_list[i] not in num_list:
                print('i:', i)
                print('num_list:' , num_list)
                dict[num_list[i]]=i
            else:
                print('target-num_list[i]:' , target-num_list[i])
                print('dict[target-num_list[i]]:' , dict(target-num_list[i]),0)
                return

# [dict[target-num_list[i] ], i]
Solution_3.twoSum_3(num_list,target)