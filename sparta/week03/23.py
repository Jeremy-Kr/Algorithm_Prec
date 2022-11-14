shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    sorted_prices = sorted(prices,reverse=True)
    sorted_coupons = sorted(coupons,reverse=True)
    discounted_price = 0
    price_idx = 0
    coupons_idx = 0
    while price_idx < len(prices) and coupons_idx < len(coupons):
        discounted_price += sorted_prices[price_idx] * (100-sorted_coupons[coupons_idx]) / 100
        price_idx += 1
        coupons_idx += 1
    while price_idx < len(prices):
        discounted_price += sorted_prices[price_idx]
        price_idx += 1
    return discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))