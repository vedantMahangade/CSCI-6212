import time
import random


# Generates a list of n number of client machines.
def generate_client_machine_list(n):
    client_machines = []
    i = 0
    for i in range(0, n):
        client_machines.append(random.randint(1, 10))
        i += 1
    return client_machines


# returns the total weight of the client_machines
def get_total_weights(client_machines):
    total = 0
    
    for machine in client_machines:
        total += machine

    return total


if __name__ == "__main__":
    # Gives the user the option to enter how many list sizes they want.
    n_list = int(input("Enter number of client machines: "))

    # Gives user the option to enter k number of servers to implement
    k = int(input("Enter number of servers: "))

    # Generates n number of client machines
    list_of_client_machines = generate_client_machine_list(n=n_list)

    print(list_of_client_machines)

    # Start time (in ns) of when the function to implement runs.
    # start = time.perf_counter_ns()

    # TODO FUNCTION TO IMPLEMENT

    # End time (in ns) of when the function to implement runs.
    # end = time.perf_counter_ns()
