/*

	Project Euler 
	Problem #5

	Dylan Bowers
	Elapsed Run-time: 0.000000s
	Result: 232792560

	Goal: Find the smallest positive number that is evenly divisble by all numbers 1 to 20
	Approach: Make array [1, 2, ..., 20]. Iterate it, divide out divisible at index i from all 
	          numbers in front of it. Afterward, the answer is the multiplication of all numbers
	          You can see a better visual of this in the code itself.

	          This is to make sure we have the lowest numbers possible with no repeats.
	Runtime: O(n^2)
	
*/
#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;

#define MAX_DIVISOR (20)

int p005() {
	/* Answer holder */
	int answer = 1;

	/* Initialize the array from 1 to desired */
	int* divisors = new int[MAX_DIVISOR + 1];
	for(int i = 1; i <= MAX_DIVISOR; i++) { divisors[i] = i; }

	/* Divide over the array */
	/*
		How it should run for MAX_DIVISOR = 10
		[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		[1| 2, 3, 4, 5, 6, 7, 8, 9, 10]
		[1, 2| 3, 2, 5, 3, 7, 4, 9, 5]
		[1, 2, 3| 2, 5, 2, 7, 4, 3, 5]
		[1, 2, 3, 2| 5, 1, 7, 2, 3, 5]
		[1, 2, 3, 2, 5| 1, 7, 2, 3, 1]
		[1, 2, 3, 2, 5, 1| 7, 2, 3, 1]
		. . . (nothing else changes)
		[1, 2, 3, 2, 5, 3, 7, 2, 3, 1]
		=> 1 * 2 * 3 * 2 * 5 * 1 * 7 * 2 * 3 * 1 = 2520

	*/

	for(int i = 1; i < MAX_DIVISOR; i++) { 
		for(int q = i + 1; q <= MAX_DIVISOR; q++) {
			if(divisors[q] % divisors[i] == 0) { divisors[q] /= divisors[i]; }
		}
		answer *= divisors[i];
	}

	return answer;
}

int main() {
	clock_t s, e;
	s = clock();
	int r = p005();
	e = clock();
	printf("Result: %d\n", r);
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}