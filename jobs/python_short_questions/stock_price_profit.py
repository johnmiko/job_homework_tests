def solution(prices):
    # Type your solution here
    # The most money we can make is buy at min, sell at max
    # Increment through list because we have to buy first    
    # May make sense to divide and conquer
    a = 2
    if not prices:
        return 0
    profit = prices[-1] - prices[0]
    # Lets see if best possible price is available, if not, then we need to cut things up
    # Buy at lowest if possible
    min_price = min(prices)
    min_index = prices.index(min_price)
    # Find last occurence of max price    
    max_price = max(prices)
    max_index = len(prices) - 1 - prices[::-1].index(max_price)
    if min_index < max_index:
        return max_price - min_price
    else:
        max_profit_val = 0
        current_max_val = 0
        for price in reversed(prices):
            current_max_val = max(current_max_val, price)
            potential_profit = current_max_val - price
            max_profit_val = max(potential_profit, max_profit_val)

        return max_profit_val


prices = [0, 1, 2]
profit = solution(prices)
print(profit)
print(profit == 2)

prices = [0, 1, 2, -1]
profit = solution(prices)
print(profit)
print(profit == 2)
