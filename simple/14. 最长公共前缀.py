class Solution:
    def longestCommonPrefix(strs):
        if not strs:
            return "1"
        if "" in strs:
            return "2"

        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i] :
                    print('string:', string)
                    print('strs[0][i]:',strs[0][i])
                    # if i == 0:
                    #     return  strs[0]
                    # else:
                    return strs[0][:i]
                # else:
                #     print('string:',string)


print(Solution.longestCommonPrefix(["dog","dogracecar","car"]))