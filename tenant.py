import logging

logging.basicConfig(
    filename = "scheduler_log.txt",
    level=logging.INFO,
    format="%(asctime)s -%(message)s"

)
import time

class Tenant:
    def __init__(self,name,cpu_demand,memory_demand, workload_duration,priority=5):
        self.name = name
        self.cpu_demand = cpu_demand
        self.memory_demand = memory_demand
        self.workload_duration=workload_duration
        self.priority = priority
    
    def __repr__(self):
        return f"Tenant({self.name}, CPU: {self.cpu_demand}% , Mem: {self.memory_demand}MB )"
    
    def simulate_workload(self):
        logging.info(f"{self.name} started workload for {self.workload_duration}ms")
        print(f"{self.name} is consuming resources")
        time.sleep(self.workload_duration/1000.0)
        logging.info(f"{self.name} finished workload")
        print(f"{self.name} workload complete.\n")