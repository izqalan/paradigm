#include <stdio.h>
#include <string.h>

struct drink {
  char type[7];
  float price;
};

int main() {

  struct drink drinks[3];
  char drinkTypes[3][10] = {"coke", "sprite", "pepsi"};
  const float DRINK_PRICE = 3.25;
  char selectedDrink[10];
  int amount;
  
  for (int i = 0; i < 3; i++) {
    // OVERENGINEEEEERING
    strcpy(drinks[i].type, drinkTypes[i]);
    drinks[i].price = DRINK_PRICE;
  }

  printf("Choose your drink (coke, sprite, pepsi): ");
  scanf("%s", selectedDrink);

  if (strcmp(selectedDrink, "coke") && strcmp(selectedDrink, "pepsi") && strcmp(selectedDrink, "sprite")) {
    printf("Error: Invalid option. Please select Coke, Pepsi, or Sprite\n");
    return 0;
  } 

  printf("Please select the amount of cans to be purchased: ");
  scanf("%d", &amount);

  if (amount < 1){
    printf("Error: invalid amount. Amount must be higher than 0.");
    return 0;
  }

  printf("You have selected %d %s. Amount due is RM%.2f", amount, selectedDrink, amount * DRINK_PRICE);

  return 0;
}
