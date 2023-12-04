#include <stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    long long dp[36] = {0};
    dp[0] = 1;
    for (int i = 0; i < N + 1; i++)
    {
        for (int j = 0; j < i; j++)
        {
            dp[i] += dp[j] * dp[i - j - 1];
        }
    }
    printf("%lld", dp[N]);
    return 0;
}
