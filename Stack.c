#include <stdio.h>

typedef struct Stack {
    int data;
    struct Stack* next;
} Stack;

void push(Stack** top, int data) {
    Stack* new_user = (Stack*)malloc(sizeof(Stack));
    new_user->data = data;
    new_user->next = *top;
    *top = new_user;
}

int pop(Stack** top){
  int temp = (*top)->data;
  *top = (*top)->next;
  return temp;
}

int main() {
    Stack* stack = NULL; 

    push(&stack, 3);
    push(&stack, 5);
    push(&stack, 4);
    push(&stack, 2);
    int popped = pop(&stack);


    Stack* current = stack;
    while (current != NULL) {
        printf("Data: %d\n", current->data);
        current = current->next;
    }
    return 0;
}
