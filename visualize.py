import matplotlib.pyplot as plt

def plot_resource_usage(cpu_usages,mem_usages,labels):
    x = range(len(labels))
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)

    plt.bar(x,cpu_usages, color='skyblue')
    plt.xticks(x,labels,rotation=45)

    plt.title("CPU Usage (%)")
    plt.xlabel("Tenant")
    plt.ylabel("CPU %")

    plt.subplot(1,2,2)
    plt.bar(x,mem_usages,color="salmon")

    plt.xticks(x,labels,rotation=45)
    plt.title("Memory Usage (MB)")
    plt.xlabel("Tenant")
    plt.ylabel("Memory")

    plt.tight_layout()

    plt.show()