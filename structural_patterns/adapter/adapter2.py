class Socket: #gniazdko
    def __init__(self, voltage):
        self.voltage = voltage

class EuropeanSocket(Socket):
    def __init__(self):
        super().__init__(230)
        

class USASocket(Socket):
    def __init__(self):
        super().__init__(120)
        
class Device:
    max_voltage = 120

    def try_charge(self, input_voltage):
        if input_voltage > self.max_voltage:
            print(f'Urządzenie spalone!') 
        else:
            print('charging ...')

#adapter
class Charger():    
    def __init__(self, device, socket):
        self.socket = socket
        self.device = device

    def __transformator(self):
        if self.socket.voltage <= self.device.max_voltage:
            return self.socket.voltage
        else:
            voltage = self.socket.voltage
            print('napięcie zostało dostosowane')
            voltage = self.device.max_voltage
            return voltage 
        
    def plug(self):
        return self.__transformator()
    

device = Device()
socket = EuropeanSocket()
charger = Charger(device, socket)
device.try_charge(charger.plug())






