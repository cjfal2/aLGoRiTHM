#include <stdio.h>

int main() {
    int t;
    scanf("%d", &t);

    int memo[10001];
    for (int i = 0; i <= 10000; i++) {
        memo[i] = 1;
    }

    for (int i = 2; i <= 10000; i++) {
        memo[i] += memo[i - 2];
    }

    for (int j = 3; j <= 10000; j++) {
        memo[j] += memo[j - 3];
    }

    for (int k = 0; k < t; k++) {
        int num;
        scanf("%d", &num);
        printf("%d\n", memo[num]);
    }

    return 0;
}
