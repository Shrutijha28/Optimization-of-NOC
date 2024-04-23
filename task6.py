# Import necessary modules
import time
from typing import IO as IO_Type
from task2 import CPU

# Define a custom Request class
class CustomRequest:
    def __init__(self, address):
        self.address = address

# Define the enhanced SystemMemory class with latency simulation
class SystemMemory:
    def __init__(self):
        self.data = {}

    def read_data(self, address):
        time.sleep(0.1)  # Simulate read latency
        return self.data.get(address)

    def write_data(self, address, data):
        time.sleep(0.1)  # Simulate write latency
        self.data[address] = data

# Define enhanced NOC class with data routing and performance metrics
class NOC:
    def __init__(self, cpu, io, memory):
        self.cpu = cpu
        self.io = io
        self.memory = memory
        self.latency = 0
        self.total_requests = 0
        self.buffer_occupancy = 0

    def route_data(self):
        for request in self.cpu.requests:
            start_time = time.time()
            data = self.memory.read_data(request.address)
            end_time = time.time()
            self.latency += end_time - start_time
            self.total_requests += 1
            print("Data routed to CPU:", data)

        for request in self.io.requests:
            start_time = time.time()
            data = self.memory.read_data(request.address)
            end_time = time.time()
            self.latency += end_time - start_time
            self.total_requests += 1
            print("Data routed to IO:", data)

    def calculate_bandwidth(self, simulation_time):
        total_data_transferred = self.total_requests
        bandwidth = total_data_transferred / simulation_time
        print("Bandwidth:", bandwidth, "requests per second")

    def calculate_latency(self):
        print("Latency:", self.latency)

    def calculate_buffer_occupancy(self):
        # Calculate buffer occupancy based on the number of requests in the buffers
        cpu_buffer_occupancy = len(self.cpu.requests)
        io_buffer_occupancy = len(self.io.requests)
        self.buffer_occupancy = cpu_buffer_occupancy + io_buffer_occupancy
        print("Buffer Occupancy:", self.buffer_occupancy)

# Define IO class with send_request method
class IO:
    def __init__(self):
        self.requests = []

    def send_request(self, request):
        self.requests.append(request)

# Example usage
cpu = CPU()
io = IO()
memory = SystemMemory()
noc = NOC(cpu, io, memory)

# Simulate requests
cpu.send_request(CustomRequest(address=0x1000))
io.send_request(CustomRequest(address=0x2000))

# Route data through NOC
noc.route_data()

# Calculate and print performance metrics
simulation_time = 0.2  # Simulation time in seconds
noc.calculate_bandwidth(simulation_time)
noc.calculate_latency()
noc.calculate_buffer_occupancy()
