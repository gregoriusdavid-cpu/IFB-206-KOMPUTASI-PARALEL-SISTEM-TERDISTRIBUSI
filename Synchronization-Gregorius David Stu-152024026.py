def bankers_algorithm(available, allocation, max_need):
    num_processes = len(allocation)
    num_resources = len(available)
    need = [[max_need[i][j] - allocation[i][j] for j in range(num_resources)] for i in range(num_processes)]
    work = available[:]
    finish = [False] * num_processes
    safe_sequence = []

    while len(safe_sequence) < num_processes:
        found = False
        for i in range(num_processes):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(num_resources)):
                    for j in range(num_resources):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True
                    break
        if not found:
            print("Tidak ada safe state. Sistem dalam kondisi tidak aman.")
            return None
    return safe_sequence

available_resources = [3, 3, 2]
allocation_matrix = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
max_matrix = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

print("=== Banker's Algorithm ===")
print("Available resources:", available_resources)
print("Allocation matrix:")
for row in allocation_matrix:
    print(row)
print("Max matrix:")
for row in max_matrix:
    print(row)

seq = bankers_algorithm(available_resources, allocation_matrix, max_matrix)
if seq is not None:
    print("Safe state tercapai.")
    print("Safe sequence:", " -> ".join(f"P{p}" for p in seq))