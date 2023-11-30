#include <stdio.h>
#include <stdlib.h>

void quick_sort(int arr[], int left, int right) {
    int i = left, j = right;
    int pivot = arr[(left + right) / 2];
    int temp;

    while (i <= j) {
        while (arr[i] > pivot)
            i++;
        while (arr[j] < pivot)
            j--;
        if (i <= j) {
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    if (left < j)
        quick_sort(arr, left, j);
    if (i < right)
        quick_sort(arr, i, right);
}

int main() {
    int n, v[100000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &v[i]);

    quick_sort(v, 0, n - 1);

    long long ans = 0;
    for (int i = 0; i < n; i++)
        ans += (v[i] - i > 0) ? v[i] - i : 0;
    printf("%lld\n", ans);

    return 0;
}
