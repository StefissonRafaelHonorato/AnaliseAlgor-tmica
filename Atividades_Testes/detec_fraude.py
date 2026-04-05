def detectar_fraude_simples(transacoes, limite):

    # Analisa uma lista de transações para encontrar valores suspeitos

    # T(n) = Custo total de operações primitivas
    # n = len(transações)

    contador = 0    # 1 operação (atribuição)

    for i in range(len(transacoes)):    # n vezes (atribuição + comparação + incremento)
        if transacoes[i] > limite:    # 1 operação (acesso) + 1 (comparação)
            contador += 1      # 1 operação (soma) + 1 (atribuição)

    return contador     # 1 operação (retorno)

"""
Nesse código, se n = 1000, o laço for executará suas operações internas mil vezes
Se o processador for um intel i9, ele faz isso em nanossegundos
Se for um arduíno, levará milissegundos
Mas para ambos, o T(n) é linear:

aproximadamente c vezes n

Esse algoritmo tem um comportamento temporal linear
Ou seja, seu tempo de execução cresce linearmente conforme a quantidade de dados
MAS nem todos algoritmos são assim.
Para entendê-los melhor, vamos estudar as 3 classes principais da Análise Assintótica

"""