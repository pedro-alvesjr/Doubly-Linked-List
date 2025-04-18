## Doubly Linked List in Python

This project contains an implementation of a **Doubly Linked List** in Python. A doubly linked list is a type of linked list in which each node contains a reference to both the next and the previous node in the sequence.

### Features

- Create a new doubly linked list with an initial node
- Append nodes to the end of the list
- Prepend nodes to the beginning of the list
- Remove the last node (`pop`)
- Remove the first node (`pop_first`)
- Get a node by index
- Set the value of a node by index
- Print the entire list

### Example Usage

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(1, 4)

print('\nDLL after set_value():')
my_doubly_linked_list.print_list()
```

### Expected Output

```
DLL before set_value():
11
3
23
7

DLL after set_value():
11
4
23
7
```

---

## Lista Duplamente Ligada em Python

Este projeto contém uma implementação de uma **Lista Duplamente Ligada** em Python. Uma lista duplamente ligada é uma estrutura onde cada nó tem referência tanto para o próximo quanto para o nó anterior na sequência.

### Funcionalidades

- Criar uma nova lista duplamente ligada com um nó inicial
- Adicionar nós ao final da lista
- Adicionar nós ao início da lista
- Remover o último nó (`pop`)
- Remover o primeiro nó (`pop_first`)
- Obter um nó pelo índice
- Alterar o valor de um nó pelo índice
- Imprimir toda a lista

### Exemplo de Uso

my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(1, 4)

print('\nDLL after set_value():')
my_doubly_linked_list.print_list()
```

### Saída Esperada

```
DLL before set_value():
11
3
23
7

DLL after set_value():
11
4
23
7
```

