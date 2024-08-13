def frequencia_numeros(numeros):
    frequencia = {}
    
    for numero in numeros:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1
    
    return frequencia

# Lista de números fornecida
numeros = [0, 1, 2, 0, 0, 0, 0, 0, 1, 2, 0, 0, 3, 0, 0, 1, 2, 0, 0, 1, 0, 0, 0, 2, 2, 0,0, 5, 2, 0, 1]

# Chamada da função
frequencia = frequencia_numeros(numeros)

# Impressão da tabela de frequência
print("Número | Frequência | Frequência Relativa")
total_numeros = len(numeros)
for numero in sorted(frequencia):
    frequencia_relativa = frequencia[numero] / total_numeros
    print(f"{numero:>6} | {frequencia[numero]:>10} | {frequencia_relativa:>17.5f}")