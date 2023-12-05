#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    int G[N+1];
    for (int i = 0; i <= N; i++) {
        G[i] = 0;
    }

    for (int i = 1; i <= N; i++) {
        scanf("%d", &G[i]);
    }

    int answer = 0;
    int num = 0;

    for (int j = 1; j <= N; j++) {
        int visited[N+1];
        for (int k = 0; k <= N; k++) {
            visited[k] = 0;
        }

        visited[j] = 1;
        int temp = 0;
        int q = j;

        while (1) {
            int x = G[q];

            if (visited[x]) {
                if (num < temp) {
                    num = temp;
                    answer = j;
                }
                break;
            }

            temp++;
            visited[x] = 1;
            q = x;
        }
    }

    printf("%d\n", answer);

    return 0;
}
