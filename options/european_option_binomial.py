"""
Compute price of a european call option using the multi-period binomial model approximating a Black Scholes model.
Parameters of the binomial model are derived from provided parameters of a Black-Scholes model.
"""

import math

from framework.binomial_model import multi_period_binomial_tree as m

if __name__ == "__main__":

    n = 15
    K = 110
    r_bs = 0.02
    c_bs = 0.01
    sigma_bs = 0.3
    T = 0.25*10/15
    s0 = 100
    R = math.exp(r_bs*T/n)
    c = R-math.exp((r_bs-c_bs)*T/n)
    u = math.exp(sigma_bs*math.sqrt(T/n))

    asset_t = m.build_asset_tree(s0, u, n)
    option_t = m.build_option_tree(asset_t, m.call_expiration_price, K, n, u, R, c)
    for i, level in enumerate(option_t):
        print(f"Step {i}: {level}")
