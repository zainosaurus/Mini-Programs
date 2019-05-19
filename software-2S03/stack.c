/**
	Stack (implemented with array)

	Author: Zain Tahlilkar
	Created on Feb 21/2017
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define STACKSIZE 100

// type declaration and then stack array
typedef int type;

type stack[STACKSIZE];
int top;

// method prototypes
int stackFull();
int stackEmpty();
void push(type data);
type pop();
type peek();

// pushes data onto the stack
void push(type data) {
	// error check
	if (stackFull()) {
		printf("Stack Full\n");
	}
	else {
		top++;
		stack[top] = data;
	}
}	

// pops last element
type pop() {
	if (!stackEmpty()) {
		return stack[top];
		top--;
	}
	else {
		printf("Stack empty\n");
		return 0;
	}	
}

// peek: look at last element without popping it
type peek() {
	if (!stackEmpty()) {
		return stack[top];
	}
	else {
		printf("Stack Empty\n");
		return 0;
	}
}

// checks for stack full and stack empty error cases (returns boolean)
int stackFull() {
	return (top == STACKSIZE-1);
}
int stackEmpty() {
	return (top == 0);
}

// tests the program
int main() {
	// initialize the stack
	top = -1;
	// for testing...
	int i;
	
	for (i = 0; i < 55; i++) {
		push(i*15+(1+i)*10-i*i);	// random equation to populate part of the stack
	}
	
	printf("%d\n", top);
	
	top = 99;
	push(123);
	top = 0;
	pop();
	top = 54;	//reset
	return 0;
}
