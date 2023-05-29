class Solution:
    def maxCoins(self, piles: List[int]) -> int:
         # Sort the piles in descending order
        piles.sort(reverse=True)  
        # Calculate the number of iterations

        n = len(piles) // 3  

        coins = 0
        for i in range(n):
            # Pick the second-largest pile in each iteration
            coins += piles[2 * i + 1]  
        return coins
