# Script que le as 1000 primeiras linhas da rockyou.txt e escreve elas
# em um novo arquivo .txt, separando-as por virgulas e em uma unica linha
# para facilitar a criacao da array no codigo

with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as input_file:
    with open("words.txt", "w") as f:
        words = [line.strip() for line in input_file.readlines()[:1000]]
        f.write(','.join(words))
