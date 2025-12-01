<?php
$lines = file('1.txt', FILE_IGNORE_NEW_LINES);
$dial = 50;
$sum = 0;
$sum2 = 0;

foreach ($lines as $line) {
    if ($line == "") {
        continue;
    }
    $ch = $line[0];
    $a = array_values(array_slice(str_split($line), 1));
    $s = intval(implode('', $a));

    $dial_before = $dial;

    if ($ch == "L") {
        for ($i = 1; $i <= $s; $i++) {
            $dial -= 1;
            if ($dial == -1) {
                $dial = 99;
            }
            if ($dial == 0) {
                $sum2 += 1;
            }
        }
    }

    if ($ch == "R") {
        for ($i = 1; $i <= $s; $i++) {
            $dial += 1;
            if ($dial == 100) {
                $dial = 0;
            }
            if ($dial == 0) {
                $sum2 += 1;
            }
        }
    }

    if ($dial == 0) {
        $sum += 1;
    }

}

echo "Part 1: " . $sum . "\n";
echo "Part 2: " . $sum2 . "\n";