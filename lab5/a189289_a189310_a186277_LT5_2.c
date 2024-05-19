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
                        if (subMenu == 1) {
                            if (regularParking > 0) { // check there are still at least 1 space, to book for parking
                                regularParking--; // used to reserve parking 
                                printf("\nParking space reserved successfully!\n");
                            } else { // ensure that it does not go below negative
                                printf("\nNo available spaces in Regular Parking!\n");
                            }
                        } else if (subMenu == 2) {
                            if (disabledParking > 0) {
                                disabledParking--;
                                printf("\nParking space reserved successfully!\n");
                            } else { 
                                printf("\nNo available spaces in Disabled Parking!\n");
                            }
                        } else if (subMenu == 3) {
                            if (vipParking > 0) {
                                vipParking--;
                                printf("\nParking space reserved successfully!\n");
                            } else {
                                printf("\nNo available spaces in VIP Parking!\n");
                            }
                        } else {
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
                        if (subMenu == 1) {
                            if (regularParking < maxParking) { // check there are booked parking for the category selected
                                regularParking++; // adding back when user chooses the menu
                                printf("\nParking space released successfully!\n");
                            } else {
                                printf("\nNo reserved parking in Regular Parking!\n");
                            }
                        } else if (subMenu == 2) {
                            if (disabledParking < maxParking) {
                                disabledParking++;
                                printf("\nParking space released successfully!\n");
                            } else {
                                printf("\nNo reserved parking in Disabled Parking!\n");
                            }
                        } else if (subMenu == 3) {
                            if (vipParking < maxParking) {
                                vipParking++;
                                printf("\nParking space released successfully!\n");
                            } else {
                                printf("\nNo reserved parking in VIP Parking!\n");
                            }
                        } else {
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

