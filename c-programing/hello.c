#include <stdio.h>

void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void)
{
    int a,b;
    printf("Input two natuarl numbers: ");
    scanf("%d %d", &a,&b);

    printf("Original: %d %d\n",a,b);
    swap(&a,&b);
    printf("Swapped: %d %d\n",a,b);
    return 0;
}