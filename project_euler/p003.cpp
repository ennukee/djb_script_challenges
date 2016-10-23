/*
	
	Project Euler 
	Problem #3

	Dylan Bowers

	Elapsed Run-time: 0.018000s
	Result: 6857
	
*/
#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;

#define LIMIT (600851475143)

uint64_t p003(uint64_t l) {
	uint64_t max = 1;
	uint64_t cur = l;
	for(uint64_t i = 2; i < sqrt(l);) {
		if(cur % i == 0) {
			cur /= i;
			if(i > max) { max = i; }
		} else {
			if(i == 2) { i++; }
			else { i+=2; }
		}
	}
	return max;

}

int main() {
	clock_t s, e;
	s = clock();
	uint64_t r = p003(LIMIT);
	e = clock();
	printf("Result: %d\n", r);
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}