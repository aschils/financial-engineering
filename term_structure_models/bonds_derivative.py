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

import numpy as np

if __name__ == "__main__":

    # 1) what is the value of the zero coupon bond that pays 1 dollar at t=3?
    rates = [[0.02], [0.019, 0.023], [0.018, 0.021, 0.025], [0.015, 0.02, 0.022, 0.026]]
    p = 0.5

    value_lattice = [[0]*i for i in range(1,5)]
    value_lattice[3] = [1]*4 # ZCB pays 1$ at t=3


    for i in range(2, -1, -1):
        for j in range(i+1):
            value_lattice[i][j] = 1/(1+rates[i][j])*(p*value_lattice[i+1][j]+p*value_lattice[i+1][j+1])


    print(f"answer: {value_lattice[0][0]}")

    # 2) Compute the forward price at t=2 of a zero coupon bond with face value 100 and maturity=3
    # = E_2[Z³_2/B_2]/E_2[1/B_2]
    # B_t = (1+r0)...(1+r_(t-1))
    # E_2[1/B_2] = 1 because we are at t=2
    t2_lattice_proba = np.array([0.25, 0.5, 0.25])
    esp_t2 = np.dot(t2_lattice_proba, value_lattice[2])*100
    print(f"answer: {esp_t2}")
