import matplotlib.pyplot as plt


print('Informe os valores de A, B, C da equação desejada para retirar seus parâmetros:')

a = float(input('Digite o A da equação: '))
b = float(input('Digite o B da equação: '))
c = float(input('Digite o C da equação: '))
delta = b**2-4*a*c

def baskhara_x1(a,b,delta):
    x1 = (-b + delta**0.5)/2*a
    return x1


def baskhara_x2(a,b,delta):
    x2 = (-b - delta**0.5)/2*a
    return x2

def soma_raizes(a,b):
    soma = -b/a
    return soma

def produto_raizes(a,c):
    produto = c/a
    return produto

def xv(a,b):
    xv = -b/(2*a)
    return xv

def yv(a,delta):
    yv = -delta/(4*a)
    return yv

soma = soma_raizes(a,b)
produto = produto_raizes(a,c)
x1 = baskhara_x1(a,b,delta)
x2 = baskhara_x2(a,b,delta)
xvert = xv(a,b)
yvert = yv(a,delta)

if delta < 0:
    print(f'Não há raizes pois delta é negativo: {delta}')
elif delta == 0:
    print(f'Ambas as raizes são iguais: {x1}, {x2}')
else:
    print(f'X1: {x1}')
    print(f'X2: {x2}')
print(f'Y do vertice: {yvert}')
print(f'X do vertice: {xvert}')
print(f'Produto das raizes: {produto}')
print(f'Soma das raizes: {soma}')

i = -10
x= []
y= []

while i < 10:
    x.append(i)
    f = a*i**2 + b*i + c
    y.append(f)
    i+=1
    print(x)
    print(y)


plt.plot(x,y)
plt.show()
indice = y.index(min(y))
print(x[indice])
print(x)
print(y)
print(min(y))


