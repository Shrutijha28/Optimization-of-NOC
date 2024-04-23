import time

class Request:
    def __init__(self, address):
        self.address = address

class CPU:
    def __init__(self):
        self.requests = []

    def send_request(self, request):
        self.requests.append(request)

class IO:  # Define the IO class with the send_request method
    def __init__(self):
        self.requests = []

    def send_request(self, request):
        self.requests.append(request)

class SystemMemory:
    def __init__(self):
        self.data = {}

    def read_data(self, address):
        time.sleep(0.1)  # Simulate read latency
        return self.data.get(address)

    def write_data(self, address, data):
        time.sleep(0.1)  # Simulate write latency
        self.data[address] = data

class NOC:
    def __init__(self, cpu, io, memory):
        self.cpu = cpu
        self.io = io
        self.memory = memory
        self.latency = 0

    def route_data(self):
        for request in self.cpu.requests:
            start_time = time.time()
            data = self.memory.read_data(request.address)
            end_time = time.time()
            self.latency += end_time - start_time
            print("Data routed to CPU:", data)

        for request in self.io.requests:
            start_time = time.time()
            data = self.memory.read_data(request.address)
            end_time = time.time()
            self.latency += end_time - start_time
            print("Data routed to IO:", data)

    def calculate_bandwidth(self, simulation_time):
        total_data_transferred = len(self.cpu.requests) + len(self.io.requests)
        bandwidth = total_data_transferred / simulation_time
        print("Bandwidth:", bandwidth, "requests per second")

# Example usage
cpu = CPU()
io = IO()
memory = SystemMemory()
noc = NOC(cpu, io, memory)

# Write data to memory
memory.write_data(0x1000, "Data for address 0x1000")
memory.write_data(0x2000, "Data for address 0x2000")

# Simulate requests
cpu.send_request(Request(address=0x1000))
io.send_request(Request(address=0x2000))

# Route data through NOC
noc.route_data()

# Calculate and print performance metrics
simulation_time = 0.2  # Simulation time in seconds
noc.calculate_bandwidth(simulation_time)
print("Latency:", noc.latency)

