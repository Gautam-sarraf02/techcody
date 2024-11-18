#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int number, guess;
      srand(time(0));
   number = rand() % 100 + 1;
   
    // Random number between 1 and 100
    printf("Guess the number (between 1 and 100):\n");
    // Loop until the user guesses the correct number
    while (1) {
        printf("Enter your guess: ");
        scanf("%d", &guess);

        if (guess > number) {
            printf("Too high!\n");
        } else if (guess < number) {
            printf("Too low!\n");
        } else {
            printf("\nCongratulations! You guessed the correct number: %d\n", number);
            break;
        }
    }
    return 0;
}