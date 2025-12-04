s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
s3 = {1, 2}

uniao = s1 | s2

print(uniao) # {1, 2, 3, 4, 5, 6}

interseccao = s1 & s2

print(interseccao) # {3, 4}

diferenca = s1 - s2

print(diferenca) # {1, 2}

diferenca_simetrica = s1 ^ s2

print(diferenca_simetrica) # {1, 2, 5, 6}

is_subset = s3.issubset(s1)

print(is_subset) # True

is_superset = s1.issuperset(s3)

print(is_superset) # True
