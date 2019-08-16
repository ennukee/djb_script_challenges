/**
 * Codeforces Challenge #908_C
 *    @ennukee
 * 
 * Time Elapsed: 2.45ms (test case)
 *
 * @param {int} n -- Number of puts
 * @param {int} r -- Radius of each put
 * @param {int[]} x -- X_i values of each put at y = 10000
 */


function CF_908_C(n, r, x) {
    /**
     * 
     * Tracker variable used to manage the known put locations
     *   (likely overengineer'd, but whatever it looks readable
     *   and nice)
     * 
     */
    const PutsTracker = {
        puts: [],
        addPut(x, y) {
            this.puts.push( [x, y] );
        },
    }

    /**
     * 
     * ! The main logic loop !
     * 
     * ? How it works ?
     *  1. Iterate over each xi value provided
     *  2. For each xi, filter for all known puts whose X coordinate would cause a 
     *       collision (if they are within 2r of the known puts' X coordinate)
     *  3. If there are no collisions, then simply place it at the very bottom (xi, r)
     *  4. Otherwise, go through all collisions and find the highest possible collision
     *  5. From there, we KNOW the distance between these points, as well as the x1, 
     *       y1, and x2 values. So, I perform the point-distance formula re-arranged
     *       to calculate for y2 given x1, x2, y1 and dist.
     *  6. Put this new location in the tracker
     *  7. Repeat for all xi provided
     * 
     */
    x.forEach(xi => {
        const collisions = PutsTracker.puts.filter(([pxi]) => {
            return xi >= pxi - 2 * r && xi <= pxi + 2 * r; 
        });
        if (collisions.length === 0) {
            PutsTracker.addPut(xi, r);
        } else {
            const highest_collision = collisions.reduce((a, c) => {
                return a[1] > c[1] ? a : c;
            });
            const [xc, yc] = highest_collision;
            const new_yi = Math.sqrt(16 - Math.pow(xi - xc, 2)) + yc;
            PutsTracker.addPut(xi, new_yi);
        }
    });
    return PutsTracker.puts.map(([x, y]) => y).join(' ');
}

const { performance } = require('perf_hooks');
let timer = performance.now();
console.log( CF_908_C(6, 2, [5, 5, 6, 8, 3, 12]) );
timer = performance.now() - timer;
console.log(`Time elapsed for test case: ${timer.toFixed(2)}ms`)