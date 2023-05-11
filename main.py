# Definir a matriz
matriz = [[0, 1, 0, 0, 0, 0], [0, 0.2, 0.8, 0, 0, 0], [0, 0, 0.4, 0.6, 0, 0],
          [0, 0, 0, 0.6, 0.4, 0], [0, 0, 0, 0, 0.8, 0.2], [0, 0, 0, 0, 0, 1]]


# Função para calcular a potência de uma matriz
def potencia_matriz(matriz, expoente):
  linhas, colunas = len(matriz), len(matriz[0])

  # Verificar se a matriz é quadrada
  if linhas != colunas:
    print("Matriz não é quadrada.")
    return None

  # Criar matriz identidade do mesmo tamanho da matriz
  matriz_resultado = [[0] * colunas for _ in range(linhas)]
  for i in range(linhas):
    matriz_resultado[i][i] = 1

  # Calcular a potência da matriz
  for _ in range(expoente):
    nova_matriz = [[0] * colunas for _ in range(linhas)]
    for i in range(linhas):
      for j in range(colunas):
        for k in range(colunas):
          nova_matriz[i][j] += matriz[i][k] * matriz_resultado[k][j]
    matriz_resultado = nova_matriz

  return matriz_resultado


# Função para calcular a probabilidade de estar em um estado após n passos
def probabilidade_apos_n_passos(matriz, estado_inicial, n):
  linhas, colunas = len(matriz), len(matriz[0])

  # Verificar se o vetor de estado inicial tem o tamanho correto
  if len(estado_inicial) != linhas:
    print("Vetor de estado inicial inválido.")
    return None

  # Calcular a matriz de transição de estados elevada a n
  matriz_n = potencia_matriz(matriz, n)

  # Calcular o vetor de probabilidades após n passos
  resultado = [0] * linhas
  for i in range(linhas):
    for j in range(colunas):
      resultado[i] += estado_inicial[j] * matriz_n[j][i]

  return resultado


# Função para calcular a probabilidade de estar em um estado após n passos
def probabilidade_apos_n_passos(matriz, estado_inicial, n):
  linhas, colunas = len(matriz), len(matriz[0])

  # Verificar se o vetor de estado inicial tem o tamanho correto
  if len(estado_inicial) != linhas:
    print("Vetor de estado inicial inválido.")
    return None

  # Calcular a matriz de transição de estados elevada a n
  matriz_n = potencia_matriz(matriz, n)
  # Calcular o vetor de probabilidades após n passos
  resultado = [0] * linhas
  for i in range(linhas):
    for j in range(colunas):
      resultado[i] += estado_inicial[j] * matriz_n[j][i]

  return resultado


# Calcular a potência da matriz
expoente = int(input("Digite o expoente da matriz: "))
resultado = potencia_matriz(matriz, expoente)
if resultado is not None:
  # Imprimir o resultado com duas casas decimais
  print(f"\nMatriz P{expoente}:")
  for linha in resultado:
    print([round(valor, 2) for valor in linha])


def calc_prob_miniaturas():
  # matriz de transição
  matriz_transicao = [[0, 1, 0, 0, 0, 0], [0, 0.2, 0.8, 0, 0, 0],
                      [0, 0, 0.4, 0.6, 0, 0], [0, 0, 0, 0.6, 0.4, 0],
                      [0, 0, 0, 0, 0.8, 0.2], [0, 0, 0, 0, 0, 1]]

  # estado inicial
  estado_atual = [1, 0, 0, 0, 0]  # representando X0 = 0

  # calcular a probabilidade usando a matriz de transição
  probabilidade = estado_atual[0] * matriz_transicao[0][1] * matriz_transicao[
    1][2] * matriz_transicao[2][3] * matriz_transicao[3][4]

  return probabilidade


probabilidade = calc_prob_miniaturas()
print("\nA probabilidade de P(𝑋5 =2,𝑋10 =3,𝑋15 =4,𝑋20=5|𝑋0 =0) é",
      probabilidade)
