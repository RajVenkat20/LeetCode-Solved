class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validateIPv4(ip):
            arr = ip.split('.')
            for part in arr:
                if(len(part) == 0 or len(part) > 3):
                    return "Neither"
                elif(not part.isdigit()):
                    return "Neither"
                elif(part[0] == "0" and len(part) != 1):
                    return "Neither"
                elif(int(part) > 255):
                    return "Neither"

            return "IPv4"

        def validateIPv6(ip):
            arr = ip.split(':')
            hexa = set(['0', '1', '2', '3', '4', '5', '6', '7',
                       '8', '9', 'a', 'b', 'c', 'd', 'e', 'f',
                       'A', 'B', 'C', 'D', 'E', 'F'])
            for part in arr:
                if(len(part) == 0 or len(part) > 4):
                    return "Neither"
                for char in part:
                    if(char not in hexa):
                        return "Neither"

            return "IPv6"

        if(queryIP.count('.') == 3):
            return validateIPv4(queryIP)
        elif(queryIP.count(':') == 7):
            return validateIPv6(queryIP)
        else:
            return "Neither"