#include <stdio.h>

int main(void) {
  int a;
  scanf("%d", &a);

  if (620 <= a && a <= 780) {
    printf("%s", "Red");
  }
  else if (590 <= a && a <= 620) {
    printf("%s", "Orange");
  }
  else if (570 <= a && a <= 590) {
    printf("%s", "Yellow");
  }
  else if (495 <= a && a <= 570) {
    printf("%s", "Green");
  }
  else if (450 <= a && a <= 495) {
    printf("%s", "Blue");
  }
  else if (425 <= a && a <= 450) {
    printf("%s", "Indigo");
  }
  else if (380 <= a && a <= 425) {
    printf("%s", "Violet");
  }

  return 0;
}
