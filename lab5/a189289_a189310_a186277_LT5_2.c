#include <stdio.h>

int main() {
    int regularParking = 500, disabledParking = 500, vipParking = 500; //Initialize the parking of a total 500 for each category
    int maxParking=500;//each category have the 500 max parking
    int menu , subMenu; //menu for the Main menu, while subMenu is use to book parking for SELECTED category
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
        printf("Enter your choice: ");
        
        if (scanf("%d", &menu) == 1) {//ensure input is Integer
         	
	        switch (menu) {
				case 1:
					// Check Availability
					break;
				case 2:
				    //Reserve Parking 
				    printf("Select parking category (1. Regular, 2. Disabled, 3. VIP): ");
	                scanf("%d", &subMenu);
	                
	                if (subMenu == 1)
	                {
	            	  if (regularParking > 0) {
	                        regularParking--;    //used to reserved parking 
	                        printf("Parking space reserved successfully!\n");
	                    } else {
	                        printf("No available spaces in Regular Parking!\n");
	                    }
	                    subMenu=0;//clear buffer
					}
					else if (subMenu == 2)
	                {
	            	  if (disabledParking > 0) {//check there are still atleast 1 space, to book for parking
	                        disabledParking--;
	                        printf("Parking space reserved successfully!\n");
	                    } else {//ensure that it does not go below Negative
	                        printf("No available spaces in Disabled Parking!\n");
	                    }
	                    subMenu=0;//clear buffer
					}
					else if (subMenu == 3)
	                {
	            	  if (vipParking > 0) {
	                        vipParking--;
	                        printf("Parking space reserved successfully!\n");
	                    } else {
	                        printf("No available spaces in VIP Parking!\n");
	                    }
	                    subMenu=0;//clear buffer
					}
					else{
						printf("Invalid choice!\n");
						subMenu=0;//clear buffer
					}
	                
				    break;
				    
				case 3 :
				   	//Release Parking 
				    printf("Select parking category (1. Regular, 2. Disabled, 3. VIP): ");
	                scanf("%d", &subMenu);
	                
	                if (subMenu == 1)
	                {
	            	  if (regularParking < maxParking) {//check there are booked parking for the category selecetd
	                        regularParking++;   //adding back when user choose the menu
	                        printf("Parking space release successfully!\n");
	                        
	                    } else {
	                        printf("No booked parking in Regular Parking!\n");
	                    }
	                    subMenu=0;//clear buffer
					}
					else if (subMenu == 2)
	                {
	            	  if (disabledParking < maxParking) {
	                        disabledParking++;
	                        printf("Parking space release successfully!\n");
	                    } else {
	                        printf("No booked parking in Disabled Parking!\n");
	                    }
	                	subMenu=0;//clear buffer
					}
					else if (subMenu == 3)
	                {
	            	  if (vipParking < maxParking) {
	                        vipParking++;
	                        printf("Parking space release successfully!\n");
	                    } else {
	                        printf("No booked parking in VIP Parking!\n");
	                    }
	                    subMenu=0;//clear buffer
					}
					else{
						printf("Invalid choice!\n");
						subMenu=0;//clear buffer
					}
	                
				    break;
	            case 4:
	                printf("Exiting program. Thank you for using our parking management system!\n");
	                break;
				    
				default:
					printf("Invalid Menu ! You can only choose from menu 1 until menu 4 only \n");
			
			}
	    } else {
	    	 printf("Invalid input. Please enter a number.\n");
	            // Clear the input buffer to handle invalid input
	            while (getchar() != '\n');
	    }
	}while(menu != 4 );
    
    return 0;
}
