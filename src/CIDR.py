class CIDR:
    def __init__(self, network_IP:str, mask_Number:int) -> None:
        """
        Calculate the network and devices IP addresses from a given network IP and mask number.
        :param network_IP:
        :param mask_Number:
        """
        self.network_IP = network_IP
        self.mask_Number = mask_Number

    def get_network_IP(self) -> str:
        """
        Get the network IP address.
        :return:
        """
        return self.network_IP

    def get_mask_Number(self) -> int:
        """
        Get the mask number.
        :return:
        """
        return self.mask_Number

    def parse_IP_to_int(self, ip) -> int:
        """
        Parse IP address to integer.
        :param ip:
        :return:
        """
        ip_list = ip.split(".")
        ip_int = 0
        for i in range(4):
            ip_int += int(ip_list[i]) << (24 - 8 * i)
        return ip_int

    def parse_int_to_IP(self, ip_int) -> str:
        """
        Parse IP address to string.
        :param ip_int:
        :return:
        """
        ip = ""
        for i in reversed(range(4)):
            ip += str((ip_int >> (8 * i)) & 0xFF) + "."
        return ip[:-1]

    def parse_ip_to_list(self, ip) -> list:
        """
        Parse IP address to list.
        :param ip:
        :return:
        """
        return ip.split(".")

    def first_IP(self) -> int:
        """
        Calculate the first IP address.
        :return:
        """
        return self.parse_IP_to_int(self.network_IP) & (0xFFFFFFFF << (32 - self.mask_Number))

    def last_IP(self) -> int:
        """
        Calculate the last IP address.
        :return:
        """
        return self.parse_IP_to_int(self.network_IP) | (0xFFFFFFFF >> self.mask_Number)

    def broadcast_IP(self) -> int:
        """
        Calculate the broadcast IP address.
        :return:
        """
        return self.last_IP()

    def first_IP_device(self) -> int:
        """
        Calculate the first IP address of devices.
        :return:
        """
        return self.first_IP() + 1

    def last_IP_device(self) -> int:
        """
        Calculate the last IP address of devices.
        :return:
        """
        return self.last_IP() - 1

    def number_of_IP(self) -> int:
        """
        Calculate the number of IP addresses.
        :return:
        """
        return self.last_IP() - self.first_IP() + 1

    def number_of_IP_device(self) -> int:
        """
        Calculate the number of devices IP addresses.
        :return:
        """
        return (self.last_IP() - self.first_IP() + 1) - 2

    def __eq__(self, other):
        """
        Compare two CIDR objects.
        :param other:
        :return:
        """
        ipDecimalList1 = self.parse_ip_to_list(self.network_IP)
        ipDecimalList2 = self.parse_ip_to_list(other.network_IP)
        for i in range(4):
            if ipDecimalList1[i] != ipDecimalList2[i]:
                return False
        if self.mask_Number != other.mask_Number:
            return False
        return True

    def __repr__(self):
        """
        print the network and devices IP addresses.
        :return:
        """
        return f"""        === Network ===
        first_IP: {self.parse_int_to_IP(self.first_IP())}
        last_IP: {self.parse_int_to_IP(self.last_IP())}
        broadcast_IP: {self.parse_int_to_IP(self.broadcast_IP())}
        number_of_IP: {self.number_of_IP()}
        === Devices ===
        first_IP_device: {self.parse_int_to_IP(self.first_IP_device())}
        last_IP_device: {self.parse_int_to_IP(self.last_IP_device())}
        number_of_IP_device: {self.number_of_IP_device()}\n"""

    def __str__(self):
        """
        print the network and devices IP addresses.
        :return:
        """
        return f"""        === Network ===
        first_IP: {self.parse_int_to_IP(self.first_IP())}
        last_IP: {self.parse_int_to_IP(self.last_IP())}
        broadcast_IP: {self.parse_int_to_IP(self.broadcast_IP())}
        number_of_IP: {self.number_of_IP()}
        === Devices ===
        first_IP_device: {self.parse_int_to_IP(self.first_IP_device())}
        last_IP_device: {self.parse_int_to_IP(self.last_IP_device())}
        number_of_IP_device: {self.number_of_IP_device()}\n"""

