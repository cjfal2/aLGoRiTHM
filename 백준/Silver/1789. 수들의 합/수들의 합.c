#include <stdio.h>

int main(void) {
  long long int S, now = 1, total = 0;
  int ans = 0;
  scanf("%lld", &S);

  while (1) {
    total += now;
    ans++;
    if (total > S) {
      ans--;
      break;
    }
    else {
      now += 1;
    }
  }
  printf("%d", ans);
  return 0;
}
