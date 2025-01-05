import numpy as np
import scipy.stats as si


# Black-Scholes Formula Function
def black_scholes_call(S, K, T, r, sigma):
    """
    Calculate the price of a European call option using the Black-Scholes formula.

    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity in years
    r: Risk-free interest rate
    sigma: Volatility of the stock

    Returns:
    float: European call option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S * si.norm.cdf(d1) - K * np.exp(-r * T) * si.norm.cdf(d2)
    return call_price


# Binomial Tree for Call Option Pricing
def binomial_call(S, K, T, r, sigma, N):
    """
    Calculate the price of a European call option using a binomial tree model.

    Parameters:
    S: Current stock price
    K: Strike price
    T: Time to maturity in years
    r: Risk-free interest rate
    sigma: Volatility of the stock
    N: Number of periods

    Returns:
    float: European call option price
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Initialize asset prices at maturity
    call_values = np.maximum(S * u ** np.arange(N, -1, -1) * d ** np.arange(0, N + 1) - K, 0)

    # Backward iteration through the tree
    for i in range(N - 1, -1, -1):
        call_values = np.exp(-r * dt) * (p * call_values[1:i + 2] + (1 - p) * call_values[0:i + 1])

    return call_values[0]


# Adjust the Parameters to See how the difference in price between the Black-Scholes and Binomial Model changes

S = 125  # Current stock price
K = 100  # Strike price
T = 1  # Time to maturity in years
r = 0.05  # Risk-free interest rate (seems to have big effect on price)
sigma = 0.32  # Volatility of the stock   (seems to have big effect on price)
N = 10000  # Number of steps for binomial model

# Calculate Call Option Prices
bs_call_price = black_scholes_call(S, K, T, r, sigma)
binomial_call_price = binomial_call(S, K, T, r, sigma, N)

# Print Results
print("Black-Scholes Call Option Price: {:.4f}".format(bs_call_price))
print("Binomial Model Call Option Price with N={} steps: {:.4f}".format(N, binomial_call_price))

# Comparison
difference = abs(bs_call_price - binomial_call_price)
print("Difference between Black-Scholes and Binomial Model: {:.4f}".format(difference))
