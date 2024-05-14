#include <stdio.h>

double add(double num1, double num2) {
    return num1 + num2;
}

double subtract(double num1, double num2) {
    return num1 - num2;
}

double multiply(double num1, double num2) {
    return num1 * num2;
}

double divide(double num1, double num2) {
    if(num2 != 0.0)
        return num1 / num2;
    else
        return 0.0;
}

int main() {
    char operator;
    double num1, num2, result;
    int keepRunning = 1;

    while(keepRunning) {
        printf("Enter an operator (+, -, *, /) or 'q' to quit: ");
        scanf(" %c", &operator);

        if(operator == 'q') {
            keepRunning = 0;
            continue;
        }

        printf("Enter two operands: ");
        scanf("%lf %lf", &num1, &num2);

        switch(operator) {
            case '+':
                result = add(num1, num2);
                break;
            case '-':
                result = subtract(num1, num2);
                break;
            case '*':
                result = multiply(num1, num2);
                break;
            case '/':
                result = divide(num1, num2);
                break;
            default:
                printf("Invalid operator!\n");
                continue;
        }

        printf("Result: %.2lf\n", result);
    }

    printf("Calculator terminated.\n");
    return 0;
}
