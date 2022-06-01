"""
Authors: Kevin Peterson, Edgardo Infante, Preston Petersen
Date: 5/21/22
File: tests.py - unit test file for group project
test comment
"""

import unittest
import task


class TestCase(unittest.TestCase):
    def test1_conv_num_ok(self):
        self.assertTrue(task.conv_num("0xffff") == 65535)

    def test1_b_conv_num_ok(self):
        self.assertTrue(task.conv_num("0Xffff") == 65535)

    def test2_conv_num_ok(self):
        self.assertTrue(task.conv_num("0x0") == 0)

    def test3_conv_num_ok(self):
        self.assertTrue(task.conv_num("0xAD4") == 2772)

    def test4_conv_num_ok(self):
        self.assertTrue(task.conv_num("-0xAD4") == -2772)

    def test5_conv_num_ok(self):
        self.assertTrue(task.conv_num("123") == 123)

    def test6_conv_num_ok(self):
        self.assertTrue(task.conv_num("123.27") == 123.27)

    def test7_conv_num_ok(self):
        self.assertTrue(task.conv_num(".27") == 0.27)

    def test8_conv_num_ok(self):
        self.assertTrue(task.conv_num("27.") == 27.0)

    def test9_conv_num_ok(self):
        self.assertTrue(task.conv_num("-27.") == -27.0)

    def test10_conv_num_ok(self):
        self.assertTrue(task.conv_num("-.3") == -0.3)

    def test11_conv_num_fail(self):
        self.assertTrue(task.conv_num("-.") is None)

    def test12_conv_num_fail(self):
        self.assertTrue(task.conv_num("1xffff") is None)

    def test13_conv_num_fail(self):
        self.assertTrue(task.conv_num("0xfkff") is None)

    def test14_conv_num_fail(self):
        self.assertTrue(task.conv_num("0x") is None)

    def test15_conv_num_fail(self):
        self.assertTrue(task.conv_num("-0x") is None)

    def test16_conv_num_fail(self):
        self.assertTrue(task.conv_num(".") is None)

    def test17_conv_num_fail(self):
        self.assertTrue(task.conv_num("123A") is None)

    def test18_conv_num_fail(self):
        self.assertTrue(task.conv_num("123.45.7") is None)

    def test19_my_datetime(self):
        self.assertTrue(task.my_datetime(0), '01-01-1970')

    def test20_my_datetime(self):
        self.assertTrue(task.my_datetime(123456789), '11-29-1973')

    def test21_my_datetime(self):
        self.assertTrue(task.my_datetime(9876543210), '12-22-2282')

    def test22_my_datetime(self):
        self.assertTrue(task.my_datetime(201653971200), '02-29-8360')

    def test23_my_datetime(self):
        self.assertTrue(task.my_datetime(854785485), '02-01-1997')

    def test24_my_datetime(self):
        self.assertTrue(task.my_datetime(7418529633), '01-31-2205')

    def test25_my_datetime(self):
        self.assertTrue(task.my_datetime(789456123), '01-07-1995')

    def test26_my_datetime(self):
        self.assertTrue(task.my_datetime(456987132), '06-25-1984')

    def test27_my_datetime(self):
        self.assertTrue(task.my_datetime(963258741), '07-10-2000')

    def test28_my_datetime(self):
        self.assertTrue(task.my_datetime(412587963), '01-28-1983')

    def test29_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(954786) == '0E 91 A2')

    def test30_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(-954786) == '-0E 91 A2')

    def test31_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(954786, 'big') == '0E 91 A2')

    def test32_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(-954786, 'big') == '-0E 91 A2')

    def test33_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(954786, 'little') == 'A2 91 0E')

    def test34_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(-954786, 'little') == '-A2 91 0E')

    def test35_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(num=9547, endian='big') == '25 4B')

    def test36_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(num=-95, endian='little') == '-5F')

    def test37_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(-54016, 'big') == '-D3 00')

    def test38_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(54016, 'little') == '00 D3')

    def test39_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(0, 'big') == '00')

    def test40_conv_endian_ok(self):
        self.assertTrue(task.conv_endian(999, 'little') == 'E7 03')

    def test41_conv_endian_fail(self):
        self.assertTrue(task.conv_endian(999, '') is None)

    def test42_conv_endian_fail(self):
        self.assertTrue(task.conv_endian(999, 'small') is None)


if __name__ == '__main__':
    unittest.main()
