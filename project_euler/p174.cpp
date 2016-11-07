/*
	
	Project Euler 
	Problem #174

	Dylan Bowers

	https://projecteuler.net/problem=174
	
*/

#include <iostream>
#include <time.h>
#include <stdio.h>
#define MAX_T (1000000)
#define N (10)

using namespace std;

int* p174a() {
	int* L_arr = new int[MAX_T];
	for(int i = 0; i < MAX_T; i++) {
		L_arr[i] = 0;
	}

	int max_w = MAX_T / 4 + 1;
	for(int w = 3; w < max_w; w++) {
		int sum = 0;
		for(int i = w; i > 2; i-=2) {
			sum += 4 * i - 4;
			if(sum > MAX_T) { break; }
			L_arr[sum]++;
		}
	}

	int* N_arr = new int[N+1];
	for(int i = 0; i < N + 1; i++) {
		N_arr[i] = 0;
	}

	for(int i = 0; i < MAX_T; i++) {
		if(L_arr[i] <= N) {
			N_arr[L_arr[i]]++;
		}
	}

	return N_arr;
}

int p174() {
	int* a = p174a();
	int sum = 0;
	for(int i = 1; i < N + 1; i++) {
		sum += a[i];
	}
	return sum;
}

int main() {
	clock_t s, e;
	s = clock();
	int r = p174();
	e = clock();
	printf("Result: %d\n", r);
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}
