/*
	
	Project Euler 
	Problem #2

	Dylan Bowers

	Elapsed Run-time: 0.000000s
	Result: 4613732
	
*/
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <time.h>

using namespace std;

#define Phi ((sqrt(5) + 1) / 2)
#define phi (1/Phi)
#define LIMIT 4000000

int f(int n) { return ( pow(Phi, n) - pow((-phi), n) ) / sqrt(5); }

int p2() {
	int fn = 0;
	int sum = 2; // There was an issue with f(3), so we hardwire it to have f(3) already

	/* Even fibonacci numbers will only occur every 3 numbers. This is because the
	   pattern will go even odd odd even odd odd even ... and so onv due to the 
	   nature of the generation of fibonacci number being the two number prior
	   and odd+even=odd and only when odd+odd occurs will we see an even (since
	   there are never two evens in a row) */
	for(int i = 6; fn < LIMIT; i += 3) {
		sum += fn;
		fn = f(i);
	}
	return sum;
}

int main() {
	clock_t s, e;
	s = clock();
	int r = p2();
	e = clock();
	printf("Result: %d\n", r);
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}
