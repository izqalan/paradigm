#include <stdio.h>

int main() {
  int rows;
 
 do {
    printf("Enter the number of rows for the pattern (must not be negative): ");
    scanf("%d", &rows);
  } while (rows < 1);

  for (int i = 0; i < rows; i++) {
    // add paddding for triangle 
    for (int j = 0; j < rows - i; j++) {
      printf(" ");
    }

    // add sub pattern
    for (int j = 0; j < i; j++) {
      printf("*%%");
    }

    // always end pattern with an '*'
    printf("*\n");
  }

  return 0;
}