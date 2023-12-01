# https://leetcode.com/problems/longest-nice-substring/description/
s = "YazaAay"
n = len(s)
for i in range(len(s)):
    for j in range(i, n + 1):
        print(s[i:j+1])
