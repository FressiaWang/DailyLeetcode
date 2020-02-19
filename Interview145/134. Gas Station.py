"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input: 
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: 
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""
def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = rest = overall = 0
        for i in xrange(len(gas)):
            rest += gas[i] - cost[i]
            overall += gas[i] - cost[i]
            if rest < 0:
                rest, start = 0, i + 1
        return start if overall >=0 else -1
"""        
The heuristic is that if sum(gas) >= sum(cost), there must exists a starting station that enable the circular travel.
Suppose our circular route stations are {0,...,n} and sum(gas) >= sum(cost). And we define a function route(l,r) as ∑(l<=i<r) gas[i]-cost[i] The valid starting station s is the leftmost station that we can travel from it to n. So route(s,n) > 0. And we just need to prove route(s,n) + route(0,k) > 0 for any k from {0,...,s-1}.
Since s is the leftmost station that we can travel from it to n, so for any k from {0,...,s-1}, we can not travel from k to n. Or route(k,n) < 0 && route(s,n) > 0 => route(k,s) < 0.
And as sum(gas) >= sum(cost), route(0,k) + route(k,s) + route(s,n) > 0. Considering route(k,s) < 0, we can conclude that route(0,k) + route(s,n) > 0.
So based on this, we just need to find out the leftmost station that we can travel from it to n if sum(gas) >= sum(cost).
"""
def canCompleteCircuit(gas, cost):
	if sum(gas) < sum(cost): return -1
	n, s, r = len(gas), 0, 0
	for i in range(n):
		if gas[i] + r < cost[i]:
			s, r = i+1, 0
		else:
			r += gas[i]-cost[i]
	return s        
