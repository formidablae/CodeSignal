<?php

function solution($inputString)
{
    $inputArray = explode(".", $inputString);
    if (count($inputArray) != 4) {
        return false;
    }

    $numMax = 255;
    $numMin = 0;
    foreach ($inputArray as $num) {
        if ($num === "" || !is_numeric($num) || (int) $num < $numMin || (int) $num > $numMax || (strlen($num) > 1 && $num[0] === "0")) {
            return false;
        }
    }
    return true;
}
