class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0:
        print('número negativo')
        nega_str_x = str(-x)
        reverso_neg = nega_str_x[::-1]
        return reverso_neg == nega_str_x
      
      else:
         print('número positivo')
         x_str = str(x)
         reverso = x_str[::-1]

         return x_str == reverso
      
        

x = Solution()
print(x.isPalindrome(123))
print(x.isPalindrome(-121))
print(x.isPalindrome(121))
print(x.isPalindrome(-123))
