import funcoes_calculo
print("digite respectivamente os valores correspodentes a A, B, e C\npor favor utilize números por extenso\npor exemplo no lugar de 5/2 escreva 2.5 utilizando ponto no lugar de vírgula\ncerto 2.5/errado 2,5")
A = float(input("digite A "))
B = float(input("digite B "))
C = float(input("digite C "))

resultado = funcoes_calculo.equa_2(A,B,C)  

print(resultado)