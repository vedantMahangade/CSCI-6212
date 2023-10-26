import time
import random


# Generates a list of n number of client machines.
def generate_client_machine_list(n,k):
    client_machines = []
    i = 0
    for i in range(0, n):
        client_machines.append(random.randint(1, 100))
    server_locations = [] #remove when we find real server locations
    j = 0; step_size=int(n/k) #remove when we find real server locations
    for j in range(int(step_size/2),n,step_size): #remove when we find real server locations
        server_locations.append(j) #remove when we find real server locations
    return client_machines,server_locations

# calculate traffic according to current server position state
def calculate_traffic_and_labels(client_machine_weights,server_locations):
    total_traffic = 0
    all_label = []
    for i in range(0,len(client_machine_weights)):
        dist_from_all_servers = [abs(server - i) for server in server_locations]
        ith_label=dist_from_all_servers.index(min(dist_from_all_servers))
        all_label.append(ith_label)
        total_traffic += dist_from_all_servers[ith_label]*client_machine_weights[i]
    return total_traffic,all_label


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
    list_of_client_machines,list_of_server_locations = generate_client_machine_list(n=n_list,k=k_list)
    tot_traffic,old_labels = calculate_traffic_and_labels(list_of_client_machines,list_of_server_locations)

    print(list_of_client_machines)
    print(tot_traffic)

    # Start time (in ns) of when the function to implement runs.
    # start = time.perf_counter_ns()

    # TODO FUNCTION TO IMPLEMENT

    # End time (in ns) of when the function to implement runs.
    # end = time.perf_counter_ns()
