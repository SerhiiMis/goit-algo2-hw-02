from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def dfs(n):
        if n == 0:
            return 0, []
        if n in memo:
            return memo[n]

        max_profit = float('-inf')
        best_cut = []
        for i in range(1, n + 1):
            profit, cuts = dfs(n - i)
            profit += prices[i - 1]
            if profit > max_profit:
                max_profit = profit
                best_cut = cuts + [i]

        memo[n] = (max_profit, best_cut)
        return memo[n]

    max_profit, cuts = dfs(length)
    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts_choice = [[] for _ in range(length + 1)]

    for i in range(1, length + 1):
        for j in range(1, i + 1):
            if dp[i] < dp[i - j] + prices[j - 1]:
                dp[i] = dp[i - j] + prices[j - 1]
                cuts_choice[i] = cuts_choice[i - j] + [j]

    return {
        "max_profit": dp[length],
        "cuts": cuts_choice[length],
        "number_of_cuts": len(cuts_choice[length]) - 1
    }

def run_tests():
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Base case"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "No cut best"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Equal cuts"
        }
    ]

    for test in test_cases:
        print(f"\nTest: {test['name']}")
        print(f"Rod Length: {test['length']}")
        print(f"Prices: {test['prices']}")

        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nMemoization Result:")
        print(f"Max Profit: {memo_result['max_profit']}")
        print(f"Cuts: {memo_result['cuts']}")
        print(f"Number of Cuts: {memo_result['number_of_cuts']}")

        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nTabulation Result:")
        print(f"Max Profit: {table_result['max_profit']}")
        print(f"Cuts: {table_result['cuts']}")
        print(f"Number of Cuts: {table_result['number_of_cuts']}")

        print("\nTest passed successfully!")

if __name__ == "__main__":
    run_tests()
