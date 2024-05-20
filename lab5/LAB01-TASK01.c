/*
Authors:
Lam Wei Long(A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah(A186277)
*/
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    const float drinkPrice = 3.25;
    char drinkBrand[10];
    int amount;

    printf("Welcome to the Beverage Vending Machine!\n");
    printf("Please select your beverage (Coke, Pepsi, or Sprite): ");
    scanf("%s", drinkBrand);
    
    int brandLength = strlen(drinkBrand);//find the string length, for the For loop below
    // Convert the input to lowercase
    // Case insensitive string is better and easiier for string comparison and management
	for (int i = 0; i < brandLength; i++) {
        drinkBrand[i] = tolower(drinkBrand[i]);
    }

    // Check if the selected drink is valid
    if (strcmp(drinkBrand, "pepsi") == 0 || strcmp(drinkBrand, "coke") == 0 || strcmp(drinkBrand, "sprite") == 0) {
    	//strcmp() function returns 0 if the strings are equal, not 1
        printf("Please select the amount of cans to be purchased: ");//then allow to enter amount
        if (scanf("%d", &amount) == 1) {//check input is number
            if (amount < 1) {
                printf("Error: invalid amount. Amount must be higher than 0.");
            } else {
                // as the Rubric stated, MUST! use Switch statement, to determine the selected beverage and calculate the amount due
                // but it may cause problem in the future when there have some brand with same heading example: Pepsi vs Pop
                // but as for now, switch statemend is used follow the rubric
                // can use ladder if else and strcmp function for each new brand, better control as switch allow only 1 character checking
                switch (drinkBrand[0]) {
                    case 'p':
                        printf("You have selected %d Pepsi. Amount due: RM%.2f\n", amount, amount * drinkPrice);
                        break;
                    case 'c':
                        printf("You have selected %d Coke. Amount due: RM%.2f\n", amount, amount * drinkPrice);
                        break;
                    case 's':
                        printf("You have selected %d Sprite. Amount due: RM%.2f\n", amount, amount * drinkPrice);
                        break;
                    default:
                        printf("Error: Invalid option. Please select Coke, Pepsi, or Sprite.\n");
                }
            }
        } else {//input character when asking for amount
            printf("Error: Please enter a valid number.\n");
        }
    } else {//invalid drink brand
        printf("Error: Invalid option. Please select Coke, Pepsi, or Sprite.\n");
    }

    return 0;
}

