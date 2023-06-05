""" faça um algoritmo que solicite ao usuário números e 
    os armazene em um vetor de 30 posições. Crie uma função que recebe 
    o vetor preenchido e substitua todas as ocorrência de valores positivos 
    por 1 e todos os valores negativos por 0. """

print('Welcome motherfucker')
list = []
i = 0
while i <= 30:
    numbers = int(input('Enter 30 random numbers: \n'))
    list.append(numbers)
    i+=1
    for position in list:
        if position >= 0:
           positive = list.index(position)
           list[positive] = 1
        elif position < 0:
            list[position] = 0

print(list)   
