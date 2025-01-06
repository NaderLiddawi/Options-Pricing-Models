The Python script calculates the price of a European call option using two different methods: the Black-Scholes formula and a multi-period binomial tree model. The Black-Scholes method leverages continuous-time stochastic calculus and outputs a closed-form solution, calculating key intermediary variables d1 and d2 for standard normal cumulative distribution functions. The binomial model, on the other hand, discretizes the option pricing process into N time steps, constructing a lattice of potential asset prices using "up" and "down" factors based on volatility (sigma) and step time (dt), and iteratively calculates the option price backward through the tree. 

Input parameters include stock price (S), strike price (K), time to maturity (T), risk-free interest rate (r), volatility (sigma), and, for the binomial method, the number of periods (N). After computing the option price with both methods, the script compares their results and prints the respective prices and the absolute difference between them, highlighting how closely the binomial model approximates the Black-Scholes formula as N becomes large.


# European Call Option Pricing: Black-Scholes vs. Binomial Tree

This Python script calculates the price of a **European call option** using two methods:
1. **Black-Scholes Formula** (closed-form solution)
2. **Binomial Tree Model** (numerical approximation)

---

## **Black-Scholes Formula**
The **Black-Scholes formula** provides a closed-form solution for European call options. It calculates the price based on the following intermediary variables:

$$
d_1 = \frac{\ln\left(\frac{S}{K}\right) + \left(r + \frac{1}{2}\sigma^2\right)T}{\sigma \sqrt{T}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T}
$$

The price of the call option (\( C \)) is given by:

$$
C = S \cdot N(d_1) - K \cdot e^{-rT} \cdot N(d_2)
$$

Where:
- $$\( N(d) \)$$ is the cumulative distribution function (CDF) of the standard normal distribution.

### **Advantages:**
- Analytical and computationally efficient.
- Useful for European options with constant volatility and interest rates.

---

## **Binomial Tree Model**
The **binomial tree model** discretizes the option pricing process into $$\( N \)$$ time steps. It models possible future stock prices at each step using "up" and "down" movements.

### **Key Calculations:**
1. **Time Step Size**:

$$ \Delta t = \frac{T}{N} $$

2. **Up and Down Factors**:

$$ u = e^{\sigma \sqrt{\Delta t}}, \quad d = \frac{1}{u} $$

3. **Risk-Neutral Probability**:

$$ p = \frac{e^{r \Delta t} - d}{u - d} $$

4. **Option Payoff at Maturity**:

  At maturity $$(\( t = T \))$$, calculate the option payoff for all possible stock prices:
  
$$ \text{Payoff} = \max(S_T - K, 0) $$


5. **Backward Induction**:

Work backward through the tree to compute the option value at each node:

$$ C = e^{-r \Delta t} \left( p \cdot C_{\text{up}} + (1 - p) \cdot C_{\text{down}} \right) $$

---

## **Inputs and Outputs**
### **Parameters:**
- $$\( S \)$$: Current stock price.
- $$\( K \)$$: Strike price.
- $$\( T \)$$: Time to maturity (in years).
- $$\( r \)$$: Risk-free interest rate.
- $$\( \sigma \)$$: Volatility of the stock.
- $$\( N \)$$: Number of time steps for the binomial model.

### **Outputs:**
- **Black-Scholes Call Option Price**
- **Binomial Model Call Option Price**
- **Difference**: Absolute difference between the two prices.

---

## **Example Results**
Using the following inputs:
- $$\( S = 125 \)$$, $$\( K = 100 \)$$, $$\( T = 1 \)$$, $$\( r = 0.05 \)$$, $$\( \sigma = 0.32 \)$$, $$\( N = 10000 \)$$

The output is:
- **Black-Scholes Price**: $$\( 36.0047 \)$$
- **Binomial Tree Price**: $$\( 36.0050 \)$$
- **Difference**: $$\( 0.0003 \)$$

---

## **Key Takeaways**
1. The **Black-Scholes formula** provides a precise closed-form solution for European options.
2. The **binomial model** converges to the Black-Scholes price as $$\( N \)$$ (number of steps) increases.
3. **Impact of Parameters**:
   - Higher volatility $$(\( \sigma \))$$ and longer time to maturity $$(\( T \))$$ typically increase option prices.
   - The risk-free rate $$(\( r \))$$ affects the discounting of the strike price, influencing the option value.

---

## **Usage**
This script demonstrates how the binomial model approximates the Black-Scholes price and highlights their alignment for European options.
