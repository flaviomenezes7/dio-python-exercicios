matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)


# Acessando:
print(matriz[0])  # resultado: (1, "a", 2) 
print(matriz[0][0])  # resultado: 1
print(matriz[0][-1])  # resultado: 2
print(matriz[-1][-1])  # resultado: "c"