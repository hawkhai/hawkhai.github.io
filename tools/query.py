#!/usr/bin/env python3

import hashlib
import json
import os
import re
import sys
from urllib.parse import parse_qs


def add_one_to_integer_string(value):
    sign = ''
    if value and value[0] in ('+', '-'):
        sign = value[0]
        value = value[1:]

    value = value.lstrip('0')
    if value == '':
        value = '0'

    if sign == '-':
        if value == '0' or value == '1':
            return '0'

        digits = list(value)
        borrow = 1
        for i in range(len(digits) - 1, -1, -1):
            if borrow <= 0:
                break

            digit = ord(digits[i]) - 48 - borrow
            if digit < 0:
                digit += 10
                borrow = 1
            else:
                borrow = 0
            digits[i] = chr(digit + 48)

        value = ''.join(digits).lstrip('0')
        return '0' if value == '' else '-' + value

    digits = list(value)
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        if carry <= 0:
            break

        digit = ord(digits[i]) - 48 + carry
        if digit >= 10:
            digit -= 10
            carry = 1
        else:
            carry = 0
        digits[i] = chr(digit + 48)

    value = ''.join(digits)
    if carry > 0:
        value = '1' + value

    return value


def get_params():
    if 'QUERY_STRING' in os.environ:
        return parse_qs(os.environ.get('QUERY_STRING', ''), keep_blank_values=True)

    if len(sys.argv) > 1:
        return parse_qs(sys.argv[1], keep_blank_values=True)

    return {}


def get_input_value(params):
    for key in ('s', 'str', 'input', 'value'):
        if key in params:
            return params[key][0]
    return None


def embed_id_in_md5(md5_value, input_value):
    # Keep the final two hash characters. The ID ends at the third position
    # from the end, making the complete ID visible without changing length.
    return md5_value[:30 - len(input_value)] + input_value + md5_value[-2:]


def respond(body, status=None, content_type='text/plain; charset=utf-8'):
    if status is not None:
        print('Status: {}'.format(status))
    print('Content-Type: {}'.format(content_type))
    print()
    print(body)


def main():
    params = get_params()
    input_value = get_input_value(params)

    if input_value is None:
        respond('Missing input. Use URL: query.py?s=123', '400 Bad Request')
        return 1

    if re.fullmatch(r'\d{1,30}', input_value) is None:
        respond('ID must contain 1 to 30 decimal digits.', '400 Bad Request')
        return 1

    plus_one = add_one_to_integer_string(input_value)
    md5_value = embed_id_in_md5(
        hashlib.md5(plus_one.encode('utf-8')).hexdigest(),
        input_value,
    )

    if 'json' in params:
        respond(
            json.dumps({
                'input': input_value,
                'plus_one': plus_one,
                'embedded_id': input_value,
                'md5': md5_value,
            }, separators=(',', ':')),
            content_type='application/json; charset=utf-8',
        )
        return 0

    respond(md5_value)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
