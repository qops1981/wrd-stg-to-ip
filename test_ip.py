#!/usr/bin/env python3

import unittest
from ip import IP_Address
 
class TestIPConversions(unittest.TestCase):

	def test_hexadecimal(self):	# Test that a Hexadecimal input converts to all other values 

		hex_ip = '0x62d2ed4b'
		str_ip = '98.210.237.75'
		int_ip = 1657990475

		ip = IP_Address()
		ip.hexa_ip = hex_ip

		self.assertEqual(str_ip, ip.string_ip)	# Test conversion to string IP from Hexadecimal
		self.assertEqual(hex_ip, ip.hexa_ip)	# Test that input remains unchanged
		self.assertEqual(int_ip, ip.int_ip)		# Test conversion to INT IP from Hexadecimal

	def test_integer(self):		# Test that a Integer input converts to all other values 

		hex_ip = '0x62d2ed4b'
		str_ip = '98.210.237.75'
		int_ip = 1657990475

		ip = IP_Address()
		ip.int_ip = int_ip

		self.assertEqual(str_ip, ip.string_ip)
		self.assertEqual(hex_ip, ip.hexa_ip)
		self.assertEqual(int_ip, ip.int_ip)

	def test_string(self):			# Test that a String input converts to all other values 

		hex_ip = '0x62d2ed4b'
		str_ip = '98.210.237.75'
		int_ip = 1657990475

		ip = IP_Address()
		ip.string_ip = str_ip

		self.assertEqual(str_ip, ip.string_ip)
		self.assertEqual(hex_ip, ip.hexa_ip)
		self.assertEqual(int_ip, ip.int_ip)

	def test_cidr_check(self):		# Test that IP Input correctly evalutaes if in CIDR range

		ip = IP_Address()
		ip.hexa_ip = '0x62d2ed4b'
		ip.cidr    = '98.210.237.0/24'

		self.assertEqual(True, ip.in_cidr)

	def test_typecheck(self):		# Test non-IP's fail type evaluation

		ip = IP_Address()

		with self.assertRaises(ValueError):
			ip.string_ip = '98A.210.237.75'


if __name__ == '__main__':
    unittest.main()