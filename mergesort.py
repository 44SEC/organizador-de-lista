"""CODING FOR SECURITY - CHECKPOINT 2
1TDCG - 44SEC
Felipe de Resende Madeira - RM99228
João Victor S. Alves - RM99634
Rakel Macedo - RM99435
Pedro Henrique Lima Vieira - RM99432
Suellen Guedes Rufino - 97687"""

import time


### Header


print("------------------//-------------------")
print("BEM-VINDO(A) AO ORDENADOR DE LISTAS!")
print("""
   _____    _____  _____________________________  
  /  |  |  /  |  |/   _____/\_   _____/\_   ___ \ 
 /   |  |_/   |  |\_____  \  |    __)_ /    \  \/ 
/    ^   /    ^   /        \ |        \\     \____
\____   |\____   /_______  //_______  / \______  / 
     |__|     |__|       \/         \/         \/
    """)
print("------------------//-------------------")


# Definindo a lista

try:
    with open("words.txt", "r") as file:
        wordlist = file.read().split(",")
        wordlist = [word.lower() for word in wordlist]
except:
    print('[!] Não foi possível importar a lista, o arquivo está na mesma pasta que o programa?')

### Criando a funcao de ordenacao

def mergesort(arr):
    left_half = []  # Criando as listas que separam o array original
    right_half = []
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesort(left_half)
        mergesort(right_half)

    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j+=1
        k+=1

    while i < len(left_half):
        arr[k] = left_half[i]
        i+=1
        k+=1

    while j < len(right_half):
        arr[k] = right_half[j]
        j+=1
        k+=1

# Funcao reversa
def mergesortrev(arr):
    left_half = []  # Criando as listas que separam o array original
    right_half = []
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergesortrev(left_half)
        mergesortrev(right_half)

    
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j+=1
        k+=1

    while i < len(left_half):
        arr[k] = left_half[i]
        i+=1
        k+=1

    while j < len(right_half):
        arr[k] = right_half[j]
        j+=1
        k+=1



### Executando as funcoes e imprimindo os resultados

print('[!] Organizando as listas...')
time.sleep(2)    # Aguarda por 2 segundos
print('\n')

# BENCHMARK

start_time = time.time()

# Executando a lista alfabeticamente

try:
    mergesort(wordlist)
    with open("MergeSort.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Os 10 primeiros itens da lista ordenada alfabeticamente: {wordlist[:10]} (...)')
except:
    print('[!] Não foi possível organizar as listas, tente novamente...')

# Executando a lista alfabeticamente invertida

try:
    mergesortrev(wordlist)
    with open("MergeSortRev.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Os 10 primeiros itens da lista ordenada invertida: {wordlist[:10]} (...)')
except:
     print('[!] Não foi possível organizar as listas, tente novamente...')
   

end_time = time.time()

# Imprimindo o resultado final
print(f'[?] O programa demorou {round(end_time - start_time, 4)} segundo para executar o algoritmo!')
print('[INFO] A lista completa com 1000 itens está organizada em dois arquivos: MergeSort.txt e MergeSortRev.txt')
