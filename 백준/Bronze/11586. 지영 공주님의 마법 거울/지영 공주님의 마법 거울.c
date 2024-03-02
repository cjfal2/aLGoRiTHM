#include <stdio.h>
#include <string.h>

int main() {
    int N, K;
    scanf("%d", &N);
    char arr[N][101];
    
    // 문자열 입력 받기
    for (int i = 0; i < N; i++) {
        scanf("%s", arr[i]);
    }

    scanf("%d", &K);
    
    if (K == 1) {
        for (int i = 0; i < N; i++) {
            printf("%s\n", arr[i]);
        }
    } else if (K == 2) {
        for (int i = 0; i < N; i++) {
            int len = strlen(arr[i]);
            for (int j = len - 1; j >= 0; j--) {
                printf("%c", arr[i][j]);
            }
            printf("\n");
        }
    } else {
        for (int i = N - 1; i >= 0; i--) {
            printf("%s\n", arr[i]);
        }
    }

    return 0;
}
