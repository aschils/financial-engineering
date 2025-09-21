r"""
                           11.72%
                          /
                 9.38% ---
                /         \
       7.5% ---             8.44%
      /      \
6.0%           6.75% --- 6.08%
  \          /
   5.4% ---
             \
               4.86% --- 4.37%

"""


from framework.binomial_model.forward_equations import *


if __name__ == "__main__":


    # Compute the Arrow-Debreu security, paying 1 dollar at time 3 and state 2

    n=3
    interest_rates = np.zeros((n+1,n+1))
    interest_rates[0,0] = 0.06
    interest_rates[1,[0,1]] = [0.054,0.075]
    interest_rates[2,[0,1,2]] = [0.0486,0.0675,0.0938]
    interest_rates[3:] = [0.0437,0.0608,0.0844,0.01172]


    elem_prices = elementary_prices_lattice(n, interest_rates)
    print(elem_prices)
    print(f"answer {elem_prices[3,2]}")

    """
    Consider a  forward-start swap, starting at time t=1 and ending at time t=3

    Notional principal is 100,000.

    Fixed rate of swap is 7%

    Payments at t=i=2,3 are based as usual on fixed rate minus floating rate that
    prevail at t=i−1

    What is the value of the swap at t=0t=0
    """

    principal = 10**5
    r = 0.07
    rates_diff =  r-interest_rates

    value = rates_diff[1]*elem_prices[1]/(1+interest_rates[1])
    value += rates_diff[2]*elem_prices[2]/(1+interest_rates[2])

    print(f"answer {np.sum(value)*principal}")
