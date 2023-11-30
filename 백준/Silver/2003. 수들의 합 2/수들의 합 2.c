#include <stdio.h>

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    int arr[10001] = {0};
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    int cnt = 0;
    for (int start = 0; start < n; start++)
    {
        int sum = 0;
        for (int end = start; end < n; end++)
        {
            sum += arr[end];
            if (sum == m)
            {
                cnt++;
                break;
            }
            else if (sum > m)
            {
                break;
            }
        }
    }
    printf("%d", cnt);

    return 0;
}
