#include <stdio.h>
#include <stdlib.h>

typedef struct Queue {
    int data;
    struct Queue* next;
} Queue;

void enqueue(Queue** rear, int data) {
    Queue* new_element = (Queue*)malloc(sizeof(Queue));
    if (new_element == NULL) {
        perror("Memory allocation error");
        exit(EXIT_FAILURE);
    }

    new_element->data = data;
    new_element->next = NULL;
    if (*rear == NULL) {
        *rear = new_element;
        return;
    }
    Queue* temp = *rear;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = new_element;
}

Queue* dequeue(Queue** front) {
    if (*front == NULL) {
        printf("Error: Queue is empty\n");
        return *front;
    }
    Queue* temp = *front;
    *front = (*front)->next;
    return temp;
}

int main() {
    Queue* queue = NULL;
    enqueue(&queue, 4);
    enqueue(&queue, 5);
    enqueue(&queue, 6);
    enqueue(&queue, 2);
    dequeue(&queue);

    Queue* temp = queue;
    while (temp != NULL) {
        printf("%d -> ", temp->data); // 5 -> 6 -> 2
        temp = temp->next;
    }

    return 0;
}
