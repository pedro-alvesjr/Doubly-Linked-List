# Doubly Linked List in Python

This project contains an implementation of a **Doubly Linked List** in Python.  
A doubly linked list is a type of linked list in which each node contains a reference to both the next and the previous node in the sequence.

## Features

- Create a new doubly linked list with an initial node
- Append nodes to the end of the list (`append`)
- Prepend nodes to the beginning of the list (`prepend`)
- Remove the last node (`pop`)
- Remove the first node (`pop_first`)
- Get a node by index (`get`)
- Set the value of a node by index (`set_value`)
- Insert a node at a specific index (`insert`)
- Remove a node at a specific index (`remove`)
- Swap the values of the first and last nodes (`swap_first_last`)
- Reverse the entire list (`reverse`)
- Check if the list is a palindrome (`is_palindrome`)
- Partition the list around a value (`partition_list`)
- Print the entire list (`print_list`)

## Example Usage

```python
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

print('Original DLL:')
my_doubly_linked_list.print_list()

print('\nIs Palindrome?', my_doubly_linked_list.is_palindrome())

my_doubly_linked_list.reverse()
print('\nDLL after reverse():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()
print('\nDLL after swap_first_last():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.partition_list(2)
print('\nDLL after partition_list(2):')
my_doubly_linked_list.print_list()


---

# Lista Duplamente Ligada em Python

Este projeto contém uma implementação de uma **Lista Duplamente Ligada** em Python.  
Uma lista duplamente ligada é um tipo de lista encadeada em que cada nó contém uma referência tanto para o próximo quanto para o nó anterior na sequência.

## Funcionalidades

- Criar uma nova lista duplamente ligada com um nó inicial
- Adicionar nós ao final da lista (`append`)
- Adicionar nós ao início da lista (`prepend`)
- Remover o último nó (`pop`)
- Remover o primeiro nó (`pop_first`)
- Obter um nó pelo índice (`get`)
- Alterar o valor de um nó pelo índice (`set_value`)
- Inserir um nó em um índice específico (`insert`)
- Remover um nó em um índice específico (`remove`)
- Trocar os valores do primeiro e do último nó (`swap_first_last`)
- Reverter toda a lista (`reverse`)
- Verificar se a lista é um palíndromo (`is_palindrome`)
- Imprimir toda a lista (`print_list`)

## Exemplo de Uso

```python
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

print('Lista original:')
my_doubly_linked_list.print_list()

print('\nÉ palíndromo?', my_doubly_linked_list.is_palindrome())

my_doubly_linked_list.reverse()
print('\nLista após reverse():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.swap_first_last()
print('\nLista após swap_first_last():')
my_doubly_linked_list.print_list()
