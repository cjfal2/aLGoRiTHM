#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool is_prime(int n)
{
    if (n == 1)
    {
        return false;
    }
    for (int j = 2; j <= sqrt(n); j++)
    {
        if (n % j == 0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    int test_cases;
    scanf("%d", &test_cases);

    for (int i = 0; i < test_cases; i++)
    {
        int num;
        scanf("%d", &num);

        int a = num / 2, b = num / 2;
        while (a > 0)
        {
            if (is_prime(a) && is_prime(b))
            {
                printf("%d %d\n", a, b);
                break;
            }
            else
            {
                a--;
                b++;
            }
        }
    }

    return 0;
}
