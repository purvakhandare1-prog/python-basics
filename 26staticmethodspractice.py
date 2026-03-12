

class StringUtils:
    text = "python"

    @staticmethod
    def reverse(s):
        rev = ""
        for ch in s:
            rev = ch + rev
        return rev

    @staticmethod
    def is_palindrome(s):
        rev = StringUtils.reverse(s)
        if s == rev:
            return True
        else:
            return False
        
print(StringUtils.reverse("python"))
print(StringUtils.is_palindrome("madam"))
print(StringUtils.is_palindrome("python"))