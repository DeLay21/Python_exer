class palindromo:
    def num_pali(self, numero):
        resulatado = []

        for i in numero:
            resulatado.insert(0,i)
        if numero == resulatado:
           print('numero palíndromo')
           return True
        
        else:
            print("O Número não palíndromo")
            return False

x = palindromo()
print(x.num_pali([1,2,1]))
print(x.num_pali([1,2,3]))