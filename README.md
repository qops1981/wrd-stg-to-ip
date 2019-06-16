# Interview Homework (String INT to IP)
#### William DeLuca

### IP_Address Class
This class allows an input that will then be converted into the following:
* String Representation of an IP address (e.g. `98.210.237.75`)
* Integer Representation of an IP address (e.g. `1657990475`)
* Hexadecimal Representation of an IP address (e.g. `0x62D2ED4B`)

#### Examples
```ruby
# Example 1
ip = IP_Address.new
ip.hexa_ip = '0x62D2ED4B'

ip.string_ip 	#=> '98.210.237.75'
ip.hexa_ip 		#=> '0x62D2ED4B'
ip.int_ip 		#=> 1657990475

# Example 2
ip = IP_Address.new(hexa_ip: '0x62D2ED4B')

ip.string_ip 	#=> '98.210.237.75'
ip.hexa_ip 		#=> '0x62D2ED4B'
ip.int_ip 		#=> 1657990475
```

### Unit Testing
Testing setup to a list of explicit scenarios
```bash
./test_ip.rb
```