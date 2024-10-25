def analise_vendas(vendas):
    # Calcule o total de vendas e a média mensal
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Digite os valores de vendas, separados por espaço: ")
    # Converte a entrada em uma lista de inteiros
    vendas = list(map(int, entrada.split()))
    
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))
