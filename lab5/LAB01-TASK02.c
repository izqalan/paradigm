#include <stdio.h>
/*
Author:
Lam Wei Long(A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah(A186277)

Looping statement use: do-while
Control statement use: switch AND else if Ladder

Special: We have validate the input must be Integer,to ensure it does not proc to infinity loop when the user enter String characater
*/

void reserveParking(int* parking, char* parkingType) {
    if (*parking > 0) {
        (*parking)--;
        printf("\nParking space released successfully!\n");
    } else {
        printf("\nNo reserved parking in %s Parking!\n", parkingType);
    }
}

void releaseParking(int* parking, char* parkingType, int maxParking) {
    if (*parking < maxParking) {
        (*parking)++;
        printf("\nParking space released successfully!\n");
    } else {
        printf("\nNo reserved parking in %s Parking!\n", parkingType);
    }
}

int main() {
    int regularParking = 500, disabledParking = 500, vipParking = 500; // Initialize the parking of a total 500 for each category
    int maxParking = 500; // each category have the 500 max parking,can change anytime
    int menu, subMenu; // menu for the Main menu, while subMenu is used for SELECTED parking operation
    printf("Welcome to the Shopping Mall Parking Management System!\n");
    
    do {
        printf("\nAvailable Parking Spaces:\n");
        printf("Regular Parking: %d spaces\n", regularParking);
        printf("Disabled Parking: %d spaces\n", disabledParking);
        printf("VIP Parking: %d spaces\n", vipParking);
        
        printf("\nMenu:\n");
        printf("1. Check Availability\n");
        printf("2. Reserve Parking\n");
        printf("3. Release Parking\n");
        printf("4. Exit\n");
        printf("\nEnter your choice: ");
        
        if (scanf("%d", &menu) == 1) { // ensure input is an integer
            switch (menu) {
                case 1:
                    // Check Availability
                    break;
                case 2:
                    // Reserve Parking 
                    printf("Select parking category (1. Regular, 2. Disabled, 3. VIP): ");
                    if (scanf("%d", &subMenu) == 1) {// ensure input is an integer
                        switch (subMenu) {
                            case 1:
                                reserveParking(&regularParking, "Regular");
                                break;
                            case 2:
                                reserveParking(&disabledParking, "Disabled");
                                break;
                            case 3:
                                reserveParking(&vipParking, "VIP");
                                break;
                            default:
                            printf("\nInvalid choice!\n");
                        }
                    } else {//invali input
                        printf("\nInvalid input. Please enter a number.\n");
                        while (getchar() != '\n'); // Clear the input buffer, in case of user input string and special character
                    }
                    break;
                    
                case 3:
                    // Release Parking 
                    printf("Select parking category to release reservation (1. Regular, 2. Disabled, 3. VIP): ");
                    if (scanf("%d", &subMenu) == 1){// ensure input is an integer
                        switch (subMenu) {
                            case 1:
                                releaseParking(&regularParking, "Regular", maxParking);
                                break;
                            case 2:
                                releaseParking(&disabledParking, "Disabled", maxParking);
                                break;
                            case 3:
                                releaseParking(&vipParking, "VIP", maxParking);
                                break;
                            default:
                                printf("\nInvalid choice!\n");
                        }
                    } else {//invalid input
                        printf("\nInvalid input. Please enter a number.\n");
                        while (getchar() != '\n'); // Clear the input buffer, in case of user input string and special character
                    }
                    break;
                
                case 4:
                    printf("Exiting program. Thank you for using our parking management system!\n");
                    break;
                    
                default:
                    printf("Invalid menu choice! You can only choose from menu 1 to 4.\n");
            }
        } else {//invalid input
            printf("\nInvalid input. Please enter a number.\n");
            while (getchar() != '\n'); // Clear the input buffer, in case of user input string and special character
        }
    } while (menu != 4);
    
    return 0;
}
