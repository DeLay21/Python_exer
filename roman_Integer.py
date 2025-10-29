class Solution:
    def romanToInt(self, a: str) -> int:
        sim_val = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100,'D': 500, 'M': 1000
        }

        resultado = 0
        
        for i in range(len(a)):
            if i + 1 < len(a) and sim_val[a[i]] < sim_val[a[i + 1]]:
                resultado -= sim_val[a[i]]
            else:
                resultado += sim_val[a[i]]
        
        return resultado
    
nu_rom = Solution()
print(nu_rom.romanToInt('XII'))