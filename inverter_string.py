def inverter_string(string):
    # Inicializa uma string vazia para armazenar o resultado
    resposta= ""

   
    for i in range(len(string) - 1, -1, -1):        #comecei o indice do ultimo caractere pegando o tamanho(length) da string e sutraindo 1 para desconsiderar a quebra de linha
        # o indice vai decrementando ate chegar a 0 q é o primeiro caracter da string
        resposta += string[i]

    return resposta

texto = input("Digite uma string: ")
texto_invertido = inverter_string(texto)
print("String invertida:", texto_invertido)