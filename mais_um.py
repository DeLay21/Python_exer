class Solution:
    def plusOne(self, digits):
        
        for i in range(len(digits) -1 ,-1, -1):
            digits[i] += 1

            if digits[i] < 10:
                return digits
            
            elif digits[i] == 10:
                digits[i] = 0

        return [1] + digits       

x = Solution()
print(x.plusOne([1,2,9])) 

