#include <stdio.h>

int main()
{
    int N, a, b, x, answer;
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        scanf("%d %d %d", &a, &b, &x);
        answer = a * (x - 1) + b;
        printf("%d\n", answer); // 결과 출력 후 줄바꿈 추가
    }
    return 0;
}
