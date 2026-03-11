
def unbounded_knapsack_tickets(days, costs):
    last_day = days[-1]
    day_set = set(days)

    dp = [0] * (last_day + 1)

    for d in range(1, last_day + 1):
        if d not in day_set:
            dp[d] = dp[d - 1]
            continue

        dp[d] = min(
            dp[max(0, d - 1)] + costs[0],   # 1-day pass
            dp[max(0, d - 7)] + costs[1],   # 7-day pass
            dp[max(0, d - 30)] + costs[2]   # 30-day pass
        )

    return dp[last_day]


class Solution:
    def mincostTickets(self, days, costs):
        return unbounded_knapsack_tickets(days, costs)