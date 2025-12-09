import * as fs from 'node:fs';

let input = fs.readFileSync('../input.txt', 'utf8');
const lines = input.split(/\n/);
let coords = []
let maxX = 0
let maxY = 0
for (const line of lines) {
    const a = parseInt(line.split(',')[0]);
    const b = parseInt(line.split(',')[1]);
    coords.push([a, b]);
    if (a > maxX) {
        maxX = a
    }
    if (b > maxY) {
        maxY = b
    }
}

maxX += 2
maxY += 2

function getGrid(grid: Uint8Array, r: number, c: number, maxX: number): number {
    const position = r * maxX + c
    const gridPos = Math.floor(position / 4)
    const bitPos = (position % 4) * 2
    const byte = grid[gridPos]
    return (byte & (0b11 << bitPos)) >> bitPos
}

function setGrid(grid: Uint8Array, r: number, c: number, value: number, maxX: number) {
    const position = r * maxX + c
    const gridPos = Math.floor(position / 4)
    const bitPos = (position % 4) * 2
    let byte = grid[gridPos]
    byte = byte & ~(0b11 << bitPos)
    byte = byte | ((value & 0b11) << bitPos)
    grid[gridPos] = byte
}

const grid = new Uint8Array(Math.ceil((maxX * maxY) / 4));

function makeLineInGrid(grid: Uint8Array, x: number[], y: number[], maxX: number) {
    let a = x[0]
    let b = x[1]
    let c = y[0]
    let d = y[1]
    if (a == c) {
        if (b < d) {
            for (let m = b; m <= d; m++) {
                setGrid(grid, m, a, 1, maxX)
            }
        } else {
            for (let m = d; m <= b; m++) {
                setGrid(grid, m, a, 1, maxX)
            }
        }

    } else if (b == d) {
        if (a < c) {
            for (let m = a; m <= c; m++) {
                setGrid(grid, b, m, 1, maxX)
            }
        } else {
            for (let m = c; m <= a; m++) {
                setGrid(grid, b, m, 1, maxX)
            }
        }
    } else {
        throw Error("Can't fill grid, no two dimensions are the same");
    }
}

let prev = coords[0]
for (const y of coords) {
    makeLineInGrid(grid, prev, y, maxX)
    prev = y
}
makeLineInGrid(grid, prev, coords[0], maxX)
console.log("boundaries marked")

function fillOuterBounds(grid: Uint8Array, startX: number, startY: number, maxX: number, maxY: number) {
    const startColor = 0;
    const boundaryColor = 1
    const setColor = 2
    const queue = [[startX, startY]];
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    const directionsWithDiagonal = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
    let i = 0;

    while (queue.length > 0) {
        i++
        // @ts-ignore
        const [x, y] = queue.shift();

        let boundIsNeighbour = false;
        for (const [dx, dy] of directionsWithDiagonal) {
            if (getGrid(grid, y + dy, x + dx, maxX) == boundaryColor) {
                boundIsNeighbour = true;
                break;
            }
        }

        if (!boundIsNeighbour) continue

        setGrid(grid, y, x, setColor, maxX)

        for (const [dx, dy] of directions) {
            const newX = x + dx;
            const newY = y + dy;
            if (!(newX >= 0 && newX < maxX && newY >= 0 && newY < maxY)) continue;
            if (getGrid(grid, newY, newX, maxX) !== startColor) continue;

            queue.push([newX, newY]);
        }
    }
}

function printGrid(grid: Uint8Array, maxX: number) {
    for (let r = 0; r < maxY; r++) {
        let s = ""
        for (let c = 0; c < maxX; c++) {
            s += getGrid(grid, r, c, maxX)
        }
        console.log(s);
    }
}

let startY = 0
let startX: number = 0
outer: for (let r = 0; r < maxY; r++) {
    for (let c = 0; c < maxX; c++) {
        if (getGrid(grid, r, c, maxX) != 0) {
            startY = r - 1
            startX = c
            break outer
        }
    }
}

if (startX == 0 && startY == 0) throw "Can't fill grid, cant find start position"

console.log(`startX = ${startX}, startY = ${startY}`)
fillOuterBounds(grid, startX, startY, maxX, maxY);
console.log("fillOuterBounds finished")

//printGrid(grid, maxX)


function getSize(grid: Uint8Array, a: number[], b: number[], maxX: number) {
    const left = Math.min(a[0], b[0])
    const top = Math.min(a[1], b[1])
    const right = Math.max(a[0], b[0])
    const bottom = Math.max(a[1], b[1])
    for (let i = left + 1; i <= right - 1; i++) {
        let j = top
        if (getGrid(grid, j, i, maxX) == 2) {
            return 0
        }
        j = bottom
        if (getGrid(grid, j, i, maxX) == 2) {
            return 0
        }
    }

    let i = left
    for (let j = top; j <= bottom; j++) {
        if (getGrid(grid, j, i, maxX) == 2) {
            return 0
        }
    }
    i = right
    for (let j = top; j <= bottom; j++) {
        if (getGrid(grid, j, i, maxX) == 2) {
            return 0
        }
    }

    return (Math.abs(a[0] - b[0]) + 1) * (Math.abs(a[1] - b[1]) + 1);
}

function simpleSize(a: number[], b: number[]) {
    return (Math.abs(a[0] - b[0]) + 1) * (Math.abs(a[1] - b[1]) + 1);
}

let i = 0
let maxE = []
let max = 0
for (const y of coords) {
    let j = 0
    for (const x of coords) {
        if (j >= i) continue;
        if (simpleSize(x, y) <= max) continue;
        const size = getSize(grid, x, y, maxX)
        if (size > max) {
            max = size
            maxE = [x, y]
        }
        j++
    }
    i++
}
console.log(max)