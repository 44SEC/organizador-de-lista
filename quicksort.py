"""CODING FOR SECURITY - CHECKPOINT 2
1TDCG - 44SEC
Felipe de Resende Madeira - RM99228
João Victor S. Alves - RM99634
Rakel Macedo - RM99435
Pedro Henrique Lima Vieira - RM99432
Suellen Guedes Rufino - 97687"""

import time

### Cabeçalho

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


# Definido a lista

with open("words.txt", "r") as file:
    wordlist = file.read().split(",")
    wordlist = [word.lower() for word in wordlist]

### Criando as funcoes de ordenacao

# Criando a fucao partition, para particionar a lista wordlist
def partition(arr, low, high):

    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# Criando a funcao que ira executar o QuickSort
def qs(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        qs(arr, low, pi-1)
        qs(arr, pi+1, high)

def rev_list(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    return arr

### Organizando as listas e imprimindo o resultado final

print('[!] Organizando as listas...')
time.sleep(2)
print('\n')

# BENCHMARK

start_time = time.time()

# Ordenando a lista alfabeticamente

qs(wordlist, 0, len(wordlist)-1)
with open("QuickSort.txt", "w") as f:
    f.write(','.join(wordlist))
print(f'[+] Aqui está os 10 primeiros itens da lista ordenada alfabeticamente: {wordlist[:10]}')

# Ordenando a lista de forma reversa

reverse_list = rev_list(wordlist)
with open("QuickSortRev.txt", "w") as f:
    f.write(','.join(wordlist))
print(f'[+] Aqui está os 10 primeiros itens da lista invertida: {reverse_list[:10]}')

end_time = time.time()

# Imprimindo o resultado

print(f'[?] O programa levou: {round(end_time - start_time, 4)} segundo para executar o algoritmo!')
print('[INFO] A lista completa com 1000 itens está organizada em dois arquivos: QuickSort.txt e QuickSortRev.txt')
