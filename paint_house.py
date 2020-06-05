"""
// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : None
// Your code here along with comments explaining your approach
Algorithm explanation
For Recursive solution, we essentially have to copmute minimum cost from the all possible paths
starting from 0,1 and 2nd position in the top row
We compute the minimum of the costs related to color0, color1 and color2, while recursively calling on
next row and distinct columns and passing the updated min_cost to the recursive calls
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #DP solution
        if not costs:
            return 0
        for i in range(len(costs)-2,-1,-1):
            for j in range(len(costs[0])):
                if j == 0:
                    costs[i][j] = min(costs[i][j]+costs[i+1][j+1],
                                     costs[i][j]+costs[i+1][j+2])
                elif j == 1:
                    costs[i][j] = min(costs[i][j]+costs[i+1][j-1],
                                     costs[i][j]+costs[i+1][j+1])
                elif j == 2:
                    costs[i][j] = min(costs[i][j]+costs[i+1][j-2],
                                     costs[i][j]+costs[i+1][j-1])
        return min(costs[0])
        
        
        #Recursive approach
        def rec_cost(i,min_cost,last_color):
            #base case
            if i == len(costs):
                #return the min cost of the current path
                return min_cost
            
            case0,case1,case2 = float("inf"),float("inf"),float("inf")
            if last_color == 0:
                #rec call for 1 and 2, using min cost from previous row
                case0 = min(rec_cost(i+1,min_cost + costs[i][1], 1),
                            rec_cost(i+1,min_cost + costs[i][2], 2))
            elif last_color == 1:
                #rec call for 0 and 2,  using min cost from previous row
                case1 = min(rec_cost(i+1,min_cost + costs[i][0], 0),
                            rec_cost(i+1,min_cost + costs[i][2], 2))
            elif last_color == 2:
                #rec call for 0 and 1,  using min cost from previous row
                case2 = min(rec_cost(i+1,min_cost + costs[i][0], 0),
                            rec_cost(i+1,min_cost + costs[i][1], 1))
                
            return min(case0,case1,case2)
        
        case0 = rec_cost(0,0,0)
        case1 = rec_cost(0,0,1)
        case2 = rec_cost(0,0,2)
        
        return min(case0,case1,case2)