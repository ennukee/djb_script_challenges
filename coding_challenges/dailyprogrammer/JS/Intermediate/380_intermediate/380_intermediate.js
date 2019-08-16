/*
    /r/DailyProgrammer 
       Medium #380
        @ennukee
    
    Runtime:
        Basic tests   6ms
        Bonus #1:    10ms
        Bonus #2:    NOT_DONE (Reason: Didn't feel like much of a coding challenge)
        Total:       16ms
    
    For the sake of accurate benchmarking, no data is cached
      between bonuses or test cases.
*/

const { performance } = require('perf_hooks');
const { read_bonus } = require('../../dp_util'); 

// Setting up dictionary with given data
const morseVals = '.- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..'.split(' ');
const morseDict = [...'abcdefghijklmnopqrstuvwxyz'].reduce((a, c, i) => Object.assign(a, {[c]: morseVals[i]}), {});
const alphaDict = Object.keys(morseDict).reduce((acc,c,i) => Object.assign(acc, {[morseDict[c]]: c}), {});

// Actual smorse function logic
const smorse = (val) => [...val].map(i => morseDict[i]).join('');
const unsmorse = (smorse) => {
    let unsmorsed = '';
    let lastUnused = 0;

    let i = 4;
    while (i > 0) {
        const cStr = smorse.slice(lastUnused, i);
        // console.log('testing for', cStr);
        if (alphaDict[cStr]) {
            unsmorsed += alphaDict[cStr];
            lastUnused = i;
            i += 4;
        }
        i--;
        if (lastUnused == smorse.length) break;
    }
    return unsmorsed;
};

// Actions & benchmarking //
const actions = [
    basic_tests_func,
    bonus1
]
actions.forEach(func => {
    let timer = performance.now();
    func();
    timer = performance.now() - timer;
    console.log(`DONE -- ${func.name}: ${timer.toFixed(1)}ms\n`)
})
// ---------------------- //

function basic_tests_func() {
    const tests = [".--...-.-.-.....-.--........----.-.-..---.---.--.--.-.-....-..-...-.---..--.----..",
        ".----...---.-....--.-........-----....--.-..-.-..--.--...--..-.---.--..-.-...--..-",
        "..-...-..-....--.---.---.---..-..--....-.....-..-.--.-.-.--.-..--.--..--.----..-.."
    ]
    for (let test of tests) {
        unsmorsed = unsmorse(test);
        if (test == smorse(unsmorsed)) {
            console.log(unsmorsed);
        }
        else {
            console.log('Unsmorsing went wrong for word:', test);
        }
    }
}

function bonus1() {
    const bonus1_words = read_bonus('1', '.\\Intermediate\\380_intermediate\\').split('\n').map(i => i.trim('\r'));
    let bonus1_out = '';
    bonus1_words.forEach((v, i) => {
        bonus1_out += `${unsmorse(v)}\n`;
    });
    return bonus1_out;
}