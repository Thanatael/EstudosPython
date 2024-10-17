arq1 = open("../arquivos/arquivo1.txt", "r")  # Abrir o arquivo para leitura
print(type(arq1))  # O tipo do arquivo

print(arq1.read())  # Ler o arquivo

print(arq1.tell())  # Contar o número de caracteres

print(arq1.read())  # Ler o arquivo novamente, mas como já foi lido. Não tem mais oque ler

print(arq1.seek(0, 0))  # Retorna para inicio da leitura

print(arq1.read(23))  # Lendo os primeiros 23 caracteres

print(arq1.read())  # Lendo o resto do arquivo

arq1.close()

# ========= GRAVANDO ARQUIVOS =========

arq2 = open("../arquivos/arquivo2.txt", "w")

# print(arq2.read()) -- Como o arquivo foi aberto para gravação, não pode ser aberto para leitura

arq2.write("Aprendendo a programar em python!")

arq2.close()

arq2 = open("../arquivos/arquivo2.txt", "r")

print(arq2.read())

# ==== Acrescentando ======

arq2 = open("../arquivos/arquivo2.txt", "a")  # a = append

arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")

arq2.close()

arq2 = open("../arquivos/arquivo2.txt", "r")

print(arq2.read())

arq2.seek(0, 0)

print(arq2.read())
