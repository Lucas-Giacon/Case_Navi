#cria o dicionario
Classe={}
#criar vetor
guarda=[]
j=0
#loop para variar de 0 a 5
for i in range(0,5):
    #pede ao usuario para colocar as informações desejadas
    Aluno = input("Informe o nome do aluno e sobrenome (caso haja nome igual): ")
    Nota = input("Informe a nota: ")
    #Coloca os valores do usuario no dicionario classe
    #nota dos alunos entra como int
    Classe.update({Aluno:int(Nota)}) 
#cria dois vetores
Vetor_indice=[]
Vetor_valores=[]
#vetor recebe os indices do dicionario
#recebe como tuple para eles não poderem ser alterados
Vetor_indice=tuple(Classe)
#vetor recebe os valores do dicionario
#recebe como tuple para eles não poderem ser alterados
Vetor_valores=tuple(Classe.values())
#Mostra a maior nota que existe no dicionario
Maior_nota=max(Classe.values())
#estrutura loop para variar de acordo com o tamanho do vetor c
for i in range(0, len(Vetor_valores)):
    #caso o valor do vetor c na posição i seja igual ao valor a, entra nesse bloco
    if Vetor_valores[i]==Maior_nota:
        #guarda a posição (valor i) na variavel guarda
        #guardar mais de uma posição, caso exista
        guarda.insert(j, i)
        j+=1
    else :
        continue
#loop para caso exista mais de um aluno com a maior nota
for j in range(len(guarda)):
    #apresenta valores
    #como o tamanho e a posição dos dois vetores sera a mesma
    # logo a posição da nota sera a mesma do nome do aluno
    # Chamo isso atravez da variavel guarda
    print("O aluno com a maior nota é: " + str(Vetor_indice[guarda[j]]) + ", a sua nota é: " + str(Vetor_valores[guarda[j]]))