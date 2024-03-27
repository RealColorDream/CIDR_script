# CIDR calculator is a simple python script to calculate the CIDR notation of an IP address.
## Usage:
```python
import CIDR as _

CIDR = _.CIDR("192.168.0.0", 24)
print(CIDR) # by default, it will print all the information of this ip
print(CIDR.first_IP_device())
```

## Methods:
```python
for method in dir(_.CIDR):
    if not method.startswith("__"):
        print(method)
# ['broadcast_IP', 'first_IP', 'first_IP_device', 'get_mask_Number', 'get_network_IP', 'last_IP', 'last_IP_device', 'number_of_IP', 'number_of_IP_device', 'parse_IP_to_int', 'parse_int_to_IP', 'parse_ip_to_list']
```
