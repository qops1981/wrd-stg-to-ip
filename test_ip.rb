#! /usr/bin/env ruby

require_relative "ip"
require "test/unit"
 
class TestIPConversions < Test::Unit::TestCase

	def test_hexadecimal	# Test that a Hexadecimal input converts to all other values 

		hex_ip, str_ip, int_ip = '0x62D2ED4B', '98.210.237.75', 1657990475

		ip = IP_Address.new
		ip.hexa_ip = hex_ip

		assert_equal(str_ip, ip.string_ip)	# Test conversion to string IP from Hexadecimal
		assert_equal(hex_ip, ip.hexa_ip)	# Test that input remains unchanged
		assert_equal(int_ip, ip.int_ip)		# Test conversion to INT IP from Hexadecimal

	end

	def test_integer		# Test that a Integer input converts to all other values 

		hex_ip, str_ip, int_ip = '0x62D2ED4B', '98.210.237.75', 1657990475

		ip = IP_Address.new
		ip.int_ip = int_ip

		assert_equal(str_ip, ip.string_ip)
		assert_equal(hex_ip, ip.hexa_ip)
		assert_equal(int_ip, ip.int_ip)

	end

	def test_string			# Test that a String input converts to all other values 

		hex_ip, str_ip, int_ip = '0x62D2ED4B', '98.210.237.75', 1657990475

		ip = IP_Address.new
		ip.string_ip = str_ip

		assert_equal(str_ip, ip.string_ip)
		assert_equal(hex_ip, ip.hexa_ip)
		assert_equal(int_ip, ip.int_ip)

	end

	def test_cidr_check		# Test that IP Input correctly evalutaes if in CIDR range

		ip = IP_Address.new
		ip.hexa_ip = '0x62D2ED4B'
		ip.cidr    = '98.210.237.0/24'

		assert_equal(true, ip.in_cidr)

	end

	def test_typecheck		# Test non-IP's fail type evaluation

		ip = IP_Address.new
		
    	assert_raise( RuntimeError ) { ip.string_ip = '98A.210.237.75' }

  	end
 
end
