# Construa o programa que tendo como dados de entrada dois pontos quaisquer em um plano cartesiano
# , P(x1, y1) e Q(x2, y2), calcule a distância entre eles. Use a seguinte fórmula:
# distância = RAIZ(x2 - x1)^2 + (y2 - y1)^2

x1 = int(input('Qual o primeiro ponto x? '))
y1 = int(input('Qual o primeiro ponto y? '))
x2 = int(input('Qual o segundo ponto x? '))
y2 = int(input('Qual o segundo ponto y? '))
d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print('A distância dos pontos P({}, {}) e Q({}, {}) é {}.'.format(x1, y1, x2, y2, d))
