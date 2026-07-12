<?php

function addOneToIntegerString($value) {
    $sign = '';
    if ($value !== '' && ($value[0] === '+' || $value[0] === '-')) {
        $sign = $value[0];
        $value = substr($value, 1);
    }

    $value = ltrim($value, '0');
    if ($value === '') {
        $value = '0';
    }

    if ($sign === '-') {
        if ($value === '0' || $value === '1') {
            return '0';
        }

        $borrow = 1;
        for ($i = strlen($value) - 1; $i >= 0 && $borrow > 0; $i--) {
            $digit = ord($value[$i]) - 48 - $borrow;
            if ($digit < 0) {
                $digit += 10;
                $borrow = 1;
            } else {
                $borrow = 0;
            }
            $value[$i] = chr($digit + 48);
        }

        $value = ltrim($value, '0');
        return $value === '' ? '0' : '-' . $value;
    }

    $carry = 1;
    for ($i = strlen($value) - 1; $i >= 0 && $carry > 0; $i--) {
        $digit = ord($value[$i]) - 48 + $carry;
        if ($digit >= 10) {
            $digit -= 10;
            $carry = 1;
        } else {
            $carry = 0;
        }
        $value[$i] = chr($digit + 48);
    }

    if ($carry > 0) {
        $value = '1' . $value;
    }

    return $value;
}

function getInputValue() {
    foreach (array('s', 'str', 'input', 'value') as $key) {
        if (isset($_GET[$key])) {
            return (string)$_GET[$key];
        }
    }

    return null;
}

function embedIdInMd5($hash, $id) {
    // Keep the final two hash characters. The ID ends at the third position
    // from the end, making the complete ID visible without changing length.
    return substr($hash, 0, 30 - strlen($id)) . $id . substr($hash, -2);
}

$input = getInputValue();

if ($input === null) {
    $message = 'Missing input. Use URL: query.php?s=123';
    http_response_code(400);
    header('Content-Type: text/plain; charset=utf-8');
    echo $message;
    exit;
}

if (!preg_match('/^\d{1,30}$/', $input)) {
    $message = 'ID must contain 1 to 30 decimal digits.';
    http_response_code(400);
    header('Content-Type: text/plain; charset=utf-8');
    echo $message;
    exit;
}

$plusOne = addOneToIntegerString($input);
$hash = embedIdInMd5(md5($plusOne), $input);

if (isset($_GET['json'])) {
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(array(
        'input' => $input,
        'plus_one' => $plusOne,
        'embedded_id' => $input,
        'md5' => $hash,
    ), JSON_UNESCAPED_SLASHES);
    exit;
}

header('Content-Type: text/plain; charset=utf-8');
echo $hash . PHP_EOL;
