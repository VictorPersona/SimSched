from tenant import Tenant

def test_tenant_class():
    tenant_1 = Tenant("Tenant A",50,1024,100)
    tenant_2 = Tenant("Tenant B",30,512,200)

    print(tenant_1)
    print(tenant_2)

    tenant_1.simulate_workload()
    tenant_2.simulate_workload()

if __name__ == "__main__":
    test_tenant_class()