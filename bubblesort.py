"""CODING FOR SECURITY - CHECKPOINT 2
1TDCG - 44SEC
Felipe de Resende Madeira - RM99228
João Victor S. Alves - RM99634
Rakel Macedo - RM99435
Pedro Henrique Lima Vieira - RM99432
Suellen Guedes Rufino - 97687"""


### HEADER

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

import time

### Definido a lista
try:
    with open("words.txt", "r") as file:
        wordlist = file.read().split(',')
        wordlist = [word.lower() for word in wordlist]
except:
    print('[!] Não foi possível importar a lista, o arqivo está na mesma pasta que o programa?')

### Criando as funcoes de ordenacao

def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def bubblesortrev(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

### Ordenando as listas e imprimindo os resultados

print('[!] Organizando as listas...')
time.sleep(2)

# BENCHMARK

start_time = time.time()

# Ordenando a lista alfabeticamente

try:
    bubblesort(wordlist)
    with open("BubbleSort.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Aqui está os 10 primeiros itens da lista ordenados alfabeticamente: {wordlist[:10]}')
except:
    print('[!] Não foi possível organizar as listas, tente novamente...')

# Ordenando a lista inversa

try:
    bubblesortrev(wordlist)
    with open("BubbleSortRev.txt", "w") as f:
        f.write(','.join(wordlist))
    print(f'[+] Aqui está os 10 primeiros itens da lista inversa: {wordlist[:10]}')
except:
     print('[!] Não foi possível organizar as listas, tente novamente...')
   
end_time = time.time()

print(f'[!] O programa demorou {round(end_time - start_time, 4)} segundo para executar o algoritmo!')
print('[INFO] A lista completa com 1000 itens está organizada em dois arquivos: BubbleSort.txt e BubbleSortRev.txt')
