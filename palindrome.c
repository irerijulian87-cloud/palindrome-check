#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {

    char word[100];
    int i, length;
    int isPalindrome;

    while (1) {

        // Ask the user to enter a word
        printf("Enter a word (or 'quit' to exit): ");
        if (scanf("%99s", word) != 1) {
            break;  // input ended (EOF)
        }

        // Exit condition
        if (strcmp(word, "quit") == 0) {
            break;
        }

        // Reset the flag for each new word
        isPalindrome = 1;

        length = strlen(word);

        for (i = 0; i < length / 2; i++) {
            if (tolower((unsigned char)word[i]) !=
                tolower((unsigned char)word[length - 1 - i])) {
                isPalindrome = 0;
                break;
            }
        }

        if (isPalindrome) {
            printf("%s is a palindrome.\n\n", word);
        } else {
            printf("%s is not a palindrome.\n\n", word);
        }
    }

    printf("Goodbye!\n");
    return 0;
}