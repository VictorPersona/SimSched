from tenant import Tenant

def test_tenant_class():
    tenant_1 = Tenant("Tenant A",50,1024,100)
    tenant_2 = Tenant("Tenant B",30,512,200)
    tenant_3 = Tenant("Tenant_C", 70, 2048, 300)

    tenants = [tenant_1,tenant_2,tenant_3]

    print("Starting round-robin scheduler...\n")
    round_robin_scheduler(tenants)


def round_robin_scheduler(tenants):
    print("\nScheduling tenants...")

    for tenant in tenants:
        print(f"Allocating resources to {tenant.name}:")
        tenant.simulate_workload()
        print(f"{tenant.name} - CPU :{tenant.cpu_demand}%, Mem: {tenant.memory_demand}MB\n")

if __name__ == "__main__":
    test_tenant_class()