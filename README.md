# Trend Analysis with TradingView and Technical Indicators

This project enables users to analyze market trends using Yahoo Finance data, calculate technical indicators, and visualize trading charts using TradingView widgets. Additionally, it supports capturing screenshots of the charts using Selenium.

## Features

- **Trend Identification:** Determine market trends as Bullish, Bearish, or Sideways.
- **Support and Resistance Levels:** Automatically calculate key support and resistance levels.
- **Technical Indicators:**
  - Moving Averages (20, 50, 200)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- **TradingView Chart Integration:** Dynamically create HTML files with TradingView widgets.
- **Screenshot Capture:** Automatically take screenshots of TradingView charts using Selenium.

## Requirements

The following Python libraries are required for this project:

- `pandas`
- `yfinance`
- `selenium`
- `matplotlib`
- `webdriver-manager`

Install them using:

```bash
pip install pandas yfinance selenium matplotlib webdriver-manager
```

## File Structure

- `main.py`: The main script to execute the analysis and create charts.
- `README.md`: Documentation for the project.

## Usage

### 1. Run the Script

Execute the script using Python:

```bash
python main.py
```

### 2. Input Parameters

The script will prompt you to input the following parameters:

- **Ticker Symbol:** The stock or cryptocurrency symbol (e.g., `AAPL`, `TSLA`, `BTC-USD`).
- **Period:** The time period for the data (e.g., `1y`, `6mo`, `3mo`).
- **Interval:** The data interval (e.g., `1d`, `1h`, `15m`).

### 3. Output

- **TradingView HTML File:** An HTML file is created with the TradingView chart embedded.
- **Chart Screenshot:** A screenshot of the TradingView chart is saved in the same directory.

### Example

Input:

```bash
Enter the ticker symbol (e.g., AAPL, TSLA, BTC-USD): AAPL
Enter the period (e.g., 1y, 6mo, 3mo): 1y
Enter the interval (e.g., 1d, 1h, 15m): 1d
```

Output:

- `AAPL_1y_chart.html`
- `AAPL_1y_chart_screenshot.png`

## Functions

### `identify_trend(data)`
Determines whether the trend is Bullish, Bearish, or Sideways based on recent highs and lows.

### `calculate_support_resistance(data)`
Calculates support and resistance levels using the minimum and maximum values of the data.

### `calculate_indicators(data)`
Adds the following indicators to the dataset:
- Moving Averages (20, 50, 200)
- RSI
- MACD

### `create_tradingview_html(symbol, interval, period)`
Generates an HTML file with a TradingView widget for the specified symbol, interval, and period.

### `capture_tradingview_screenshot(html_path)`
Uses Selenium to capture a screenshot of the TradingView chart in the HTML file.

## Prerequisites

1. **Selenium WebDriver:** Ensure Google Chrome is installed on your system.
2. **WebDriver Manager:** The script automatically installs and manages the ChromeDriver.

## Error Handling

- If no data is fetched, the script will exit with a message.
- If the TradingView chart cannot be captured, an error message will be displayed.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Happy coding! 🚀
