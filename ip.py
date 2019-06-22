#!/usr/bin/env python3

"""
IMPRTANT NOTICE: Below is a replication of my Ruby class but in python. This is my first attempt at python, below is
inspired from various documentation online about how setup a python class. Additional some inspiration from 
stack overflow on how to convert Hexadecimals into IP's and vice versa.
"""

import socket
import struct
from ipaddress import ip_network, ip_address

class IP_Address(object):

    def __init__(self):
        self._object_ip = None
        self._string_ip = None
        self._hexa_ip   = None
        self._int_ip    = None
        
        self._cidr      = None

    # Supporting Methods

    def int_to_hex(self, int_value):
        return hex(int_value)

    def int_to_str(self, int_value):
        return socket.inet_ntoa(struct.pack("!I", int_value))

    def str_to_hex(self, str_value):
        return struct.unpack("!I", socket.inet_aton(str_value))[0]

    def str_to_int(self, str_value):
        return self.str_to_hex(str_value)

    def hex_to_int(self, hex_value):
        return int(hex_value, 16)

    # String to IP Properties

    @property
    def string_ip(self):
        return self._string_ip

    @string_ip.setter
    def string_ip(self, value):
        self._string_ip = value
        self._object_ip = ip_address(self._string_ip)
        self._int_ip    = self.str_to_int(self._string_ip)
        self._hexa_ip   = self.int_to_hex(self._int_ip)

    # Hexadecimal to IP Properties

    @property
    def hexa_ip(self):
        return self._hexa_ip

    @hexa_ip.setter
    def hexa_ip(self, value):
        self._hexa_ip = value.lower()
        self._int_ip    = self.hex_to_int(self._hexa_ip)
        self._string_ip = self.int_to_str(self._int_ip)
        self._object_ip = ip_address(self._string_ip)

    # Integer to IP Properties

    @property
    def int_ip(self):
        return self._int_ip

    @int_ip.setter
    def int_ip(self, value):
        self._int_ip = value    
        self._hexa_ip   = self.int_to_hex(self._int_ip)
        self._string_ip = self.int_to_str(self._int_ip)
        self._object_ip = ip_address(self._string_ip)

    # CIDR Setup

    @property
    def cidr(self):
        return self._cidr

    @cidr.setter
    def cidr(self, value):
        self._cidr = ip_network(value)

    @property
    def in_cidr(self):
        return self._object_ip in self._cidr


## Testing Codes during Development ##

#example_hex_ip = '0x62D2ED4B'
#example_str_ip = '98.210.237.75'
#example_int_ip = 1657990475
#
#bad_example_str_ip = '98A.210.237.75'
#
#ip = IP_Address()
#
#ip.int_ip    = example_int_ip
#ip.hexa_ip   = example_hex_ip
#ip.string_ip = example_str_ip
#ip.string_ip = bad_example_str_ip
#
#print(ip.string_ip)
#print(ip.int_ip)
#print(ip.hexa_ip)
#
#
#ip.cidr = '98.210.237.0/24'
#print(ip.cidr)
#print(ip.in_cidr)
