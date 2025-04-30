#include <stdio.h>
#include <stdlib.h>
#define MAX 100

typedef struct {
    int data[MAX];
    int top;
} Stack;

void initStack(Stack *s) {
    s->top = -1;
}

int isEmptyStack(const Stack *s) {
    return s->top == -1;
}

int isFullStack(const Stack *s) {
    return s->top == MAX - 1;
}

void push(Stack *s, int value) {
    if (isFullStack(s)) {
        printf("\nErro: Pilha cheia.");
        return;
    }
    s->data[++s->top] = value;
    printf("\nValor %d empilhado.", value);
}

int pop(Stack *s) {
    if (isEmptyStack(s)) {
        printf("\nErro: Pilha vazia.");
        return -1;
    }
    int val = s->data[s->top--];
    printf("\nValor %d desempilhado.", val);
    return val;
}

int peek(const Stack *s) {
    if (isEmptyStack(s)) {
        printf("\nPilha vazia.");
        return -1;
    }
    return s->data[s->top];
}

void displayStack(const Stack *s) {
    if (isEmptyStack(s)) {
        printf("\nPilha vazia.");
        return;
    }
    printf("\nConteúdo da pilha:");
    for (int i = 0; i <= s->top; i++) {
        printf("\n%d ", s->data[i]);
    }
    printf("\n");
}

typedef struct {
    int data[MAX];
    int front, rear, size;
} Queue;

void initQueue(Queue *q) {
    q->front = 0;
    q->rear = -1;
    q->size = 0;
}

int isEmptyQueue(const Queue *q) {
    return q->size == 0;
}

int isFullQueue(const Queue *q) {
    return q->size == MAX;
}

void enqueue(Queue *q, int value) {
    if (isFullQueue(q)) {
        printf("\nErro: Fila cheia.");
        return;
    }
    q->rear = (q->rear + 1) % MAX;
    q->data[q->rear] = value;
    q->size++;
    printf("\nValor %d enfileirado.", value);
}

int dequeue(Queue *q) {
    if (isEmptyQueue(q)) {
        printf("\nErro: Fila vazia.");
        return -1;
    }
    int val = q->data[q->front];
    q->front = (q->front + 1) % MAX;
    q->size--;
    printf("\nValor %d desenfileirado.", val);
    return val;
}

int frontQueue(const Queue *q) {
    if (isEmptyQueue(q)) {
        printf("\nFila vazia.");
        return -1;
    }
    return q->data[q->front];
}

void displayQueue(const Queue *q) {
    if (isEmptyQueue(q)) {
        printf("\nFila vazia.");
        return;
    }
    printf("\nConteúdo da fila:");
    int count = q->size;
    int idx = q->front;
    while (count--) {
        printf("\n%d ", q->data[idx]);
        idx = (idx + 1) % MAX;
    }
    printf("\n");
}

void menu() {
    printf("\n=== Menu === " );
    printf("\n1. Push na Pilha " );
    printf("\n2. Pop da Pilha " );
    printf("\n3. Mostrar Pilha " );
    printf("\n4. Enqueue na Fila " );
    printf("\n5. Dequeue da Fila " );
    printf("\n6. Mostrar Fila " );
    printf("\n7. Sair " );
    printf("\nEscolha uma opção: " );
}

int main() {
    Stack s;
    Queue q;
    initStack(&s);
    initQueue(&q);

    int opcao, valor;
    do {
        menu();
        if (scanf("%d", &opcao) != 1) break;
        switch (opcao) {
            case 1:
                printf("\nValor a empilhar:");
                scanf("%d", &valor);
                push(&s, valor);
                break;
            case 2:
                pop(&s);
                break;
            case 3:
                displayStack(&s);
                break;
            case 4:
                printf("\nValor a enfileirar:");
                scanf("%d", &valor);
                enqueue(&q, valor);
                break;
            case 5:
                dequeue(&q);
                break;
            case 6:
                displayQueue(&q);
                break;
            case 7:
                printf("\nEncerrando..");
                break;
            default:
                printf("\nOpção inválida. Tente novamente.");
        }
    } while (opcao != 7);

    return 0;
}