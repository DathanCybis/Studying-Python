class Calculadora:
    def somar(self, num1, num2, num3=None):
        if num3 is None:
            return num1 + num2
        else:
            return num1 + num2 + num3
        

calc = Calculadora()

print(calc.somar(3, 2)) # 5

print(calc.somar(3, 2, 3)) # 8
