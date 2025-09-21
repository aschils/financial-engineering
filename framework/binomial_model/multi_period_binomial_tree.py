"""
Multi-period binomial tree for option pricing
"""


from typing import Callable, List

"""
Compute the asset prices S_t for all t and for all paths possible in the binomial tree

params:
- s0: asset price at t=0
- u: increase factor between t and t+1, d=1/u being the decrease factor
- n: number of periods
returns: multi period binomial tree up to period 'n' for the asset
"""
def build_asset_tree(s0: float, u: float, n: int):
    d = 1.0/u
    asset_tree = [[s0*u**j*d**(t-j) for j in range(t+1)] for t in range(n+1)]
    return asset_tree

"""
params:
- asset_tree: the multi period binomial tree for the asset underlying the option
- expiration_price: a function taking the underlying asset price and the strike price as parameters and returning the
 cash-flow offered by the option at maturity
- strike_price: the strike price of the option
- n: number of periods until option maturity
- u: increase factor between t and t+1, d=1/u being the decrease factor
- interest_rate
- dividend: underlying asset dividend, 0 if no dividend
"""
def build_option_tree(
        asset_tree: List[List[float]],
        expiration_price: Callable[[float, float], float],
        strike_price: float,
        n: int,
        u: float,
        interest_rate: float,
        dividend: float):
    d = 1/u
    option_tree = [[0.0 for j in range(t+1)] for t in range(n+1)]
    option_tree[-1] = [expiration_price(s, strike_price) for s in asset_tree[-1]]

    q = (interest_rate - d - dividend) / (u - d)
    one_minus_q = 1-q

    for t in range(len(option_tree)-2, -1, -1):
        for j in range(t+1):
            option_tree[t][j] = (one_minus_q*option_tree[t+1][j] + q*option_tree[t+1][j+1])/interest_rate
    return option_tree

def call_expiration_price(asset_price: float, strike_price: float):
    return max(asset_price-strike_price, 0)

def put_expiration_price(asset_price: float, strike_price: float):
    return max(strike_price-asset_price, 0)

