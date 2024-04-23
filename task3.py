import time
from dataclasses import dataclass

from task2 import CPU, NOC  # Importing necessary classes

class SystemMemory:
    def __init__(self):
        self.data = {}

    def read_data(self, address):
        time.sleep(0.1)  # Simulate read latency
        return self.data.get(address)

    def write_data(self, address, data):
        time.sleep(0.1)  # Simulate write latency
        self.data[address] = data

class Request:
    def __init__(self, address):
        self.address = address

@dataclass
class URLRequest:
    address: int

class IO:
    def __init__(self):
        self.requests = []

    def send_request(self, request):
        self.requests.append(request)

class Buffer:
    def __init__(self, size):
        self.size = size
        self.data = []

    def add_data(self, data):
        if len(self.data) < self.size:
            self.data.append(data)
        else:
            print("Buffer overflow: Data discarded")

    def remove_data(self):
        if self.data:
            return self.data.pop(0)
        else:
            print("Buffer is empty")

class Arbiter:
    def __init__(self):
        self.weights = {}

    def set_weights(self, weights):
        self.weights = weights

    def prioritize_requests(self, requests):
        # Implement weighted round-robin arbitration logic
        pass

class PowerManagement:
    def __init__(self, threshold):
        self.threshold = threshold

    def check_power_limit(self, current_power):
        if current_power > self.threshold:
            return True
        else:
            return False

    def throttle(self):
        # Implement throttling logic based on power limits
        pass

# Example usage
cpu = CPU()
io = IO()
memory = SystemMemory()
noc = NOC(cpu, io, memory)
buffer = Buffer(size=10)
arbiter = Arbiter()
power_manager = PowerManagement(threshold=100)  # Set power threshold

# Simulate requests
cpu.send_request(Request(address=0x1000))
print("CPU request sent")

io.send_request(Request(address=0x2000))
print("IO request sent")

# Route data through NOC
noc.route_data()
print("Data routed through NOC")

# Monitor power usage
current_power = 90  # Simulated current power usage
if power_manager.check_power_limit(current_power):
    power_manager.throttle()
    print("Throttling applied")

# Add more functionality as needed for simulation control and data collection
