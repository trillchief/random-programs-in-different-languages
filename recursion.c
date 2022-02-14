#include <string.h>
#include <stdio.h>
#include <stdlib.h>

// 4=> 4 + 3 + 2 + 1 = 10

int f(int x)
{
    if (x == 0)
    {
        return 0;
    }
    printf("Hello from f with x = %d\n", x);
    return x + f(x - 1);
}

// return 4 + 3 + 2 + 1 = 0

int main(int argc, char *argv[])
{
    int result = f(4);
    printf("The result of calling f is %d\n", result);
    return 0;
}