# Título e Imagem de capa

<h1 align="center"> Organizador de Listas </h1>

![py](https://files.realpython.com/media/Pandas-Sort_Watermarked.63f138ec3804.jpg)

# Badges
![badge1](https://img.shields.io/badge/python-3.11-blue) ![badge2](https://img.shields.io/badge/status-aguardando%20revis%C3%A3o-yellow) ![badge3](https://img.shields.io/badge/gitstars-4-blue) ![badge4](https://img.shields.io/badge/testado%20por-44Sec-green)


# Índice 

* [Título e Imagem de capa](#título-e-imagem-de-capa)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Vídeo Explicativo](#vídeo-explicativo)
* [Status do Projeto](#status-do-projeto)
* [Os algoritmos sort](#os-algoritmos-sort)
* [Formas de organização](#formas-de-organização)
* [Contagem do tempo de execução](#contagem-do-tempo-de-execução) 
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Link de vídeo explicativo](https://youtu.be/WcaoXCMeOw4)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras-do-projeto)
* [Licença](#licença)
* [Conclusão](#conclusão)

# Descrição do Projeto

O presente projeto tem como objetivo realizar a organização de listas através de algoritmos de ordenação, sem utilizar a função "Sort". Para a composição da aplicação foram escolhidos três algoritmos que a realizam a função, retornando ao usuário uma lista organizada de forma alfanumérica.

# Vídeo Explicativo

* https://www.youtube.com/watch?v=WyYauB-P-mM

# Status do Projeto

O projeto foi desenvolvido mediante a proposta de trabalho do professor Fábio Cabrini, na disciplina "Coding for Security", como segundo "checkpoint" para a turma 1TDCG da Faculdade de Administração e Informática Paulista. Aguardando revisão e aprovação pelo docente responsável.

# Os algoritmos sort

Os algoritmos de ordenação, também conhecidos como "sort", são conjuntos de instruções que colocam os elementos em uma certa ordem. Estes buscam as informações em uma array ou lista indicada e ordenam de forma pré-definida, como alfanumérica, numérica ou alfabética.    

# Formas de organização

Existem vários algorítimos diferentes, alguns são mais apropriados para uma situação que outros. Alguns são mais eficientes para listas pequenas ou quase ordenadas, enquanto isso outros percorrem a lista e entregam o resultado mais rápido. 

# Contagem do tempo de execução

Para verificar o desempenho dos algoritmos escolhidos adicionamos a função "time". Esta conta o tempo de execução de cada um dos três algoritmos implementados no código e retorna o tempo processamento de cada um diante da lista proposta. 

# Funcionalidades e Demonstração da aplicação

## Funcionamento dos algoritmos

Os programas funcionam lendo uma wordlist .txt, criada a partir de outro arquivo utilizando um script em python (catting.py) que retira as 1000 primeiras palavras deste arquivo (No caso, as 1000 primeiras palavras da wordlist *"rockyou.txt"*) e as adiciona em um arquivo novo chamado *"words.txt"*. Os algoritmos principais começam lendo este arquivo "words.txt" e criando uma lista com as palavras contidas nele.

Foram utilizados três algoritmos para a criação deste projeto: BubbleSort, MergeSort e QuickSort.

### Bubble Sort

O algoritmo Bubble Sort é um algoritmo de ordenação simples que percorre repetidamente uma lista de itens várias vezes. A ideia é comparar os itens adjacentes e trocá-los de posição se estiverem na ordem errada. O processo de ordenação continua até que não haja mais trocas a serem feitas, o que indica que a lista está ordenada. O nome "bubble" vem da ideia de que os itens maiores "borbulham" para a parte superior da lista, enquanto os menores "afundam" para a parte inferior.

**Bubble Sort funciona em 6 passos:**

1. Inicia-se um loop que percorre toda a lista de itens;
2. Dentro deste loop, incia-se outro loop que percorre a lista novamente, comparando cada par de itens adjacentes;
3. Se o item à esquerda for maior que o item à direita, as posições são invertidas;
4. Este processo segue até o final da lista;
5. Os passos 2 e 4 são repetidos para cada item da lista;
6. Se em uma iteração completa pelo loop nenhuma troca for feita, a lista está ordenada e o algoritmo pode ser interrompido.

Bubble Sort não é um algoritmo recomendado para ordenar grandes quantidades de dados, porque sua complexidade de tempo é *O(n^2)*. Ou seja, **o tempo que o algoritmo leva para executar cresce de forma proporcional ao quadrado dos dados de entrada.** Por exemplo: caso o algoritmo esteja trabalhando com uma lista de 4 itens, supondo que o algoritmo leva 2ms para ser executado em cada item da lista, o algoritmo levaria 8^2ms para terminar de executar. Em pequenas quantidades, o Bubble Sort é suficiente, porém em grandes quantidades de dados é necessário um algoritmo mais eficiente.

### Merge Sort

Este algoritmo é eficiente porque segue a ideia de "dividir para conquistar". A ideia central é dividir a lista não ordenada em pedaços menores, ordená-los e, em seguida, combiná-los de volta em uma lista ordenada.

**Merge Sort funciona em 4 passos:**

1. A lista é dividida de forma não ordenada em duas metades iguais;
2. Repete-se o processo de divisão até que se tenha uma lista de apenas um item;
3. É combinado duas sublistas ordenadas em uma única lista ordenada. Para fazer isso, compara-se o primeiro elemento de cada sublista e o menor é inserido em uma nova lista. Em seguida, avança-se para o próximo elemento da sublista de onde o elemento foi retirado. O processo é repetido até que ambas as sublistas tenham sido completamente adicionadas à nova lista;
4. Repete-se o processo de combinação até que se tenha apenas uma lista ordenada.

A complexidade de tempo do Merge Sort é O(n log n), ou seja, ele é muito mais eficiente que o Bubble Sort, porque o tempo de execução do algoritmo aumenta de forma proporcional ao produto do tamanho dos dados de entrada. Porém, frente a um algoritmo que opera in-place, Merge Sort consome mais memória.

### Quick Sort

O algoritmo Quick Sort divide a lista de entrada em duas *partições*, recursivamente ordena essas partições e, em seguida, as mescla para produzir a lista final ordenada.

**Quick Sort funciona em 4 passos:**

1. É escolhido um elemento da lista de entrada, que será chamado de "pivô";
2. Em seguida, a lista é dividida em duas partições: uma contendo elementos menores que o pivô e outra contendo elementos maiores que o pivô;
3. Recursivamente, as duas partições são ordenadas, usando o mesmo algoritmo Quick Sort;
4. Por fim, as duas partições ordenadas são unidas para produzir a lista final.

A complexidade de tempo médio do Quick Sort é *O(n log n)*. Mesmo tendo a mesma complexidade de tempo média, Quick Sort e Merge Sort não operam na mesma velocidade por múltiplas razões. Uma dessas razões é que Merge Sort é um algoritmo que precisa criar uma lista temporária enquanto organiza a lista original, consumindo mais espaço na memória, já Quick Sort é um algoritmo in-place, por tanto não utiliza de uma estrutura de dados auxiliar, conseguindo consumir menos memória.

## Execução

* Primeiro, clone o repositório no diretório desejado, utilizando o git bash, caso esteja no Windows, ou diretamente pelo terminal Linux/MacOS, com o comando:
```
git clone https://github.com/44SEC/organizador-de-lista.git
```
* Em seguida, utilizando um terminal, vá para o diretório onde foi baixado o repositório:
```
cd /caminho/para/o/diretorio/
```
* É possível executar cada algoritmo individualmente, utilizando o comando 
```
* py {nome_do_arquivo}.py
``` 
no Windows ou 
```
* python3 {nome_do_arquivo}.py
``` 
* no Linux. No MacOS, 
```
* python {nome_do_arquivo}.py
```
* Também é possível executar um script powershell ou shellscript para executar um *benchmark* dos 3 algoritmos e exibir apenas seu tempo de execução. No Linux e MacOS, utilize o comando: 
```
* sh run.sh
```
No Windows, abra seu terminal Powershell e utilize o comando 
```
* ./run.ps1
```
* Cada algoritmo cria, no final de sua execução, um arquivo .txt na mesma pasta em que está localizado. Este arquivo .txt possuí as 1000 palavras da lista organizadas.

# Tecnologias utilizadas

Para a realização da organização das listas, utilizamos a implementação de três algoritmos de ordenação. Além disso, para contagem do tempo de execução, foi utilizado o módulo time. No código fonte da aplicação, feita em python 3.11, encontram-se funções de laço "for", "def" para definir funções,"print" para exibir mensagens ao usuário, "if" para tomada de decisões além de "try" e "execpt" para tratamento de execessão. Uma Shell Script foi criada, para a automação da execução das aplicações de ordanações, onde se rotorna o resultado de cada uma, juntamente com um script powershell que executa a mesma função no sistema Windows.

# Link de vídeao explicativo

# Pessoas Desenvolvedoras do Projeto

Felipe de Resende Madeira

João Victor Santos Alves

Rakel de Macedo Oliveira

Pedro Henrique Lima Vieira

Suellen Guedes Rufino

# Licença

 General Public License

# Conclusão

A implementação do funções de ordenação, sem a utilização do sort nos permite observar como a função funciona realmente. Com implementação de calculos matemáticos diferentes conseguismos chegar ao mesmo resultado, alterando apenas a seu tempo de processamento.   
