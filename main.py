import time
import random
import math

# Cost of placing server at median 
# establishing Base Case
def placeOneServer(trafficWeights, i, j):
    totalWeight = 0
    for x in range(i, j+1):
        totalWeight += trafficWeights[x-1]
  
    half_sum = totalWeight // 2
    server_pos = i
  
    accumulatedWeight = 0
    for x in range(i, j+1):
        accumulatedWeight += trafficWeights[x-1]
        if accumulatedWeight >= half_sum:
            server_pos = x
            break 

    return sum(trafficWeights[x-1] * abs(server_pos-x) for x in range(i, j+1))
      


def findOptimalServerPositions(trafficWeights, clients, k):

    # create a dynamic table of size (n x n x k)
    dp = [[[float("inf") for _ in range(k+1)] for _ in range(clients+1)] for _ in range(clients+1)]

    # Bottom up DP 
    # Initialize dp table
    for i in range(clients+1):
        for j in range(clients+1):
            dp[i][i][1] = 0         # initialize to 0 as total cost with one server and one client will be 0
            dp[i][j][0] = float("inf")  # initialize to infinity as total cost with no servers will be 0
            
    start = time.perf_counter_ns()
    # Fill dp table   
    for m in range(1, k+1):
        for i in range(1, clients+1):
            for j in range(i, clients+1):
                for x in range(i, j-1):
                    c = dp[i][x][m-1] + placeOneServer(trafficWeights,x+1, j)
                    dp[i][j][m] = min(dp[i][j][m], c) # Update dp table

    end = time.perf_counter_ns()
    time_ = end-start 
    # Minimum cost
    # print(dp[1][clients][k])
    return time_,dp[1][clients][k]


# driver code
if __name__ == "__main__":
    
    # n = 30
    # trafficWeights = [34,47,45,20,11,24,37,30,81,73,99,30,21,52,51,41,60,63,96,67,69,5,92,66,44,47,99,21,47,56]
    #                 # [75, 70, 25, 42, 53, 3]
    #                 # [1,4,2,3,7,5]
    #                 # [10, 90, 50, 100, 207, 90, 46, 70]

    # k = 10
    k = 4
    inc = 0.5
    counter = 0.25
    for n in range (10,50):
        w = [random.randint(1,100) for _ in range(0,n)]
        # Start time (in ns) of when the function to implement runs.
        

        time_, optimalPositions = findOptimalServerPositions(w, n, math.floor(k))

        # End time (in ns) of when the function to implement runs.
        
        print(n,"\t\t\t",math.floor(k),"\t\t\t",time_)
        k = k + 0.3

