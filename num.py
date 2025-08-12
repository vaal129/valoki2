import numpy as np #np es un alias para recortar el nombre de numpy

vector = np.array([1, 2, 3, 4, 5])
print(vector)

print (vector[2])

"""Los vectores o son como las listas, no tiene  un metodo end() para agregar elementos o tienen un metodo pop() para eliminar elementos, pero si tenen metodo reshape()
 para cambiar su forma, adicionalmente despues creado no se puede cambiar el tamaño del vector. """

vector1  = np.zeros(5)
print(vector1)

vector2 = np.ones(5)
print(vector2)

vector3 = np.arange(1,10)
print("rango", vector3)

vector4 = np.linspace(1,10,5)
print("linspace", vector4)

vector5 = np.random.rand(10)
print("random", vector5)

vector6 = np.random.randint(1,10,100)
print("random int", vector6)