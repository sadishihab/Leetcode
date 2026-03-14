def longestPalindromeLength(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    ans = 0

    for i in range(len(s)):
        ans = max(ans, expand(i, i), expand(i, i + 1))

    return ans