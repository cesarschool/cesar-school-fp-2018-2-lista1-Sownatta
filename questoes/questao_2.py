## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    celsius = float(input("Temperatura em ºC: "))
    tf = (celsius/5) * 9 + 32
    print ("Temperatura em Fahrenheit é igual a: ", tf)




if __name__ == '__main__':
    main()
