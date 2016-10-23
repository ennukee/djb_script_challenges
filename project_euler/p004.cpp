/*

	Project Euler 
	Problem #4

	Dylan Bowers
	Elapsed Run-time: 0.162000s
	Result: 906609

	Goal: Find the largest palindrome made from a multiple of two three-digit numbers
	Approach: Iterate twice on 100 to 999, check if first loop * second loop is a palindrome
	          and if it is, if it's bigger than the largest known. Save if it is, return max 
	          at end.
	Runtime: approx O(n^3)
	
*/
#include <iostream>
#include <stdio.h>
#include <time.h>
#include <math.h>

using namespace std;

bool is_palindrome(int i) {
	string c_a = to_string(i);
	int a_l = c_a.size();
	for(int i = 0; i < a_l / 2 + 1; i++) {
		if(c_a[i] != c_a[a_l - (i + 1)]) { return false; }
	}
	return true;
}

int p004() {
	int max_palindrome = 0;
	for(int i = 100; i <= 999; i++) {
		for(int q = 100; q <= 999; q++) {
			int product = i * q;
			if(is_palindrome(product) && product > max_palindrome) { max_palindrome = product; }
		}
	}
	return max_palindrome;
}

int main() {
	clock_t s, e;
	s = clock();
	uint64_t r = p004();
	e = clock();
	printf("Result: %d\n", r);
	printf("Code executed in %fs\n", ((float)e - (float)s)/CLOCKS_PER_SEC);
}