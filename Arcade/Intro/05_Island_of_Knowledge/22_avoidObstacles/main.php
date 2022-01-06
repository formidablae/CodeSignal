<?php

function getDivisors($n)
{
    $res = [];
    $i = 1;
    for ($i = 1; $i <= sqrt($n); $i++) {
        if ($n % $i == 0) {
            array_push($res, $i);
        }

        if ($n / $i == $i) {
            $i--;
            break;
        }
    }

    for (; $i >= 1; $i--) {
        if ($n % $i == 0) {
            array_push($res, ($n / $i));
        }
    }

    return $res;
}

function solution($inputArray) {
    $factors = [1];
    foreach ($inputArray as $num) {
        $numFactors = getDivisors($num);
        foreach ($numFactors as $factor) {
            $flagNotPresent = true;
            for ($i = 0; $i < count($factors); $i++) {
                if ($factors[$i] === $factor) {
                    $flagNotPresent = false;
                    break;
                } else if ($factors[$i] < $factor) {
                    continue;
                } else {
                    break;
                }
            }
            if ($flagNotPresent) {
                array_splice($factors, $i, 0, $factor);
            }
        }
    }

    $i = 1;
    $sol = 0;
    for (; $i < $factors[count($factors) - 1]; $i++) {
        if ($factors[$i - 1] !== $i) {
            $sol = $i;
            break;
        }
    }
    return $sol !== 0 ? $sol : $i + 1;
}
