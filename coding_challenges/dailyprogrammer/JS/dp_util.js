/*
    /r/DailyProgrammer 
        @ennukee
    
    Utility Files
*/

const fs = require('fs');
const path = require('path');

const enable1 = fs.readFileSync(path.resolve(__dirname, 'enable1.txt'), 'utf8');
const read_bonus = (param, p) => fs.readFileSync(path.resolve(__dirname, `${p}bonus${param}.txt`), 'utf8');

module.exports = {
    enable1,
    read_bonus,
}
