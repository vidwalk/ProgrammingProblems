#include "list.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/*
 * This is your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to 
get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
 */

typedef struct node {
	int item;
	struct node * np;
} node;

node * head, *tail;

node *xor(node *a, node *b)
{
	// We need to convert the pointers into ints before performing the XOR function
	return (node*)((uintptr_t)a ^ (uintptr_t)b);
}

void insert(int item, bool at_tail)
{
	//Allocate space for the node and add the item
	node *ptr = (node*)malloc(sizeof(node));
	ptr->item = item;

	if (NULL == head) {
		// If there is no head, we will make the tail and head have the same value
		ptr->np = NULL;
		head = tail = ptr;
	}
	else if (at_tail) {
		//The new element in the list has the XOR between the tail and NULL because there is no item after it
		ptr->np = xor (tail, NULL);
		//The tail now has the XOR value between the pointer and the following value that has just been added
		tail->np = xor (ptr, xor (tail->np, NULL));
		//We add the pointer at the end
		tail = ptr;
	}
	else {
		//The new element in the list has the XOR between the NULL and head because there is no item before it
		ptr->np = xor (NULL, head);
		//The head now has the XOR value between the pointer and the following value that has just been added
		head->np = xor (ptr, xor (NULL, head->np));
		//We add the pointer at the start
		head = ptr;
	}
}

int delete(bool from_tail)
{
	if (NULL == head) {
		//If there is no head, we have an empty list
		printf("Empty list.\n");
		exit(1);
	}
	else if (from_tail) {

		//We start from the tail, so we will point there
		node *ptr = tail;
		//Save the item from were we currently point
		int item = ptr->item;
		//The previous pointer will point to the previous one to the tail
		node *prev = xor (ptr->np, NULL);
		//If it is null, then the head is null
		if (NULL == prev) head = NULL;
		//Else change to the XOR between the tail and the XOR between were the previous pointed and NULL => the last node will point to the previous one
		else prev->np = xor (ptr, xor (prev->np, NULL));
		//tail now receives the pointer previous to it
		tail = prev;
		//free the tail
		free(ptr);
		ptr = NULL;
		return item;
	}
	else {
		//we start from the head
		node *ptr = head;
		//save the value
		int item = ptr->item;
		//find the next
		node *next = xor (NULL, ptr->np);
		//if there is no next, tail is null
		if (NULL == next) tail = NULL;
		//find the next by calculating the XOR between the head and xor from the next one(between head and the next value to it) which will result in the the next pointing to the next following it
		else next->np = xor (ptr, xor (NULL, next->np));
		head = next;
		//free the space
		free(ptr);
		ptr = NULL;
		return item;
	}
}

void list()
{
	node *curr = head;
	node *prev = NULL, *next;
	//Go through the whole list while printing the elements
	while (NULL != curr) {
		printf("%d ", curr->item);
		//The next will point to the xor of the previous and were the current points
		next = xor (prev, curr->np);
		//We swap the previous with the current and the current with the next
		prev = curr;
		curr = next;
	}

	printf("\n");
}

node* get(int index)
{
	node *curr = head;
	node *prev = NULL, *next;
	int i = 0;
	// Go through the list to find the node at the index provided. 
	//If the index is outside the possible values, it returns the last element in the list
	while (NULL != curr && index != i) {
		next = xor (prev, curr->np);
		prev = curr;
		curr = next;
		i++;
	}
	return curr;
}

int main(int argc, char *argv[])
{
	for (int i = 1; i <= 10; i++)
		insert(i, i < 6);

	list(); // 10 9 8 7 6 1 2 3 4 5

	for (int i = 1; i <= 4; i++)
		delete(i < 3);

	list(); // 8 7 6 1 2 3

	insert(get(3)->item, true);

	list(); // 8 7 6 1 2 3 1
}