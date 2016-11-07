/*

	Project Euler 
	Problem #9

	Dylan Bowers

	https://projecteuler.net/problem=9
	
*/

#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
#define LIMIT (1000)

int p009() {
	for(int i = 1; i <= LIMIT; i++) {
		for(int q = 1; q <= LIMIT - (500 - i); q++) {
			int r = 1000 - (i + q);
			if(i * i + q * q == r * r) {
				return i * q * r;
			}
		}
	}
	return 0;
}

int main() {
	printf("%d\n", p009());
}