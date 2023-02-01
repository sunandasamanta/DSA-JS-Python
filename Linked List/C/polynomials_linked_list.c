#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int coefficient;
    int exponent;
    struct Node *next;
};

struct Node *createNode(int coefficient, int exponent)
{
    struct Node *newNode = (struct Node *)malloc(sizeof(struct Node));
    newNode->coefficient = coefficient;
    newNode->exponent = exponent;
    newNode->next = NULL;
    return newNode;
}

struct Node *insert(struct Node *head, int coefficient, int exponent)
{
    struct Node *newNode = createNode(coefficient, exponent);
    if (head == NULL)
    {
        return newNode;
    }
    else
    {
        newNode->next = head;
        return newNode;
    }
}

struct Node *addPolynomials(struct Node *first, struct Node *second)
{
    struct Node *result = NULL;
    struct Node *temp1, *temp2;
    temp1 = first;
    temp2 = second;

    while (temp1 != NULL && temp2 != NULL)
    {
        if (temp1->exponent > temp2->exponent)
        {
            result = insert(result, temp1->coefficient, temp1->exponent);
            temp1 = temp1->next;
        }
        else if (temp1->exponent < temp2->exponent)
        {
            result = insert(result, temp2->coefficient, temp2->exponent);
            temp2 = temp2->next;
        }
        else
        {
            result = insert(result, temp1->coefficient + temp2->coefficient, temp1->exponent);
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
    }
    while (temp1 != NULL)
    {
        result = insert(result, temp1->coefficient, temp1->exponent);
        temp1 = temp1->next;
    }
    while (temp2 != NULL)
    {
        result = insert(result, temp2->coefficient, temp2->exponent);
        temp2 = temp2->next;
    }
    return result;
}

void display(struct Node *head)
{
    if (head == NULL)
    {
        printf("\nPolynomial does not exist!!\n");
    }
    else
    {
        printf("\nThe polynomial is:\n");
        while (head != NULL)
        {
            printf("%dx^%d", head->coefficient, head->exponent);
            head = head->next;
            if (head != NULL)
            {
                printf(" + ");
            }
        }
    }
}

int main()
{
    struct Node *first = NULL;
    struct Node *second = NULL;
    struct Node *result = NULL;
    int coefficient, exponent, terms;

    printf("Enter the number of terms in first polynomial: ");
    scanf("%d", &terms);
    for (int i = 0; i < terms; i++)
    {
        printf("Enter the coefficient and exponent of term %d: ", i + 1);
        scanf("%d%d", &coefficient, &exponent);
        first = insert(first, coefficient, exponent);
    }
    printf("Enter the number of terms in second polynomial: ");
    scanf("%d", &terms);
    for (int i = 0; i < terms; i++)
    {
        printf("Enter the coefficient and exponent of term %d: ", i + 1);
        scanf("%d%d", &coefficient, &exponent);
        second = insert(second, coefficient, exponent);
    }

    result = addPolynomials(first, second);

    printf("\nFirst polynomial:\n");
    display(first);
    printf("\nSecond polynomial:\n");
    display(second);
    printf("\nResult polynomial:\n");
    display(result);

    return 0;
}
