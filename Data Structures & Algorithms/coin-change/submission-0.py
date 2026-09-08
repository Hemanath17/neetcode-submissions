class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def solve(remain_amount):
            if remain_amount ==0:
                return 0
            if remain_amount<0:
                return -1
            if remain_amount in memo:
                return memo[remain_amount]
            fewest_coins = float('inf')
            for coin in coins:
                result = solve(remain_amount-coin)
                if result !=-1:
                    fewest_coins = min(fewest_coins, result+1)
            if fewest_coins == float('inf'):
                ans = -1
            else:
                ans = fewest_coins
                
            memo[remain_amount] = ans
            return ans
        return solve(amount)
