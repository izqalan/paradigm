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
    float sales[DAYS_IN_A_WEEK];
    float totalSales;
};

// Requirements states inputSales only take one parameter which is a pointer to an Employee structure
void inputSales(struct Employee *employees) {
        
    // Input validation for ID,check it must be integer
    printf("ID: ");
    while (scanf("%d", &employees->id) != 1) {
        printf("Error: Invalid input for ID. Please enter a valid integer.\n");
        // Clear input buffer
        while (getchar() != '\n') {
            printf("ID: ");
        }
    }
    
    // Name input
    printf("Name: ");
    // Clear input buffer
    while (getchar() != '\n');
    fgets(employees->name, sizeof(employees->name), stdin);
    employees->name[strcspn(employees->name, "\n")] = 0;

    // sales input
    printf("Enter sales for each day of the week: \n");
    for (int i = 0; i < DAYS_IN_A_WEEK; i++) {
        printf("Day %d: ", i + 1);
        while (scanf("%f", &employees->sales[i]) != 1) {
            printf("Error: Invalid input for sales amount. Please enter a valid number.\n");
            // Clear input buffer
            while (getchar() != '\n');
            printf("Day %d: ", i + 1);
        }
    }
}

float calculateTotalSales(struct Employee *employees) {//find sales for each employee
    float totalSales = 0;
    for (int i = 0; i < DAYS_IN_A_WEEK; i++) {
        totalSales += employees->sales[i];
    }
    employees->totalSales = totalSales;
    return totalSales;
}

float calculateOverallTotalSales(struct Employee *employees, int numEmployees) {//find grand total sale of ALL employee
    float overallTotalSales = 0;
    for (int i = 0; i < numEmployees; i++) {
        overallTotalSales += employees[i].totalSales;
    }
    return overallTotalSales;
}

struct Employee* findEmployeeWithHighestSales(struct Employee *employees) {//find top sale employee
    struct Employee *topSaleEmployee = &employees[0];
    for (int i = 1; i < DAYS_IN_A_WEEK; i++) {
        if (employees[i].totalSales > topSaleEmployee->totalSales) {
            topSaleEmployee = &employees[i];
        }
    }
    return topSaleEmployee;
}

int main() {

    int numEmployees;
    printf("Enter the number of employees: ");
    scanf("%d", &numEmployees);

    // //Requirement 1: malloc function is used to allocate memory for an array of Employee structures
    // //we find the total size needed by the formula: number of employee multiply with the size of the Employee structure
    // //and the result is return back the the pointer *employees
    struct Employee *employees = (struct Employee *)malloc(numEmployees * sizeof(struct Employee));

    //Requirement 2: Properly handles scenarios where memory allocation fails due to insufficient memory
    if (employees == NULL) {
        printf("Error: Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < numEmployees; i++) {
        printf("\nEmployee %d\n", i + 1);
        inputSales(&employees[i]);
    }

    // total sales for each employee
    for (int i = 0; i < numEmployees; i++) {
        float total = calculateTotalSales(&employees[i]);
        printf("\nTotal Sales for Employee %d (%s): RM%.2f", i + 1, employees[i].name, total);
    }
    // overall total sales
    float overallTotalSales = calculateOverallTotalSales(employees, numEmployees);
    printf("\n\nOverall Total Sales for the Week: RM%.2f\n", overallTotalSales);

    // top sale employee
    struct Employee *topSaleEmployee = findEmployeeWithHighestSales(employees);
    printf("\nEmployee with the Highest Sales:\n");
    printf("ID: %d\n", topSaleEmployee->id);
    printf("Name: %s\n", topSaleEmployee->name);
    printf("Total Sales: RM%.2f\n", topSaleEmployee->totalSales);

    // free memory
    free(employees);

    printf("\n\nThank you for using our Sales Tracking System!\n");
    return 0;
}

