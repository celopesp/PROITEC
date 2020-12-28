"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e 
calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = raiz quadrada de (x2 - x1)^2 + (y2 - y1)^2

Entrada
O arquivo de entrada contém duas linhas de dados. 
A primeira linha contém dois valores de ponto flutuante: x1 y1 e 
a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""
import math
a1,b1 = input("Informe os dois valores (separados por espaço) do ponto p1(x1,y1):").split()

a2,b2 = input("Informe os dois valores separados por espaço do ponto p2(x2,y2):").split()
x1 = float(a1)
y1 = float(b1)
x2 = float(a2)
y2 = float(b2)

distancia = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

print(f'{distancia:.4f}')