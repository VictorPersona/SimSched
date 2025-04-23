from visualize import plot_resource_usage
from tenant import Tenant
import logging

logging.basicConfig(
    filename = "scheduler_log.txt",
    level=logging.INFO,
    format="%(asctime)s -%(message)s"

)

def create_simple_tenants():
    tenant_1 = Tenant("Tenant A",50,1024,100,10)
    tenant_2 = Tenant("Tenant B",30,512,200,4)
    tenant_3 = Tenant("Tenant_C", 70, 2048, 300,1)

    tenants = [tenant_1,tenant_2,tenant_3]
    return tenants
    

def round_robin_scheduler(tenants):
    logging.info(f"Running Round Robin Scheduler")
    cpu_usages = []
    mem_usages = []
    labels = []
    print("\nScheduling tenants...")

    for tenant in tenants:
        logging.info(f"Allocating {tenant.name} -> CPU:{tenant.cpu_demand}%, Memory:{tenant.memory_demand}MB")
        print(f"Allocating resources to {tenant.name}:")
        tenant.simulate_workload()
        print(f"{tenant.name} - CPU :{tenant.cpu_demand}%, Mem: {tenant.memory_demand}MB\n")

        cpu_usages.append(tenant.cpu_demand)
        mem_usages.append(tenant.memory_demand)
        labels.append(tenant.name)
    
    plot_resource_usage(cpu_usages,mem_usages,labels)

def priority_scheduler(tenants):
    cpu_usages = []
    mem_usages = []
    labels = []
    tenants = sorted(tenants,key=lambda t: t.priority)

    for tenant in tenants:
        print(f"Scheduling {tenant.name} [Priority : {tenant.priority}]\n")
        tenant.simulate_workload()

        cpu_usages.append(tenant.cpu_demand)
        mem_usages.append(tenant.memory_demand)
        labels.append(tenant.name)
    
    plot_resource_usage(cpu_usages,mem_usages,labels)

def fair_scheduler(tenants):
    tenants = sorted(tenants,key=lambda t:t.cpu_demand * t.workload_duration)
    
    cpu_usages = []
    mem_usages = []
    labels = []

    for tenant in tenants:
        print(f"Scheduling {tenant.name} [Total demand : {tenant.cpu_demand * tenant.workload_duration}]\n")
        tenant.simulate_workload()

        cpu_usages.append(tenant.cpu_demand)
        mem_usages.append(tenant.memory_demand)
        labels.append(tenant.name)
    
    plot_resource_usage(cpu_usages,mem_usages,labels)

if __name__ == "__main__":
    tenants = create_simple_tenants()

    print("Choose Scheduling Policy")
    print("1. Round Robin")
    print("2. Priority-Based")
    print("3. Fairness (Least Demand First)")
    choice = input("Enter Choice (1/2/3): ")

    if(choice =="1"):
        round_robin_scheduler(tenants)
    elif(choice=="2"):
        priority_scheduler(tenants)
    elif(choice=="3"):
        fair_scheduler(tenants)
    else:
        print("Invalid Choice")