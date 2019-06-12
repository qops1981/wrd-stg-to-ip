#!/usr/bin/env ruby

require 'ipaddr'

class IP_Address

    attr_reader :object_ip, :string_ip, :hexa_ip, :int_ip, :cidr

    def initialize()
        @object_ip = nil
        @string_ip = nil
        @hexa_ip   = nil
        @int_ip    = nil
        
        @cidr      = nil   
    end

    def string_ip=(str)
        @string_ip = str
        @object_ip = str_to_obj(@string_ip)
        @int_ip    = str_to_int(@string_ip)
        @hexa_ip   = int_to_hex(@int_ip)
    end

    def hexa_ip=(hex)
        @hexa_ip   = hex
        @int_ip    = hex_to_int(@hexa_ip)
        @string_ip = int_to_ipa(@int_ip)
        @object_ip = str_to_obj(@string_ip)
    end

    def int_ip=(i)
        @int_ip    = i
        @string_ip = int_to_ipa(@int_ip)
        @object_ip = str_to_obj(@string_ip)
        @hexa_ip   = int_to_hex(@int_ip)
    end

    def cidr=(c)
        @cidr = str_to_obj(c)
    end

    def str_to_int(str_value) str_value.split(".").map(&:to_i).pack('CCCC').unpack('N')[0] end
    def int_to_ipa(int_value) [int_value].pack('N').unpack('CCCC').join('.') end
    def int_to_hex(int_value) '0x' + int_value.to_s(16).upcase end
    def hex_to_int(hex_value) hex_value.to_i(16) end

    def str_to_obj(str_value) IPAddr.new(str_value) rescue raise('ERROR: Not Recognized as an IP address') end

    def in_cidr
        raise('ERROR: no IP set for comparison') if @object_ip.nil?
        raise('ERROR: no CIDR value set for comparison') if @cidr.nil?
        @cidr.include?(@object_ip)
    end

end

example_hex_ip = '0x62D2ED4B'
#example_str_ip = '98.210.237.75'
#example_int_ip = 1657990475

#bad_example_str_ip = '98A.210.237.75'

ip = IP_Address.new

#ip.int_ip    = example_int_ip
ip.hexa_ip   = example_hex_ip
#ip.string_ip = example_str_ip

#ip.string_ip = bad_example_str_ip

ip.cidr = '98.210.237.0/24'

#ip = IPAddr.new(example_str_ip)
#p ip.to_string
#p ip.to_i

p ip.hexa_ip
p ip.int_ip
p ip.string_ip
p ip.object_ip
p ip.cidr
p ip.in_cidr
