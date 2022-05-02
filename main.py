def mapa(x0, R):
    """ definindo uma função chamada 'mapa', que retorna o valor de x1 para um dado x0 e R """
    return x0*R*(1-x0)


x1 = mapa(x0=0.1, R=3.4)
print("x1 =", x1)

x2 = mapa(x0=x1, R=3.4)
print("x2 =", x2)

x3 = mapa(x0=x2, R=3.4)
print("x3 =", x3)


def orbita(x0, R, maxiter):
    """ definindo uma função que retorna uma órbita, ou seja, retorna os valores de x1, x2, ..., xn a partir de um dado x0 e R."""

    #  inicializa uma lista com zeros em todas as posições
    x = [0]*(maxiter+1)

    # primeiro elemento da lista x recebe o valor x0
    x[0] = x0

    # preencho a lista x com os respectivos valores de x1, x2, x2, ..., xn
    for n in range(maxiter):
        x[n+1] = mapa(x[n], R)

    # retorna a lista x
    return x


x = orbita(x0=0.1, R=3.4, maxiter=3)
print(x)

# plotando o vetor x
import matplotlib.pyplot as plt # matplotlib é uma maneira de visualizar dados
plt.plot(x, marker='o')
plt.xlabel("índice")
plt.ylabel("valor de x")
plt.show()

# iterando a órbita 50 vezes
x = orbita(x0=0.1, R=3.4, maxiter=30)
plt.plot(x, marker='o')
plt.xlabel("índice")
plt.ylabel("valor de x")
plt.show()


import numpy as np
x0_list = np.linspace(0, 1, 30)
print(x0_list)

x1_list = mapa(x0=x0_list, R=3.4)

# gráfico de x1 em função de x0
plt.plot(x0_list, x1_list, marker='o')
plt.plot([0, 0.9], [0, 0.9]) # linha identidade
plt.xlabel('x0')
plt.ylabel('y0')
plt.show()


# gráfico em formato 'cobweb'
plt.plot(x0_list, x1_list)
plt.plot([0, 0.9], [0, 0.9]) # linha identidade
plt.xlabel('x0')
plt.ylabel('y0')

x = orbita(x0=0.1, R=3.4, maxiter=15)
for i in range(len(x)-1):
    plt.plot([x[i], x[i], x[i+1]], [x[i], x[i+1], x[i+1]], marker='o', color='red')

plt.show()


# gráfico em formato 'cobweb', onde ignoramos um tempo de transiente
plt.plot(x0_list, x1_list)
plt.plot([0, 0.9], [0, 0.9]) # linha identidade
plt.xlabel('x0')
plt.ylabel('y0')

x = orbita(x0=0.1, R=3.4, maxiter=100)
for i in range(80, len(x)-1):
    plt.plot([x[i], x[i], x[i+1]], [x[i], x[i+1], x[i+1]], marker='o', color='red')

plt.show()


# exemplo de órbita caótica
x1_list = mapa(x0=x0_list, R=3.95)

plt.plot(x0_list, x1_list)
plt.plot([0, 0.9], [0, 0.9]) # linha identidade
plt.xlabel('x0')
plt.ylabel('y0')

x = orbita(x0=0.1, R=3.95, maxiter=100)
for i in range(len(x)-1):
    plt.plot([x[i], x[i], x[i+1]], [x[i], x[i+1], x[i+1]], marker='o', color='red')

plt.show()


# criando um diagrama de bifurcação
R_list = np.linspace(1, 4, 1000)
transient = 1000
maxiter = 100
nponto = 0 # contador que é incrementado sempre que salvamos um novo ponto

# criamos dois arrays que salvarão os resultados obtidos
eixo_horizontal = np.zeros(len(R_list)*maxiter)
eixo_vertical = np.zeros(len(R_list)*maxiter)

for R in R_list:
    x0 = 0.2 # começamos sempre com x0=0.2

    # pulando o tempo de transiente
    for iter in range(transient):
        x0 = mapa(x0, R)

    # após pular o transiente, salvamos os pontos nos dois arrays
    # chamados eixo_horizontal e eixo_vertical
    for iter in range(maxiter):
        x0 = mapa(x0, R)

        eixo_horizontal[nponto] = R
        eixo_vertical[nponto] = x0
        nponto += 1

plt.xlabel('R')
plt.ylabel('x')
plt.plot(eixo_horizontal, eixo_vertical, 'o', markersize=0.1)
plt.show()