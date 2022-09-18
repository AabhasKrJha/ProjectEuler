// c program for faster implementation using method 2

// Smallest multiple

// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include <stdio.h>
#include <stdbool.h>

int main(){

    int divisors[19] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
    int divident = 1;
    bool divisible;

    while (true){

        divisible = true;

        for (int index = 0; index < 19; index++){

            int divisior = divisors[index];
            if (divident % divisior != 0){
                divisible = false;
                break;
            }

        }

        if (divisible){
            printf("%d", divident);
            break;
        } else{
            divident++;
        }

    }

    return 0;
}
