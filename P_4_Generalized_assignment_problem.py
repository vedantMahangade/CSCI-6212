import numpy as np
import sys
import time

#Initialize employee-job matrix
time_elapsed = np.zeros((1, 100))

def calculate_total_payment(assignment, costs):
    # Initialize total payment
    total_payment = 0
    # Iterate through people in the mxm matrix
    for person, job in enumerate(assignment):
        # Add their payment when assigned to a certain job (assignment)
        total_payment += costs[person, job]
    return total_payment

def branch_and_bound(assignment, costs, current_payment, remaining_jobs, best_solution):
    if remaining_jobs == 0:
        # Leaf node, calculate actual payment
        current_payment += calculate_total_payment(assignment, costs)
        # Check if current_payment is lower than best_solution
        if current_payment < best_solution[0]:
            # If solution is more optimal that best solution, replace it
            best_solution[0] = current_payment
            # Copy best_solution
            best_solution[1] = assignment.copy()
        return

    # Branch by assigning the next job to a person
    for job in range(costs.shape[1]):
        if job not in assignment:
            new_assignment = assignment.copy()
            new_assignment.append(job)
            new_payment = current_payment + costs[len(assignment), job]

            if new_payment < best_solution[0]:
                branch_and_bound(new_assignment, costs, new_payment, remaining_jobs - 1, best_solution)

def solve_generalized_assignment(costs):
    m, n = costs.shape  # m people, n jobs
    best_solution = [sys.maxsize, []]  # [best_payment, best_assignment]
    branch_and_bound([], costs, 0, n, best_solution)
    return best_solution[1]

for i in range(1,100):
    m = i  # Number of people and jobs
    costs = np.random.randint(1, 100, size=(m, m))  # Random costs for each assignment
    start = time.perf_counter_ns()
    best_assignment = solve_generalized_assignment(costs)
    #print(costs)
    #print("Best assignment:", best_assignment)
    end = time.perf_counter_ns()
    time_elapsed[0, i] = end-start
print(time_elapsed)
