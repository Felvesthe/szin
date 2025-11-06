import os
import time
import tracemalloc

class AlgorithmLogger:

    def __init__(self, method_name, n, m):
        self.peak_memory_kb = None
        self.execution_time = None
        self.start_time = None

        self.method_name = method_name

        self.directory = 'results'
        os.makedirs(self.directory, exist_ok=True)

        self.filename = f'{self.directory}/{n}x{m}_{method_name}.txt'

    def start_measure(self):
        tracemalloc.start()
        self.start_time = time.perf_counter()

    def stop_measure(self):
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.perf_counter()

        self.execution_time = end_time - self.start_time
        self.peak_memory_kb = peak_memory / 1024

    def save(self, result_matrix, path, total_visited):
        with open(self.filename, 'w') as f:
            f.write(f'Algorithm: {self.method_name.upper()}\n')
            f.write(f'Execution time: {self.execution_time:.6f} s\n')
            f.write(f'Peak memory usage: {self.peak_memory_kb:.2f} KB\n')
            f.write(f'Visited nodes: {total_visited}\n')
            f.write(f'Path length: {len(path)}\n\n')

            f.write('Final matrix:\n')
            for row in result_matrix:
                f.write(' '.join(map(str, row)) + '\n')
