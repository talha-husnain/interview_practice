from queue import Queue, PriorityQueue


def determine_data_structure(lines):
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
                # Priority queue in Python is min-heap, so invert values for max-heap behavior
                pq.put(-value)
        else:
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
