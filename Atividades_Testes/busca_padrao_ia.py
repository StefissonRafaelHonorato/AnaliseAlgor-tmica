def busca_padrao_ia(dataset, padrao_alvo):
    
    # Analisa a complexidade de tempo T(n) baseada na posição do alvo
    # n = len(dataset)
    
    n = len(dataset)

    for i in range(n):
        if dataset[i] == padrao_alvo:
            return f"Padrão encontrado na posição {i}"  # melhor caso se i=0

        # Operação primitiva: Comparação (if)

# --- Cenários ---
base_dados = [10, 20, 30, 40, 50] # n = 5

# MELHOR CASO: O alvo é o primeiro elemento (1 operação)
# T(n) = Omega(1)
print(busca_padrao_ia(base_dados, 10))

# PIOR CASO: O alvo não existe ou é o último (n operações)
# T(n) = O(n)
print(busca_padrao_ia(base_dados, 99))