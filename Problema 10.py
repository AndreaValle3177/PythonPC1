lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
lista_resultante = [lista[i] for i in range(len(lista)) if i not in [0, 4, 5]]
print(lista_resultante)