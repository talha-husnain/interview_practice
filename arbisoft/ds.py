import sys
from queue import Queue, PriorityQueue


def determine_data_structure(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    num_operations = int(lines[0].strip())
    is_stack, is_queue, is_pq = True, True, True
    stack, queue, pq = [], Queue(), PriorityQueue()

    for line in lines[1:]:
        operation, value = line.strip().split()
        value = int(value)

        if operation == "push":
            if is_stack:
                stack.append(value)
            if is_queue:
                queue.put(value)
            if is_pq:
                pq.put(-value)  # Python's PriorityQueue is a min-heap
        else:  # pop operation
            if is_stack and (not stack or stack.pop() != value):
                is_stack = False
            if is_queue and (queue.empty() or queue.get() != value):
                is_queue = False
            if is_pq and (pq.empty() or -pq.get() != value):
                is_pq = False

    if [is_stack, is_queue, is_pq].count(True) > 1:
        return "NOT SURE"
    elif is_stack:
        return "LIFO"
    elif is_queue:
        return "FIFO"
    elif is_pq:
        return "PQ"
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path as an argument")
    else:
        file_path = sys.argv[1]
        result = determine_data_structure(file_path)
        print(result)

# Usage: python script_name.py input_file.txt
