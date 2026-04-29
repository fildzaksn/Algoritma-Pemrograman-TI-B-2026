# Helper recursive function
def isPalindromeRec(s, left, right):
        
    # Base case
    if left >= right:
        return True
        
    # If mismatch found
    if s[left] != s[right]:
        return False
        
    # Recursive call with narrowed range
    return isPalindromeRec(s, left + 1, right - 1)
    
def isPalindrome(s):
    return isPalindromeRec(s, 0, len(s) - 1)


if __name__ == "__main__":
    s = "abba"
    
    if isPalindrome(s):
        print("true")
    else:
        print("false")