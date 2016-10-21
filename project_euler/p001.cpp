/*

	Project Euler 
	Problem #1

	Dylan Bowers
	Elapsed Run-time: 0.000000s
	Result: 233168
	
*/

#include <stdio.h>
#include <iostream>
#include <time.h>

using namespace std;

int p1() {
	int sum = 0;
	for(int i = 0; i < 1000; i++) { if(i%5==0 || i%3==0) { sum += i; } }
	return sum;
}

int main() {
	clock_t s, e;
	s = clock();
	int r = p1();
	e = clock();
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
	printf("Result: %d", r);
}
	
