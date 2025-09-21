r"""
Use the term structure lattice model (from t=0 to t=3) below to price the bond derivatives in the following questions.

                     2.6%
                    /
           2.5% ---
          /          \
   2.3% -             2.2%
  /      \
2.0%       2.1% --- 2.0%
  \        /
   1.9% -
          \
           1.8% --- 1.5%

proba of up move: 0.5


"""

from framework.binomial_model.multi_period_binomial_tree import *

import numpy as np


def risk_neutral_pricing(n, q1, q2, rates, maturity_values):
    value_lattice = [[0]*i for i in range(1,n+2)]
    value_lattice[-1] = maturity_values

    for i in range(n-1, -1, -1):
        for j in range(i+1):
            value_lattice[i][j] = 1/(1+rates[i][j])*(q1*value_lattice[i+1][j]+q2*value_lattice[i+1][j+1])

    return value_lattice

if __name__ == "__main__":

    # 1) what is the value of the zero coupon bond that pays 1 dollar at t=3?
    rates = [[0.02], [0.019, 0.023], [0.018, 0.021, 0.025], [0.015, 0.02, 0.022, 0.026]]
    p = 0.5

    n = 3
    value_lattice = risk_neutral_pricing(3, p, p, rates, [1]*(n+1)) # ZCB pays 1$ at t=3
    print(f"answer: {value_lattice[0][0]}")

    # 2) Compute the forward price at t=2 of a zero coupon bond with face value 100 and maturity=3
    # = E_2[Z³_2/B_2]/E_2[1/B_2]
    # B_t = (1+r0)...(1+r_(t-1))
    # E_2[1/B_2] = 1 because we are at t=2
    t2_lattice_proba = np.array([0.25, 0.5, 0.25])
    esp_t2 = np.dot(t2_lattice_proba, value_lattice[2])*100
    print(f"answer: {esp_t2}")

    """
    please start by building an n=10-period binomial model for the short-rate.
    The lattice parameters are: r0,0=5%, u=1.1, d=0.9 and q=1−q=1/2.
    """
    r0 = 0.05
    u=1.1
    n=10
    d=0.9
    q1 = q2 = 0.5
    F = 100
    short_rate_lattice = build_asset_tree(0.05, u, n, d)
    zcb_pricing = risk_neutral_pricing(n, q1, q2, short_rate_lattice, [F]*(n+1))
    print(f"answer {zcb_pricing[0][0]}")

    """
    Compute the price of a forward contract on the same ZCB of the previous question where the forward contract matures
    at time t=4. 
    """

    esp_inv_B4 = risk_neutral_pricing(4, q1, q2, short_rate_lattice, [1]*(n+1))[0][0]
    print(f"answer {zcb_pricing[0][0]/esp_inv_B4}")

    # Compute the initial price of a futures contract on the same ZCB of the previous two questions.
    # The futures contract has an expiration of t=4.
    # First compute the possible values for Z^10_4. Then go back in the lattice but without discounting with the interest rate


    future_lattice = risk_neutral_pricing(4, q1, q2, np.zeros((n,n)), zcb_pricing[4])
    print(f"answer {future_lattice[0][0]}")

    # Compute the price of an American call option on the same ZCB of the previous three questions. The option has
    # expiration t=6 and strike=80.

    K = 80
    maturity_values = np.maximum(0, np.array(zcb_pricing[6])-K)
    option_lattice = risk_neutral_pricing(6, q1, q2, short_rate_lattice, maturity_values)

    print(f"answer {option_lattice[0][0]}")

