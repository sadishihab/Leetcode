class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1 — Initialize two pointers
        L, R = 0, len(s) - 1

        # Step 2 — Move pointers towards each other
        while L < R:
            # Skip non-alphanumeric characters on the left
            while L < R and not s[L].isalnum():
                L += 1
            # Skip non-alphanumeric characters on the right
            while L < R and not s[R].isalnum():
                R -= 1

            # Step 3 — Compare lowercase characters
            if s[L].lower() != s[R].lower():
                return False  # mismatch found → not palindrome

            # Step 4 — Move inward
            L += 1
            R -= 1

        # Step 5 — Pointers met with no mismatch → palindrome
        return True
