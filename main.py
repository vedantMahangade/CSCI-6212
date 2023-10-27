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
    try: 
        server_locations += 0
    except TypeError:
        #print('type error so loop through multiple servers')
        for i in range(0,len(client_machine_weights)):
            dist_from_all_servers = [abs(server - i) for server in server_locations]
            ith_label=dist_from_all_servers.index(min(dist_from_all_servers))
            all_label.append(ith_label)
            total_traffic += dist_from_all_servers[ith_label]*client_machine_weights[i]
    else:
        #print('no typeerror, only one server')
        for i in range(0,len(client_machine_weights)):
            dist_from_all_server = abs(server_locations - i)
            total_traffic += dist_from_all_server*client_machine_weights[i]
    return total_traffic,all_label

def move_servers(client_machine_weights,all_label):
    j=0
    server_locations = []
    for i in range(0,max(all_label)+1):
        temp_traffic = float('inf')
        #print('Reset traffic to: ', temp_traffic)
        temp_weights = []
        startj = j
        while all_label[j] == i:
            #print(client_machine_weights[j])
            temp_weights.append(client_machine_weights[j])
            j += 1
            if j == len(client_machine_weights):
                break
        #print('temp weights',temp_weights)
        for k in range(0,j-startj):
            #print('temppweights:',temp_weights,'and k', k)
            temptraffic = calculate_traffic_and_labels(temp_weights,k)[0]
            #print('temptraffic',temptraffic, 'for group', i)
            if temptraffic <= temp_traffic:
                #print('Current traffic:', temp_traffic, 'and current server: ', k)
                #print('New traffic', temptraffic, 'and new server', k)
                #print('___')
                append_server_pos = startj + k
                temp_traffic = temptraffic
        #print('testing', append_server_pos)
        server_locations.append(append_server_pos)
    return server_locations

def run_iterations(list_of_client_machines,old_labels):
    # Start time (in ns) of when the function to implement runs.
    start = time.perf_counter_ns()
    for i in range(0,1000):
        new_servers = move_servers(list_of_client_machines,old_labels)
        tot_traffic,new_labels = calculate_traffic_and_labels(list_of_client_machines,new_servers)
        if old_labels == new_labels:
            break
        else:
            old_labels = new_labels
        print("New traffic: ", tot_traffic, " --- Current iteration: ", i, " --- New server locations: ", new_servers) 
    # End time (in ns) of when the function to implement runs.
    end = time.perf_counter_ns()
    return end-start

if __name__ == "__main__":
    # Gives the user the option to enter how many list sizes they want.
    n_list = int(1000)#int(input("Enter number of client machines: "))

    # Gives user the option to enter k number of servers to implement
    k_list= int(12)#int(input("Enter number of servers: "))
    # Generates n number of client machines
    list_of_client_machines,list_of_server_locations = generate_client_machine_list(n=n_list,k=k_list)
    tot_traffic,old_labels = calculate_traffic_and_labels(list_of_client_machines,list_of_server_locations)
    print('initial servers', list_of_server_locations)
    print('initial_traffic', tot_traffic)
    #print(list_of_client_machines)
    #new_servers = move_servers(list_of_client_machines,old_labels)
    #new_traffic,new_labels = calculate_traffic_and_labels(list_of_client_machines,new_servers)
    #print('new_servers', new_servers)
    #print('new traffic', new_traffic)
    time_ = run_iterations(list_of_client_machines,old_labels)
