import random
import time

class Tenant:
    def __init__(self,name,cpu_demand,memory_demand, io_demand):
        self.name = name
        self.cpu_demand = cpu_demand
        self.memory_demand = memory_demand
        self.io_demand=io_demand
    
    def __repr__(self):
        return f"Tenant({self.name}, CPU: {self.cpu_demand}% , Mem: {self.memory_demand}MB, I/O: {self.io_demand}ops )"
    
    def simulate_workload(self):
        print(f"{self.name} is consuming resources")
        time.sleep(random.uniform(0.5,2))
        print(f"{self.name} workload complete.")