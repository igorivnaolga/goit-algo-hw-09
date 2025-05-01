# goit-algo-hw-09

You are given a set of coins [50, 25, 10, 5, 2, 1]. Imagine you're developing a system for a cash register that must determine the optimal way to give change to a customer.

You need to write two functions for the cash register system that distributes change:

## Greedy Algorithm Function find_coins_greedy

This function should take the amount to be given as change and return a dictionary with the quantity of each coin denomination used to make up that amount.
For example, for the amount 113, it should return the dictionary {50: 2, 10: 1, 2: 1, 1: 1}.
The algorithm should be greedy, meaning it selects the largest available coin denominations first.

## Dynamic Programming Function find_min_coins

This function should also take the amount to be given as change, but should use dynamic programming to find the minimum number of coins required to make up that amount.
The function should return a dictionary with coin denominations and their counts to reach the target amount in the most efficient way.
For example, for the amount 113, it should return {1: 1, 2: 1, 10: 1, 50: 2}.

## Compare the Efficiency

Compare the efficiency of the greedy algorithm and the dynamic programming algorithm, based on their runtime (e.g., Big O notation) and performance for large sums.
Highlight how they perform on large amounts and explain why one algorithm may be more effective than the other in certain situations.
Include your conclusions in the readme.md file of the assignment.
