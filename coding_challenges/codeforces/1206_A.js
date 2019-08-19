/**
 * Codeforces Challenge #1206_A
 *    @ennukee
 * 
 * Time Elapsed: 9.05ms (test cases)
 *
 * @param {int[]} a -- values in array A
 * @param {int[]} b -- values in array B
 * @param {function} tcb -- A test callback function that confirms the validity of the output
 */


function CF_1206_A( {a, b}, tcb ) {
    /**
     * Given the assumption that A and B are arrays full of positive integers (>0),
     *   we can always get a unique combination by combining the highest values
     *   of each given array
     */

    const aMax = Math.max(...a);
    const bMax = Math.max(...b);
    if (tcb(a, b, aMax, bMax)) {
        console.log(aMax, bMax);
    }
    else {
        console.log('FAILED_TEST');
    }
}

/**
 * 
 * Test cases and benchmarking code below this point
 * 
 * Unrelated to the solution code
 * 
 */

const { performance } = require('perf_hooks');
let timer = performance.now();

const test_cases = [
    [1, [20], 2, [10, 20]],
    [3, [5, 2, 2], 5, [1, 5, 7, 7, 9]],
    [4, [1, 3, 5, 7], 4, [7, 5, 3, 1]],
]
const callback = (a, b, ai, bi) => a.includes(ai) && b.includes(bi) && !a.includes(ai+bi) && !b.includes(ai+bi);
test_cases.forEach(([a_len, a, b_len, b]) => {
    CF_1206_A({a, b}, callback);
});

timer = performance.now() - timer;
console.log(`Time elapsed for test case: ${timer.toFixed(2)}ms`)