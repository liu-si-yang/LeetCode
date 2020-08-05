# 方法一:转字符串
class Solution:
    def isPalindrome( x: int) -> bool:
        x_str = str(x)
        x_result= x_str[::-1]
        return x_str == x_result

print(Solution.isPalindrome(-121))

# 方法一简化
class Solution:
    def isPalindrome( x: int) -> bool:
        return str(x) == str(x)[::-1]

print(Solution.isPalindrome(-121))