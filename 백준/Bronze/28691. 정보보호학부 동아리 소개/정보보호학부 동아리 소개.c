#include <stdio.h>

int main(void) {
  char a;
  scanf(" %c", &a); // 공백을 추가하여 개행 문자를 무시합니다.

  if (a == 'M') {
    printf("%s\n", "MatKor"); // 문자열을 출력하기 위해서는 %s를 사용합니다.
  }
  else if (a == 'W') {
    printf("%s\n", "WiCys");
  }
  else if (a == 'C') {
    printf("%s\n", "CyKor");
  }
  else if (a == 'A') {
    printf("%s\n", "AlKor");
  }
  else {
    printf("%s\n", "$clear");
  }

  return 0;
}
