import numpy as np
import sys

def calculate_total_payment(assignment, costs):
    total_payment = 0
    for person, job in enumerate(assignment):
        total_payment += costs[person, job]
    return total_payment

def branch_and_bound(assignment, costs, current_payment, remaining_jobs, best_solution):
    if remaining_jobs == 0:
        # Leaf node, calculate actual payment
        current_payment += calculate_total_payment(assignment, costs)
        if current_payment < best_solution[0]:
            best_solution[0] = current_payment
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

# Example usage:
m = 3  # Number of people
n = 3  # Number of jobs
costs = np.random.randint(1, 100, size=(m, n))  # Random costs for each assignment

best_assignment = solve_generalized_assignment(costs)
print("Best assignment:", best_assignment)
