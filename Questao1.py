#declara variavel w, dar valor zero para ela
w=0
#loop para variar de 1 a 5milhões
for i in range(1, 5000000):
    #condicional, caso o resto da divizão de i por 2, 37 e 49 for zero entra no bloco
    if(i%2==0 and i%37==0 and i%49==0):
        #soma mais um na variavel w, usada para contar quantas vezes entra nesse bloco
        w=w+1
        #vai determinar quantos numeros seguem a regra
    #caso não entra nesse bloco e continua no loop
    else:
        continue
#apresentará o resultado
print("No intervalo de 1 a 5 milhões existe "+ str(w) + " números pares, multiplos de 37 e multiplos de 49")