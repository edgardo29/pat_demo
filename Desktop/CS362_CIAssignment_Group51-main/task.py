"""
Authors: Kevin Peterson, Edgardo Infante, Preston Petersen
Date: 5/21/22
File: task.py - contains 3 functions as per group assignment description
"""


# Logic and helpers for conv_num
def conv_num(num_str):
    valid_hex_digs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                      'A', 'B', 'C', 'D', 'E', 'F']
    valid_decimal_digs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # Return None if empty or only contains decimal
    if len(num_str) == 0 or len(num_str) == 1 and num_str[0] == '.':
        return None

    num_str = num_str.upper()

    # If 0x prefix, no '.' or non alpha chars other than ABCDEF
    if (len(num_str) > 2 and num_str[0:2].upper() == "0X") or \
            (len(num_str) > 3 and num_str[0:3].upper() == "-0X"):

        start_index = 2
        if num_str[0] == '-':
            start_index = 3

        # Hex number, no '.' or alpha chars other than ABCDEF
        for i in range(start_index, len(num_str)):
            if not num_str[i].upper() in valid_hex_digs:
                return None

        return conv_valid_string_from_hex(num_str)
    else:  # Non-hex number, no Alpha
        num_dec_points_found = 0
        shifted_arr = False
        found_num = False

        # Iterate through each char to validate
        for i in range(len(num_str)):
            if num_str[i] in valid_decimal_digs:
                found_num = True

            # On first iteration, check for special case (. or -)
            if i == 0:
                # if Decimal first, add leading 0 and set flag
                if num_str[i] == '.':
                    num_dec_points_found += 1
                    num_str = "0" + num_str
                    shifted_arr = True
                # If first digit is invalid, return None
                elif (num_str[i] != '-' and not
                num_str[i] in valid_decimal_digs):
                    return None
            else:
                # After first digit, check for regular numbers - skip if we
                # added a leading 0
                if (i == 1 and not shifted_arr) or i > 1:
                    # If decimal, ensure this is first otherwise return None
                    if num_str[i] == '.':
                        num_dec_points_found += 1
                        if num_dec_points_found > 1:
                            return None
                    elif not num_str[i] in valid_decimal_digs:
                        return None

                # if decimal found at end, add a trailing 0
                if i == len(num_str) - 1 and num_str[i] == '.':
                    num_str += "0"

        # If there were no valid numbers, return None
        if not found_num:
            return None

        return conv_valid_string_to_int_or_dec(num_str)


# Helper function for converting a string to hex once we've validated string
def conv_valid_string_from_hex(num_str):
    neg_value = 1
    if num_str[0] == '-':
        neg_value = -1
        num_str = num_str[1:len(num_str) + 1]

    hex_to_dec_conversion = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    split_num = num_str.split('0X')
    hex_value = split_num[1]

    final_value = 0
    exp = 0
    for i in range(len(hex_value) - 1, -1, -1):
        final_value += hex_to_dec_conversion[hex_value[i]] * (16 ** exp)
        exp += 1

    return final_value * neg_value


# Helper function for converting a string to int/dec once we've
# validated string
def conv_valid_string_to_int_or_dec(num_str):
    string_to_num = 0
    neg_value = 1
    if num_str[0] == '-':
        neg_value = -1
        num_str = num_str[1:len(num_str) + 1]

    split_num = num_str.split('.')
    int_value = split_num[0]
    dec_value = None
    if len(split_num) > 1:
        dec_value = split_num[1]

    for i in int_value:
        # Use ascii conversion to get actual number
        string_to_num = string_to_num * 10 + (ord(i) - 48)

    if dec_value is not None:
        final_dec = 0
        divisor = 1
        for i in dec_value:
            # Use ascii conversion to get actual value
            final_dec = final_dec * 10 + (ord(i) - 48)
            divisor *= 10

        final_dec /= divisor
        string_to_num += final_dec

    return string_to_num * neg_value


# function takes integer value, converts to date and returns as string
def my_datetime(num_sec):

    def checkLeapYear(year):

        # Returns True if the year is a leap year

        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    def daysInMonth(month, year):

        # Returns the number of days in a month

        if month == 2:
            if checkLeapYear(year):
                return 29
            else:
                return 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def convertSeconds(seconds):

        # Returns an int of the converted seconds to days

        return seconds // 86400

    number_of_days = convertSeconds(num_sec)  # convert seconds to days

    day = 1
    month = 1
    year = 1970

    while number_of_days > 0:  # while there are still days to convert
        number_of_days -= 1  # decrement the number of days
        day += 1  # increment the day
        if day > daysInMonth(month, year):  # if the day is greater than the days in the month
            day = 1  # reset the day to 1
            month += 1  # increment the month
        if month > 12:  # if the month is greater than 12
            month = 1  # reset the month to 1
            year += 1  # increment the year

    return f'{month:02d}-{day:02d}-{year:02d}'  # return the converted date


# Function that takes a number and endian type and returns
# a hexidecimal conversion.
def conv_endian(num, endian='big'):
    if endian != 'big' and endian != 'little':
        return None

    hex = ""
    negative = False
    if num < 0:
        negative = True

    num = abs(num)

    binary = conv_dec_to_bin(num)
    if len(binary) % 8 != 0:
        zeros = '0' * (8 - (len(binary) % 8))
        binary = zeros + binary
    for i in range(len(binary), 7, -8):
        dec_right = chunk_to_dec(binary[(i - 4):i])
        dec_left = chunk_to_dec(binary[(i - 8):(i - 4)])
        if endian == 'little':
            hex += dec_to_hex(dec_left)
            hex += dec_to_hex(dec_right)
            if i > 8:
                hex += ' '
        else:
            hex = dec_to_hex(dec_right) + hex
            hex = dec_to_hex(dec_left) + hex
            if i > 8:
                hex = ' ' + hex
    if negative:
        hex = '-' + hex
    return hex


# Helper function to convert a decimal number into binary
def conv_dec_to_bin(num):
    binary = ""
    if num == 0:
        binary = "0"
    while num >= 1:
        rem = num % 2
        num = int(num / 2)
        binary = str(rem) + binary
    return binary


# Takes a section of 4 binary digits and converts them to decimal
def chunk_to_dec(bin_str):
    idx = 3
    dec = 0
    for i in range(4):
        dec += int(bin_str[i]) * (2 ** idx)
        idx -= 1
    return dec


# Converts decimal number from chunk to hexidecimal character
def dec_to_hex(num):
    over_10 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    if num >= 10:
        return str(over_10[num])
    return str(num)
