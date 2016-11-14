/*

	Project Euler 
	Problem #6

	Dylan Bowers
	Elapsed Run-time: 0.000000s
	Result: -25164150 (though answer is positive ver)

	https://projecteuler.net/problem=6
	Approach: (shouldn't really need an explanation)
	Runtime: O(n)
	
*/

#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;

#define LIMIT (100)

int p006() {
	int sq_nums = 0;
	int sq_sums = 0;

	for(int i = 1; i <= LIMIT; i++) {
		sq_nums += pow(i, 2);
		sq_sums += i;
	}

	sq_sums *= sq_sums;

	return sq_nums - sq_sums;
}

int main() {
	clock_t s, e;
	s = clock();
	int r = p006();
	e = clock();
	printf("Result: %d\n", r);
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}