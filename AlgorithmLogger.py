import os
import time
import tracemalloc

class AlgorithmLogger:
    def __init__(self, method_name, n, m):
        self.start_time = None
        self.method_name = method_name

        self.directory = 'results'
        os.makedirs(self.directory, exist_ok=True)

        self.filename = f'{self.directory}/{n}x{m}_{method_name}.txt'

        self.logs = []

    def log(self, text):
        self.logs.append(text)

    def start_measure(self):
        tracemalloc.start()
        self.start_time = time.perf_counter()

    def stop_measure(self):
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.perf_counter()
        return (end_time - self.start_time), (peak_memory / 1024)

    # max_frontier_size = zbiór odkrytych węzłów, które nie zostały jeszcze przetworzone,
    # odnosi się do max_queue_size lub max_stack_size w zależności od algorytmu
    def save(self, result_matrix, path, execution_time, peak_memory_kb, total_visited, max_frontier_size):
        with open(self.filename, 'w') as f:
            f.write(f'Algorithm: {self.method_name.upper()}\n')
            f.write(f'Execution time: {execution_time:.6f} s\n')
            f.write(f'Peak memory usage: {peak_memory_kb:.2f} KB\n')
            f.write(f'Visited nodes: {total_visited}\n')
            f.write(f'Maximum frontier size: {max_frontier_size}\n')
            f.write(f'Path length: {len(path)}\n\n')

            f.write('Final matrix:\n')
            for row in result_matrix:
                f.write(' '.join(map(str, row)) + '\n')

            f.write('\n--- Steps ---\n')
            for line in self.logs:
                f.write(line + '\n')
