from serial.tools import list_ports


class Api:

    def get_all_ports(self):
        ports = list_ports.comports()
        res = []

        for port in ports:
            res.append(port.device)

        return res

    def test(self):
        raise NotImplementedError()
