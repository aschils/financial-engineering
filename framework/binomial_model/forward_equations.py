import numpy as np

def elementary_prices_lattice(n: int, interest_rates: np.ndarray):
    l = np.zeros((n+1,n+1))
    l[0,0] = 1
    growth_rates = 1+interest_rates
    for i in range(0,n):
        for j in range(0,i+2):
            if j == 0:
                l[i + 1, j] = 0.5 * l[i,j]/growth_rates[i,j]
            elif j == i+1:
                l[i + 1, j] = 0.5* l[i,i]/growth_rates[i,i]
            else:
                l[i+1,j] = 0.5*(l[i,j-1]/growth_rates[i,j-1] + l[i,j]/growth_rates[i,j])
    return l
