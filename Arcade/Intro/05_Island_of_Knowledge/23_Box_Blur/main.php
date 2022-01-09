<?php

function calcAvg($square) {
    $res = 0;
    $length = count($square);
    $width = count($square[0]);
    for ($i = 0; $i < $length; $i++) {
        $res += array_sum($square[$i]);
    }
    return floor($res / ($length * $width));
}

function solution($image) {
    $result = [];
    $length = count($image);
    $width = count($image[0]);
    for ($i = 1; $i < $length - 1; $i++) {
        $result[$i - 1] = [];
        $internalsquare = [];
        for ($j = 1; $j < $width - 1; $j++) {
            $result[$i - 1][$j - 1] = [];
            $internalsquare[0] = [
                $image[$i - 1][$j - 1],
                $image[$i - 1][$j],
                $image[$i - 1][$j + 1],
            ];
            $internalsquare[1] = [
                $image[$i][$j - 1],
                $image[$i][$j],
                $image[$i][$j + 1],
            ];
            $internalsquare[2] = [
                $image[$i + 1][$j - 1],
                $image[$i + 1][$j],
                $image[$i + 1][$j + 1],
            ];
            $result[$i - 1][$j - 1] = calcAvg($internalsquare);
        }
    }
    return $result;
}

// $image1 = [
//     [1, 1, 1],
//     [1, 7, 1],
//     [1, 1, 1]
// ];

// $image2 = [
//     [7, 4, 0, 1],
//     [5, 6, 2, 2],
//     [6, 10, 7, 8],
//     [1, 4, 2, 0]
// ];

// print_r(solution($image1));
// print_r(solution($image2));
