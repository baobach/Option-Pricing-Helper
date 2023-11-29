import numpy as np
from numba import njit

class AsianOptionPricer:
    """
    AsianOptionPricer: Computes the price of an Asian option using Monte Carlo simulation.

    Parameters:
    S0 : float
        Initial asset price.
    strike : float
        Strike price of the option.
    risk_free_rate : float
        Risk-free interest rate.
    volatility : float
        Volatility of the underlying asset.
    maturity : float
        Time to maturity in years.
    num_steps : int
        Number of steps in the simulation.
    num_simulations : int
        Number of simulations to run.
    option_type : str, optional
        Type of option ('C' for Call option, 'P' for Put option). Default is 'C'.
    """

    def __init__(self, S0, strike, risk_free_rate, volatility, maturity, num_steps, num_simulations, option_type='C'):
        self.S0 = S0
        self.strike = strike
        self.risk_free_rate = risk_free_rate
        self.volatility = volatility
        self.maturity = maturity
        self.num_steps = num_steps
        self.num_simulations = num_simulations
        self.option_type = option_type

    @staticmethod
    @njit
    def _simulate_asset_price(S0, risk_free_rate, volatility, maturity, num_steps, num_simulations):
        dt = maturity / num_steps
        S = np.empty((num_steps + 1, num_simulations))
        S[0] = S0

        for i in range(num_steps):
            z = np.random.standard_normal(num_simulations)
            S[i + 1] = S[i] * np.exp((risk_free_rate - 0.5 * volatility ** 2) * dt +
                                      volatility * np.sqrt(dt) * z)

        return S

    def calculate_price(self):
        S = self._simulate_asset_price(self.S0, self.risk_free_rate, self.volatility,
                                       self.maturity, self.num_steps, self.num_simulations)

        avg_price = np.mean(S[1:], axis=0)

        if self.option_type == 'C':
            payoff = np.maximum(avg_price - self.strike, 0)
        else:
            payoff = np.maximum(self.strike - avg_price, 0)

        discount_factor = np.exp(-self.risk_free_rate * self.maturity)
        option_value = discount_factor * np.mean(payoff)

        return option_value
    
class LookbackOptionPricer:
    """
    LookbackOptionPricer: Computes the price of a Lookback option using Monte Carlo simulation.

    Parameters:
    S0 : float
        Initial asset price.
    strike : float
        Strike price of the option.
    risk_free_rate : float
        Risk-free interest rate.
    volatility : float
        Volatility of the underlying asset.
    maturity : float
        Time to maturity in years.
    num_steps : int
        Number of steps in the simulation.
    num_simulations : int
        Number of simulations to run.
    option_type : str, optional
        Type of option ('C' for Call option, 'P' for Put option). Default is 'C'.
    """

    def __init__(self, S0, strike, risk_free_rate, volatility, maturity, num_steps, num_simulations, option_type='C'):
        self.S0 = S0
        self.strike = strike
        self.risk_free_rate = risk_free_rate
        self.volatility = volatility
        self.maturity = maturity
        self.num_steps = num_steps
        self.num_simulations = num_simulations
        self.option_type = option_type

    @staticmethod
    @njit
    def _simulate_asset_price(S0, risk_free_rate, volatility, maturity, num_steps, num_simulations):
        dt = maturity / num_steps
        S = np.empty((num_steps + 1, num_simulations))
        S[0] = S0

        for i in range(num_steps):
            z = np.random.standard_normal(num_simulations)
            S[i + 1] = S[i] * np.exp((risk_free_rate - 0.5 * volatility ** 2) * dt +
                                      volatility * np.sqrt(dt) * z)

        return S

    def calculate_price(self):
        if self.option_type not in ["C", "P"]:
            raise ValueError("Wrong Option Type. Use 'C' for Call option and 'P' for Put option.")

        S = self._simulate_asset_price(self.S0, self.risk_free_rate, self.volatility,
                                       self.maturity, self.num_steps, self.num_simulations)

        M_max = np.max(S, axis=0)
        M_min = np.min(S, axis=0)

        if self.option_type == "C":
            option_value = np.exp(-self.risk_free_rate * self.maturity) * np.mean(np.maximum(M_max - self.strike, 0))
        elif self.option_type == "P":
            option_value = np.exp(-self.risk_free_rate * self.maturity) * np.mean(np.maximum(self.strike - M_min, 0))

        return option_value


