'''
    给你两个有序整数数组 nums1 和 nums2，
    请你将 nums2 合并到 nums1 中，
    使 nums1 成为一个有序数组。
'''

# 方法一:拼接两个列表,然后排序

def Merge_array(num1, num2):
    num1.extend(num2)
    num1.sort()
    return num1



if __name__ == '__main__':
    print(Merge_array([1,2,3,0,0,0], [2,5,6]))