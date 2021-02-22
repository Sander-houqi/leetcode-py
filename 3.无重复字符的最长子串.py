#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:

    # def lengthOfLongestSubstring(self, s: str) -> int:

    #     map = {}
    #     i = 0
    #     max_len = 0
    #     for j in range(len(s)):
    #         if s[j] in map:
    #             i = max(map.get(s[j]),i)

    #         max_len = max(max_len,j-i+1)
    #         map[s[j]]=j+1

    #     return max_len

    # 滑动窗口
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        
        return max_len

       


# @lc code=end
if __name__ == "__main__":
    s= Solution()
    # string = "abcabcbb"
    string = "pwwkew"
    print(s.lengthOfLongestSubstring(string))