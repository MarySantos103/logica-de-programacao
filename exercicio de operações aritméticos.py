def calcular_peso_ideal(altura):
    peso_ideal=(72.7*altura)-58
    return peso_ideal
altura=float(input("digite sua altura em metros:"))
peso_ideal=calcular_peso_ideal(altura)
print("seu peso ideal e:",peso_ideal,"quilogramas")
