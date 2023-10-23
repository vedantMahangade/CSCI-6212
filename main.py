import time


# Generates a list of n number of client machines.
def generate_client_machine_list(n):
    client_machines = []
    for client_machine in range(1, n+1):
        client_machines.append(client_machine)
    return client_machines


if __name__ == "__main__":

    # Gives the user the option to enter how many list sizes they want.
    n_list = int(input("Enter n lists: "))

    # Generates n number of client machines
    list_of_client_machines = generate_client_machine_list(n=n_list)

    print(list_of_client_machines)

    # Start time (in ns) of when the function to implement runs.
    start = time.perf_counter_ns()

    # TODO FUNCTION TO IMPLEMENT

    # End time (in ns) of when the function to implement runs.
    end = time.perf_counter_ns()
