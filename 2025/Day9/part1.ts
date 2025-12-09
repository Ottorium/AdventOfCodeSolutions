import * as fs from 'node:fs';

let input = fs.readFileSync('../input.txt', 'utf8');
const lines = input.split(/\n/);

let coords = []
for (const line of lines) {
    const a = parseInt(line.split(',')[0]);
    const b = parseInt(line.split(',')[1]);
    coords.push([a, b]);
}


function getSize(a: number[], b: number[]) {
    return (Math.abs(a[0] - b[0]) + 1) * (Math.abs(a[1] - b[1]) + 1);
}

let i = 0
let maxE = []
let max = 0
for (const y of coords) {
    let j = 0
    for (const x of coords) {
        if (j >= i) continue;
        const size = getSize(x, y)
        if (size > max) {
            max = getSize(x, y)
            maxE = [x, y]
        }
        console.log(x, y)
        console.log(size)
        j++
    }
    i++
}
console.log(max)