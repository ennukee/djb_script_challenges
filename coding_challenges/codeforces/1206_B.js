/**
 * Codeforces Challenge #1206B
 *    @ennukee
 * 
 * Time Elapsed: 9.56ms (test cases)
 *
 * @param {int[]} a -- values in sequence for product
 */


function CF_1206_B( {a} ) {
    /**
     * 
     * Logic of this function
     * 
     *  1. Iterate over each value in the sequence 
     *  2. If > 0, add coins necessary to reduce to 1
     *  3. If < 0, add coins necessary to reduce to -1 and add to negative counter
     *  4. If == 0, add to zero counter
     *  5. If negative counter is ODD (product == -1), either add 1 coin if a zero 
     *       exists, or add 2 coins to convert a negative to positive.
     *  6. Add coins equal to zero count to bring them all to 1.
     *  7. Return coins
     * 
     */
    let negCount = 0, 
        zeroCount = 0, 
        coins = 0;
    a.forEach(ai => {
        if (ai > 0) coins += ai - 1;
        else if (ai < 0) {
            coins += Math.abs(ai) - 1;
            negCount++;
        }
        else if (ai == 0) zeroCount++;
    });

    if (negCount % 2 === 1) {
        if (zeroCount > 0) {
            coins += 1;
            zeroCount--;
        } else {
            coins += 2;
        }
    }

    coins += zeroCount;

    console.log(coins);
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
    [2, [-1, 1]],
    [4, [0, 0, 0, 0]],
    [5, [-5, -3, 5, 3, 0]],
]
test_cases.forEach(([n, a]) => {
    CF_1206_B({a});
});

timer = performance.now() - timer;
console.log(`Time elapsed for test case: ${timer.toFixed(2)}ms`)