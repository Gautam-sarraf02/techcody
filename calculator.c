#include <stdio.h>
#include <math.h>

// Function are:-
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
double power(double a, double b);
double square_root(double a);
double sine(double a);
double cosine(double a);
double tangent(double a);

int main() {
    int symbol;
    double num1, num2, result;

    while (1) {
        printf("\nScientific Calculator:\n");
        printf("1. Addition\n");
        printf("2. Subtraction\n");
        printf("3. Multiplication\n");
        printf("4. Division\n");
        printf("5. Power\n");
        printf("6. Square Root\n");
        printf("7. Sine\n");
        printf("8. Cosine\n");
        printf("9. Tangent\n");
        printf("0. Exit\n");
        printf("Enter your symbole: ");
        scanf("%d", &symbol);

        if (symbol== 0) {
            printf("Exiting...\n");
            break;
        }

        if (symbol>= 1 && symbol <= 5) {
            printf("Enter first number: ");
            scanf("%lf", &num1);
            printf("Enter second number\n.: ");
            scanf("%lf", &num2);
        } 
        else if (symbol == 6) {
            printf("Enter number: ");
            scanf("%lf", &num1);
        } 
        else if (symbol >= 7 && symbol <= 9) {
            printf("Enter angle in radians: ");
            scanf("%lf", &num1);
        }
        else {
            printf("Invalid choice!\n");
            continue;
        }

        switch (symbol) {
            case 1:
                result = add(num1, num2);
                printf("\nResult: %lf", result);
                break;
            case 2:
                result = subtract(num1, num2);
                printf("\n/Result: %lf", result);
                break;
            case 3:
                result = multiply(num1, num2);
                printf("Result: %lf\n", result);
                break;
            case 4:
                result = divide(num1, num2);
                if (num2 != 0)
                    printf("Result: %lf\n", result);
                break;
            case 5:
                result = power(num1, num2);
                printf("Result: %lf\n", result);
                break;
            case 6:
                result = square_root(num1);
                if (num1 >= 0)
                    printf("Result: %lf\n", result);
                break;
            case 7:
                result = sine(num1);
                printf("Result: %lf\n", result);
                break;
            case 8:
                result = cosine(num1);
                printf("Result: %lf\n", result);
                break;
            case 9:
                result = tangent(num1);
                printf("Result: %lf\n", result);
                break;
            default:
                printf("Invalid choice!\n");
        }
    }
    return 0;
}

// Function are:- 
double add(double a, double b) 
{
    return a + b;
}

double subtract(double a, double b) 
{
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) 
{
    if (b != 0)
        return a / b;
    else {
        printf("math Error !\nbetter luck next time ");
        return 0;
    }
}

double power(double a, double b)
 {
    return pow(a, b);
}

double square_root(double a)
 {
    if (a >= 0)
        return sqrt(a);
    else {
        printf("Error: Negative number!\n");
        return 0;
    }
}

double sine(double a) 
{
    return sin(a);
}

double cosine(double a) 
{
    return cos(a);
}

double tangent(double a) 
{
    return tan(a);
}
