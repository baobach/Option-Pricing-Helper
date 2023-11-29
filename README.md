# Option Pricing Helper

The Option Pricing Helper is a Python-based repository designed to assist in calculating the prices of various types of financial options. It includes implementations of the Black-Scholes equation for European options and Monte Carlo simulations for exotic options like Asian and Lookback options.

## Project Structure

The repository is organized as follows:

- **`src/`**: Contains Python scripts for option pricing calculations.
  - **`black_scholes.py`**: Implementation of the Black-Scholes equation for European options.
  - **`exotics.py`**: Monte Carlo methods for pricing exotic options.
- **`examples/`**: (Optional) Directory for example usage files.
- **`requirements.txt`**: Lists project dependencies required for running the scripts.

## Implemented Features

### Black-Scholes Equation

The `black_scholes.py` script provides functions to calculate the price of European options using the Black-Scholes model. Users can input the necessary parameters such as stock price, strike price, time to maturity, risk-free interest rate, and volatility to obtain option prices for both call and put options.

### Exotic Options (Monte Carlo)

The `exotics.py` script implements Monte Carlo simulations for pricing exotic options. At present, it includes functions for Asian option pricing using Monte Carlo methods. Additional exotic option pricing methods such as Lookback options can be implemented within this script.

## Usage

Users can utilize these scripts by importing the functions into their Python environment. Examples of usage and sample input data can be found in the `examples/` directory.

### Dependencies

Make sure to install the required dependencies listed in `requirements.txt` using `pip install -r requirements.txt`.

## Contributions

Contributions and enhancements to the existing functionalities are welcome. Feel free to fork this repository, make changes, and submit pull requests.

## Disclaimer

This project provides financial tools and calculations that should be used for educational purposes only. It is not intended for making real-time trading decisions.

## License

The Option Pricing Helper is licensed under the [MIT License](LICENSE).
