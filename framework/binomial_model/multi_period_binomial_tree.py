
from typing import Callable, List

"""
Compute the asset prices S_t for all t and for all paths possible in the binomial tree

inputs:
- s0: asset price at t=0
- u: increase factor between t and t+1
- n: number of periods
"""
def asset_tree(s0: float, u: float, n: int):
    d = 1.0/u
    asset_t = [[s0*u**j*d**(t-j) for j in range(t+1)] for t in range(n+1)]
    return asset_t

def option_tree(asset_tree: List[List[float]], expiration_price: Callable[[float,float], float], strike_price: float, n: int,
                u: float, interest_rate: float, dividend: float):
    d = 1/u
    option_t = [[0.0 for j in range(t+1)] for t in range(n+1)]
    option_t[-1] = [expiration_price(s, strike_price) for s in asset_tree[-1]]

    q = (interest_rate - d - dividend) / (u - d)
    one_minus_q = 1-q

    for t in range(len(option_t)-2, -1, -1):
        for j in range(t+1):
            option_t[t][j] = (one_minus_q*option_t[t+1][j] + q*option_t[t+1][j+1])/interest_rate
    return option_t

def call_expiration_price(asset_price: float, strike_price: float):
    return max(asset_price-strike_price, 0)

def put_expiration_price(asset_price: float, strike_price: float):
    return max(strike_price-asset_price, 0)

