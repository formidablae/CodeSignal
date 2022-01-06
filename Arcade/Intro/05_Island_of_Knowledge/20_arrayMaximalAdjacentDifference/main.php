<?php

function solution($inputArray) {
    $maxDiff = 0;
    for ($i = 0; $i < count($inputArray) - 1; $i++) {
        $diff = abs($inputArray[$i] - $inputArray[$i + 1]);
        if ($diff > $maxDiff) {
            $maxDiff = $diff;
        }
    }
    return $maxDiff;
}
