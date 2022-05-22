def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)): #range vai fazer uma sequência onde o primeiro elemento é o 1, definido ali, e o ultimo é o tamanho do array
        if arr[i] < menor :
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor)) #pop retira o item do array e retora ele e o append inclui ele no novo array
    return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10, 25, 1, -3, 0, 44]))