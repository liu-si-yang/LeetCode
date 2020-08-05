# # # 方法一
# class Solution:
#     def remanToInt(s: str):
#         n_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         result = 0
#         for i in range(len(s)):
#             if i > 0 and n_map[s[i]] > n_map[s[i - 1]]:
#                 print(i)
#                 print('n_map[s[i-1]]: %d ,n_map[s[i]]: %d ,result: %d' % (n_map[s[i - 1]], n_map[s[i]], result))
#                 result = result + n_map[s[i]] - 2 * n_map[s[i - 1]]
#             else:
#                 print(i)
#                 print('n_map[s[i-1]]: %d ,n_map[s[i]]: %d ,result: %d' % (n_map[s[i - 1]], n_map[s[i]], result))
#                 result += n_map[s[i]]
#         return result
#
#
# print(Solution.remanToInt('IV'))


# # 方法二
class Solution_2:
    def remanToInt_2(s: str):
        n_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        tmp = result = 0
        for sk in s[::-1]:
            sv = n_map[sk]
            # if tmp <= sv:
            #     result = result + sv
            # else:
            #     result = result - sv
            result = (result+sv) if tmp <= sv else (result-sv)
            tmp = sv
        return result


print(Solution_2.remanToInt_2('MCMXCIV'))
