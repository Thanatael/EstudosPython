#  EXERCÍCIO 1
# lista = [2, 3, 4]
#
# for i in lista:
#     print(i ** 3)

# EXERCÍCIO 2
# palavras = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'.split()

# def resu(x):
#    return [x.upper(), x.lower(), len(x)]


# def pr(y):
#    return y


# portugal = list(map(resu, palavras))
# brasil = list(map(pr, palavras))
# print(portugal)
# print(brasil)

# EXERCÍCIO 3

# matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for i in matrix:
#     print(i)

# EXERCÍCIO 4

# lista = [0, 1, 2, 3, 4]


# def qua(x):
#     return x ** 2
#
#
# def cub(y):
#     return y ** 3
#
#
# print(list(map(qua, lista)))
# print(list(map(cub, lista)))


# EXERCÍCIO 5

# listaA = [2, 3, 4]
# listaB = [10, 11, 12]
#
#
# def tome(x, y):
#     return x ** y
#
#
# print(list(map(tome, listaA, listaB)))


# EXERCÍCIO 6

# ran = range(-5, 5)
#
#
# def gos(f):
#     if f < 0:
#         return True
#     else:
#         return False
#
#
# print(list(filter(gos, ran)))

# EXERCÍCIO 7

# a = [1, 2, 3, 5, 7, 9]
# b = [2, 3, 5, 6, 7, 8]
#
#
# def comum(t):
#     if t == fogo:
#         return True
#     else:
#         return False
#
#
# for y in b:
#     fogo = y
#     print(list(filter(comum, a)))

# EXERCÍCIO 8

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 4, "d": 5}
# dict3 = {}
#
# for chave1, chave2 in zip(dict1, dict2):
#     dict3[chave1] = dict2[chave2]
#
#
# print(dict3)

# EXERCÍCIO 9

# lista = ["a", "b", "c", "d", "e", "f", "g", "h"]
# print(lista[6:])

# EXERCÍCIO 10

# texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'
# resultado = re.findall(r'Data Science (\w+)', texto)
# print("A palavra após 'Data Science' é:", resultado[0])
