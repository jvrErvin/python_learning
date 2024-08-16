import argparse
import time
from multiprocessing import Process, Queue

from tqdm import tqdm


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments for the number of workers and the number of tasks.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Run a multiprocessing task with a specified number of workers and tasks."
    )
    parser.add_argument(
        "--n_workers", type=int, default=4, required=False, help="Number of worker processes (default: 4)"
    )
    parser.add_argument(
        "--n_tasks", type=int, default=100, required=False, help="Number of tasks to be processed (default: 100)"
    )

    return parser.parse_args()


# Worker function
def worker(input_queue: Queue, output_queue: Queue) -> None:
    """
    Worker process that takes tasks from the input queue, processes them, and
    puts the results into the output queue.

    Args:
        input_queue (Queue): Queue from which the worker retrieves tasks.
        output_queue (Queue): Queue to which the worker sends processed results.

    Returns:
        None
    """
    while True:
        item = input_queue.get()
        if item is None:
            break  # Exit the loop if we receive a None signal

        # Simulate processing the item
        result = item * item  # For example, square the item
        time.sleep(1)  # Simulate some delay in processing
        output_queue.put(result)


# Writer function
def writer(output_queue: Queue, output_file: str) -> None:
    """
    Writer process that takes results from the output queue and writes them to
    a specified text file.

    Args:
        output_queue (Queue): Queue from which the writer retrieves results.
        output_file (str): Path to the file where results will be written.

    Returns:
        None
    """
    with open(output_file, "w") as f:
        while True:
            result = output_queue.get()
            if result is None:
                break  # Exit the loop if we receive a None signal
            f.write(f"{result}\n")


# Main function to set up the multiprocessing
def main(n_workers: int, n_tasks: int) -> None:
    """
    Sets up and manages the multiprocessing environment for parallel task processing.

    Args:
        n_workers (int): Number of worker processes to start.
        n_tasks (int): Number of tasks to be processed.

    Returns:
        None
    """
    input_queue = Queue()
    output_queue = Queue()

    # Start worker processes
    workers = []
    for _ in tqdm(range(n_workers), desc="Starting workers"):
        p = Process(target=worker, args=(input_queue, output_queue))
        p.start()
        workers.append(p)

    # Start writer process
    writer_process = Process(target=writer, args=(output_queue, "output.txt"))
    writer_process.start()

    # Put tasks in the input queue
    tasks = [i for i in range(n_tasks)]  # Example tasks
    for task in tqdm(tasks, desc="Adding tasks to queue"):
        input_queue.put(task)

    # Signal the workers to exit by sending None for each worker
    for _ in tqdm(range(n_workers), desc="Signalling workers to exit"):
        input_queue.put(None)

    # Wait for the workers to finish
    print("Waiting for workers to finish...")
    for p in workers:
        p.join()

    # Signal the writer to exit
    output_queue.put(None)

    # Wait for the writer to finish
    writer_process.join()

    print("All tasks have been processed and results written to output.txt")


if __name__ == "__main__":
    args = parse_arguments()  # Parse command-line arguments
    main(args.n_workers, args.n_tasks)  # Pass parsed arguments to main()
