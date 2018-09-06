## QUESTÃO 4 ##
# Escreva um programa que pergunte a quantidade de km percorridos por um carro 
# alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi 
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e 
# R$ 0,15 por km rodado.

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    km = int(input("Quantidade de km percorridos: "))
    d = int(input("Quantidade de dias que o carro foi alugado: "))
    valor = (km * 0.15) + (60 * d)
    print ("Preço a pagar: ", valor, "reais.")



    
if __name__ == '__main__':
    main()
