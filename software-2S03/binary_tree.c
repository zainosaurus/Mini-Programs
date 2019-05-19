/**
	Binary Tree (implemented using an array)
	Author: Zain Tahlilkar
	Created: Feb 21/2017
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100;	// max size of tree is 100, just for coding convenience

// type
typedef int type;

type tree[MAX];

// initializes array (for testing)
void init() {
	int i;
	for (i = 0; i < MAX; i++) {
		tree[i] = i;
	}
}

// returns the index of the left child of the requested node
int leftChildOf(int node) {
	if (node >= MAX) return -1;

	return (2*node + 1);
}

// returns right child
int rightChildOf(int node) {
	if (node >= MAX) return -1;

	return (2 * node + 2);
}

// returns parent
int parentOf(int node) {
	if (node <= 0) return -1;

	return (node-1)/2;	
}


