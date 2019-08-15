/*
    /r/DailyProgrammer 
        Easy #380
        @ennukee
    
    Runtime:
        Basic tests   8ms
        Bonus #1:   245ms
        Bonus #2:    34ms
        Bonus #3:    15ms
        Bonus #4:    41ms (slow version 59ms) 
        Bonus #5:   433ms
        Total:      781ms
    
    For the sake of accurate benchmarking, no data is cached
      between bonuses or test cases.
*/

const { performance } = require('perf_hooks');
const { enable1 } = require('../../dp_util'); 
let en1 = enable1(require('path'));

// Setting up dictionary with given data
const morse_vals = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' ');
const morse_dict = [...'abcdefghijklmnopqrstuvwxyz'].reduce((a, c, i) => Object.assign(a, {[c]: morse_vals[i]}), {});

// Actual smorse function logic
const smorse = (val) => [...val].map(i => morse_dict[i]).join('');

// Actions & benchmarking //
const actions = [
    basic_tests_func,
    bonus1,
    bonus2,
    bonus3,
    bonus4,
    bonus4_manual,
    bonus5
]
actions.forEach(func => {
    let timer = performance.now();
    func();
    timer = performance.now() - timer;
    console.log(`DONE -- ${func.name}: ${timer.toFixed(1)}ms\n`)
})
// ---------------------- //

// Test cases
function basic_tests_func() {
    const test_cases = ['sos', 'daily', 'programmer', 'bits', 'three'];
    test_cases.forEach(i => {
        console.log(i, '=>', smorse(i));
    });
}

// Bonus #1
function bonus1() {
    const tracker = {}
    for (let word of en1.split('\n')) {
        const smorsed = smorse(word);
        tracker[smorsed] |= 0;
        tracker[smorsed] += 1;
        if (tracker[smorsed] == 13) {
            console.log(`Found: ${word} (${smorsed})`)
            return;
        }
    }
}

// Bonus 2
function bonus2() {
    // Brute-force version
    for (let word of en1.split('\n')) {
        const smorsed = smorse(word);
        if (/---------------/g.exec(smorsed)) {
            console.log(`Found: ${word} (${smorsed})`)
            return;
        }
    }
}

// Bonus 3
function bonus3() {
    for (let word of en1.split('\n').filter(w => w.length === 21)) {
        const smorsed = smorse(word);
        if (smorsed.replace(/[^\-]/g, "").length === smorsed.replace(/[^\.]/g, "").length && word !== 'counterdemonstrations') {
            console.log(`Found: ${word} (${smorsed})`);
            return;
        }
    }
}

// Bonus 4
function bonus4() {
    const isPalindrome = (val) => val.slice(Math.ceil(val / 2)) === [...val.slice(Math.ceil(val / 2))].reverse().join('');
    for (let word of en1.split('\n').filter(w => w.length === 13)) {
        const smorsed = smorse(word);
        if (isPalindrome(smorsed)) {
            console.log(`Found: ${word} (${smorsed})`);
        }
    }
}

// Also bonus 4 -- but with a more direct iterative check to reduce time consumption
function bonus4_manual() {
    const isPalindrome = function(val) {
        let valid = true;
        [...Array(Math.ceil(val.length/2)).keys()].forEach(v => {
            if (val[v] !== val[val.length - v - 1]) valid = false;
        })
        return valid;
    }
    for (let word of en1.split('\n').filter(w => w.length === 13)) {
        const smorsed = smorse(word);
        if (isPalindrome(smorsed)) {
            console.log(`Found: ${word} (${smorsed})`);
        }
    }
}

// Bonus 5
function bonus5() {
    function getAllCombos(n, c = '') {
        if (n == 0) return [c];
        else {
            return [ ...getAllCombos(n - 1, c + '.'), ...getAllCombos(n - 1, c + '-') ];
        }
    }
    let combos = getAllCombos(13);
    let seen = new Set([]);
    for (let word of en1.split('\n')) {
        const smorsed = smorse(word);
        if (smorsed.length >= 13) {
            for(let i = 0; i <= smorsed.length - 13; i++) {
                const slce = smorsed.slice(i, i + 13);
                seen.add(slce);
            }
        }
    }

    const survivors = combos.filter(key => !seen.has(key));
    for (let seq of survivors) {
        console.log(`Found: ${seq}`);
    }
}
