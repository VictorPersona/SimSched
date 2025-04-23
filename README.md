

---

```
# Simulated Resource Scheduler for Multi-Tenant Environments

## 🧠 Overview

This project simulates how an operating system can schedule CPU and memory resources across multiple tenants in a cloud environment. Each tenant has distinct workload profiles, simulating real-world scenarios like CPU-bound, memory-intensive, and I/O-heavy applications.



## ⚙️ Features

- CLI-based simulation of tenant workloads.
- Three basic scheduling strategies:
  - Round Robin
  - Priority-Based
  - Fairness (Least Total Demand First)
- Resource usage visualization using `matplotlib`.
- Logging of execution flow to aid explanation and reproducibility.

## 📦 Technologies Used

- Python 3
- `matplotlib` for visualizing CPU and memory allocation
- `time` and `random` for simulating tenant activity
- `logging` (optional) for tracking activity

## 🧪 How to Run

1. Install dependencies:
   ```bash
   pip install matplotlib
   ```

2. Run the simulation:
   ```bash
   python main.py
   ```

3. Choose a scheduling policy (Round Robin, Priority, or Fairness).

4. Watch the console for simulation logs and observe the plots for resource utilization.

## 📁 Project Structure

```
.
├── tenant.py            # Tenant class with simulated workloads
├── main.py              # Scheduler logic and user interaction
├── visualize.py         # Plotting CPU and memory usage
├── scheduler_log.txt    # [Optional] Log file of scheduling activity
└── README.md            # Project overview
```

## 🌱 Future Enhancements

- Introduce realistic I/O modeling per tenant.
- Use Linux namespaces or Docker containers for deeper simulation.
- Explore cgroup-based real-time control in future iterations.
- Evaluate scheduling algorithms with dynamically changing workloads.

---

This simulation shows my early initiative toward understanding the technical challenges of scheduling in OS-aware multi-tenant cloud databases. It also forms a core component of my application portfolio for the MEXT scholarship and cloud-focused graduate studies.
```

---

