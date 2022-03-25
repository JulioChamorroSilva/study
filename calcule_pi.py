# -*- coding: utf-8 -*-
import numpy as np

print("Calculando Pi usando o método Monte Carlo")
# O Método Monte Carlo é um meio de calcular a área de uma função sem precisar integrá-la. 
# Um meio divertido de aprender o método é calculando pi
N = int(input("Escolha o número de pontos: "))
# N será o número de pontos jogados em um quadrado de lado 1
n = 0
# n será o número de pontos jogados no quadrado que cairão em um círculo de raio 1
rng = np.random.default_rng()
# O rng gera numeros aleatórios entre 0 e 1
for _ in range(N):
    x_axis = rng.random()
    y_axis = rng.random()
    if x_axis**2 + y_axis**2 =< 1.0:
        n += 1
        # Essa função calcula os pontos dentro do raio r=1 do círculo e acresce a variável n
resultado = 4.0 * n / N
# Como os calculos nesse programa ocorrem dentro do quadrante positivo da função, 
# é necessário multiplicar a razão dos valores por 4 para obter o valor correto de pi
print(f"O valor de pi é: {resultado}")
