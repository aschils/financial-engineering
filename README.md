
# Financial engineering portfolio

This repository contains code related to mathematical finance, algorithmic trading,... It serves as a portfolio
for applying to quantitative finance positions.

## Options

- compute price of european call option using the multi-period binomial model approximating a Black Scholes 
model: options/european_option_binomial.py

## Fixed income derivatives

term_structure_models/bonds_derivative.py
- use the term structure lattice model to price bond derivatives
- values of zero bond coupon (ZCB)
- forward and future prices of ZCB
- price of american option on ZCB
- Arrow-Debreu security prices: term_structure_models/arrow_debreu_security.py