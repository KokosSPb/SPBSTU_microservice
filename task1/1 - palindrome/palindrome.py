def bPalindrome(tP):
    return tP == tP[::-1]

print(bPalindrome("rotator"))
print(bPalindrome("text"))
print(bPalindrome("refer"))