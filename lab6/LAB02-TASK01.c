/*
Authors:
Lam Wei Long (A189310)
Izqalan Nor'Izad (A189289)
Nuruddin Naim Bin Abu Hanifah (A186277)
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DAYS_IN_A_WEEK 7 //if want to change to monthly , then just change here to 30,but maybe the variable name is not that suitable

struct Employee {
    int id;
    char name[50];
    float *sales;  // Pointer to dynamically allocated sales array
    float totalSales;
};

void inputSales(struct Employee *employees, int numEmployees) {
	//requirement5: Function inputSales correctly inputs sales data for each employee.
    for (int i = 0; i < numEmployees; i++) {
        printf("\n\nEnter details for Employee %d:\n", i + 1);
        
        // Input validation for ID,check it must be integer
        printf("ID: ");
        while (scanf("%d", &employees[i].id) != 1) {
            printf("Error: Invalid input for ID. Please enter a valid integer.\n");
            // Clear input buffer
            while (getchar() != '\n');
            printf("ID: ");
        }
        
        while (getchar() != '\n');  // Clear input buffer after reading ID

        printf("Name: ");
        fgets(employees[i].name, sizeof(employees[i].name), stdin);
        
 		// Remove newline character if found, this is needed because name can have space and it may cause error to skip newline
        int len = strlen(employees[i].name);
        if (len > 0 && employees[i].name[len - 1] == '\n') {
            employees[i].name[len - 1] = '\0';
        }

        employees[i].sales = (float *)malloc(DAYS_IN_A_WEEK * sizeof(float)); //allocate needed memory, multiply by the days
        if (employees[i].sales == NULL) {
            printf("Error: Memory allocation for sales data failed\n");
            exit(1);
        }

		// Input validation for sales,check it must be number
        printf("Enter sales for each day of the week: \n");
        for (int j = 0; j < DAYS_IN_A_WEEK; j++) {
            printf("Day %d: ", j + 1);
            while (scanf("%f", &employees[i].sales[j]) != 1) {
                printf("Error: Invalid input for sales amount. Please enter a valid number.\n");
                // Clear input buffer
                while (getchar() != '\n');
                printf("Day %d: ", j + 1);
            }
        }
    }
}

void calculateTotalSales(struct Employee *employees, int numEmployees) {//find sales for each employee
    for (int i = 0; i < numEmployees; i++) {
        employees[i].totalSales = 0;
        for (int j = 0; j < DAYS_IN_A_WEEK; j++) {
            employees[i].totalSales += employees[i].sales[j];
        }
    }
}

float calculateOverallTotalSales(struct Employee *employees, int numEmployees) {//find grand total sale of ALL employee
    float overallTotal = 0;
    for (int i = 0; i < numEmployees; i++) {
        overallTotal += employees[i].totalSales;
    }
    return overallTotal;
}

struct Employee* findEmployeeWithHighestSales(struct Employee *employees, int numEmployees) {//find top sale employee
    if (numEmployees == 0) {
        return NULL;
    }

    struct Employee *topSaleEmployee = &employees[0];//we set the first employee as the highest sale first,then compare other
    for (int i = 1; i < numEmployees; i++) {// start from index1(second employee)
        if (employees[i].totalSales > topSaleEmployee->totalSales) {
            topSaleEmployee = &employees[i];//if found more,  then pointer point to the employee with higest sale
        }
    }
    return topSaleEmployee;
}

int main() {
    int numEmployees;
    
    printf("Welcome to the Sales Tracking System!\n\n");
    
    do {// Input validation for loop
        printf("Enter the number of employees: ");
        if (scanf("%d", &numEmployees) != 1 || numEmployees <= 0) {//check is integer , and more than 0
            // Clear input buffer in case of invalid input
            while (getchar() != '\n');
            printf("Invalid input. Please enter a positive integer.\n");
        }
    } while (numEmployees <= 0);
    
    struct Employee *employees = (struct Employee *)malloc(numEmployees * sizeof(struct Employee));
    //Requirement 1: malloc function is used to allocate memory for an array of Employee structures
    //we find the total size needed by the formula: number of employee multiply with the size of the Employee structure
    //and the result is return back the the pointer *employees
    
    if (employees == NULL) {
        printf("Error: Memory allocation failed\n");
        return 1;
    }//Requirement 2: Properly handles scenarios where memory allocation fails due to insufficient memory

    inputSales(employees, numEmployees);
    calculateTotalSales(employees, numEmployees);

	printf("\n\n");
 	for (int i = 0; i < numEmployees; i++) {
        printf("Total Sales for Employee %d (%s): RM%.2f \n",
               i + 1, employees[i].name, employees[i].totalSales);
    }

    float overallTotalSales = calculateOverallTotalSales(employees, numEmployees);
    printf("\nOverall Total Sales for the Week: RM%.2f\n", overallTotalSales);

    struct Employee *topSaleEmployee = findEmployeeWithHighestSales(employees, numEmployees);
    if (topSaleEmployee != NULL) {
        printf("\nEmployee with Highest Sales:\nID: %d\nName: %s\nTotal Sales: RM%.2f\n",
               topSaleEmployee->id, topSaleEmployee->name, topSaleEmployee->totalSales);
    }

    for (int i = 0; i < numEmployees; i++) {
        free(employees[i].sales);
    }//requirement 3: Properly deallocates memory for the sales array of each employee

    free(employees);
    //Requirement 4: Properly deallocates memory for the array of Employee structures
    
    printf("\n\nThank you for using our Sales Tracking System!\n");
    return 0;
}

