import multiprocessing

def multiply_row(row, matrix_b, result_queue, row_idx):
    result_row = []
    for j in range(len(matrix_b[0])):
        total = 0
        for k in range(len(row)):
            total += row[k] * matrix_b[k][j]
        result_row.append(total)
    result_queue.put((row_idx, result_row))

if __name__ == "__main__":
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[5, 6], [7, 8]]
    
    q = multiprocessing.Queue()
    processes = []

    for i in range(len(matrix_a)):
        p = multiprocessing.Process(target=multiply_row, args=(matrix_a[i], matrix_b, q, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [q.get() for _ in range(len(matrix_a))]
    results.sort()
    
    final_result = [row for idx, row in results]
    print("Hasil Perkalian Matriks:", final_result)