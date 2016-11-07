/*

	Project Euler 
	Problem #214

	Dylan Bowers
	
	https://projecteuler.net/problem=214
	
*/

#include <stdio.h>
#include <iostream>
#include <math.h>
#include <time.h>
#define LIMIT 40000000

using namespace std;

void p214() {
	long long unsigned int answer = 0;
	int* all_totients = new int[LIMIT + 1];
	for(int i = 0; i <= LIMIT; i++) { all_totients[i] = i; }
	for(int n = 2; n <= LIMIT; n++) {
		if(n == all_totients[n]) {
			for(int m = n; m <= LIMIT; m += n) {
				all_totients[m] /= n;
				all_totients[m] *= n - 1;
			}
		}
	}

	cout << "-> All totients calculated" << endl;

	int* tot_chain_lengths = new int[LIMIT + 1];
	tot_chain_lengths[0] = 0;
	tot_chain_lengths[1] = 1;

	for(int n = 2; n < LIMIT; n++) {
		tot_chain_lengths[n] = tot_chain_lengths[all_totients[n]] + 1;

		if(tot_chain_lengths[n] == 25 && all_totients[n] == n-1) {
			answer += n;
		}
	}
	cout << "-> All TCLs calculated" << endl;

	cout << answer << endl;
}

int main() {
	clock_t s, e;
	s = clock();
	p214();
	e = clock();
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}