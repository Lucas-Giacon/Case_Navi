#importar bibliotaca para executar calculos de ln
import math
#declaração de variaveis
j=1
#declaração do vetor
Vetor=[]

i=0
fat=1
#estrutura de loop, para enquanto i for menor que 10
while i<10:
    #condicional, entra quando o resto da divizão por 2 for igual a zero, entra no bloco
    #portanto, caso seja par entra nesse bloco
    if (i%2==0):
        #loop para fazer conta de fatorial
        # sai do loop enquanto j for menor ou igual a i
        while j<=i:
            #conta de fatorial
            fat = fat*j
            j+=1
        #Inserindo novos valores ao vetor 
        Vetor.insert(i, 3**i + 7*(fat))
    #caso seja impar entra nesse bloco
    else:
        #Inserindo novos valores ao vetor 
        Vetor.insert(i, 2**i + 4*(math.log(i)))

    i+=1
#apresenta os resultados
print( "O valor máximo encontrado no vetor é: " + str(max(Vetor)))
#Faz a conta da media pela soma dos valores do vetor dividido pelo seu tamanho
med = sum(Vetor)/len(Vetor)
#apresenta resultados
print("A media do números é: " + str(med))