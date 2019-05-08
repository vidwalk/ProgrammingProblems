#pragma once
#include <stdbool.h>
typedef struct node node;

node *xor(node *a, node *b); //Perform xor on the two nodes
void insert(int item, bool at_tail); // Adds an item to the list based on the bool
void list(); // print all items
int delete(bool from_tail); //Returns the item if deleted
//Returns a node in the list at the index !! Returns last value in the list if the index is outside of the bounds
node* get(int index);

