#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Function prototypes
void displayBoard(char board[3][3]);
void playerInput(char board[3][3], char player);
int checkGameStatus(char board[3][3]);
void resetBoard(char board[3][3]);

// Function to display the board
void displayBoard(char board[3][3]) {
    printf("\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) 
        {
            printf(" %c ", board[i][j]);
            if (j < 2) 
            printf("|");
        }
        if (i < 2) printf("\n---|---|---\n");
    }
    printf("\n");
}

// Function to handle player input
void playerInput(char board[3][3], char player) {
    int row, col;

    while (true) {
        printf("Enter row (1-3) and column (1-3): ");
        scanf("%d %d", &row, &col);

        if (row >= 1 && row <= 3 && col >= 1 && col <= 3 && board[row - 1][col - 1] == ' ') {
            board[row - 1][col - 1] = player;
            break;
        } else {
            printf("Invalid move! Try again.\n");
        }
    }
}

// Function to check the game status
int checkGameStatus(char board[3][3]) {
    // Check rows and columns
    for (int i = 0; i < 3; i++) {
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2] && board[i][0] != ' ') return 1;
        if (board[0][i] == board[1][i] && board[1][i] == board[2][i] && board[0][i] != ' ') return 1;
    }

    // Check diagonals
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2] && board[0][0] != ' ') return 1;
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0] && board[0][2] != ' ') return 1;

    // Check for draw
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') return 0; // Still moves left
        }
    }

    return 2; // Draw
}

// Function to reset the board
void resetBoard(char board[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

int main() {
    char board[3][3];
    char currentPlayer = 'X';
    int gameStatus = 0; // 0: ongoing, 1: win, 2: draw
    char choice;

    resetBoard(board);

    printf("Welcome to Tic-Tac-Toe!\n");

    while (true) {
        displayBoard(board);
        printf("Player %c's turn. Enter your move (row and column):\n", currentPlayer);

        playerInput(board, currentPlayer);

        gameStatus = checkGameStatus(board);
        if (gameStatus == 1) {
            displayBoard(board);
            printf("Player %c wins! 🎉\n", currentPlayer);
            break;
        } else if (gameStatus == 2) {
            displayBoard(board);
            printf("It's a draw! 🤝\n");
            break;
        }

        // Switch player
        currentPlayer = (currentPlayer == 'X') ? 'O' : 'X';
    }

    // Restart or quit option
    printf("Would you like to play again? (y/n): ");
    scanf(" %c", &choice);
    if (choice == 'y' || choice == 'Y') {
        resetBoard(board);
        main(); // Restart the game
    } else {
        printf("Thanks for playing! Goodbye!\n");
        exit(0);
    }

    return 0;
}
