from Deque import *

de = Deque(10)

de.insertRight(1)
de.insertRight(7)
de.insertRight(9)
de.insertRight(5)
de.insertRight(4)


print('Contenido de cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()

de.insertLeft(4)

print('Contenido de la cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()


de.removeLeft()


print('Contenido de la cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()


de.removeRight()


print('Contenido de la cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()

de.removeRight()

print('Contenido de la cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()


de.removeRight()

print('Contenido de la cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()

de.removeLeft()


print('Contenido de la cola doble:', end=' ')
for i in range(de.size):
    print(de.items[(de.front + i) % de.capacity], end=' ')
print()


print('El primer elemento de la cola doble:', de.peekLeft())


print('El último elemento de la cola doble:', de.peekRight())


print('La cola doble está vacía?', de.isEmpty())


print('La cola doble está llena?', de.isFull())