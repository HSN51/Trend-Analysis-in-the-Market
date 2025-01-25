import os
import time
import yfinance as yf
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt

# Trend Türlerini Belirleme
def identify_trend(data):
    recent_highs = data['High'].tail(10).values
    recent_lows = data['Low'].tail(10).values

    if all(x < y for x, y in zip(recent_lows, recent_lows[1:])) and all(x < y for x, y in zip(recent_highs, recent_highs[1:])):
        return "Bullish Trend (Yükselen Trend)"
    elif all(x > y for x, y in zip(recent_lows, recent_lows[1:])) and all(x > y for x, y in zip(recent_highs, recent_highs[1:])):
        return "Bearish Trend (Düşen Trend)"
    else:
        return "Sideways Trend (Yatay Trend)"

# Destek ve Direnç Hesaplama
def calculate_support_resistance(data):
    support = float(data['Low'].min())  # Float formatı
    resistance = float(data['High'].max())
    return support, resistance

# Hareketli Ortalamalar ve Teknik İndikatörler
def calculate_indicators(data):
    data['MA_20'] = data['Close'].rolling(window=20).mean()
    data['MA_50'] = data['Close'].rolling(window=50).mean()
    data['MA_200'] = data['Close'].rolling(window=200).mean()

    # RSI Hesaplama
    delta = data['Close'].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    data['RSI'] = 100 - (100 / (1 + (avg_gain / avg_loss)))

    # MACD Hesaplama
    short_ema = data['Close'].ewm(span=12, min_periods=1).mean()
    long_ema = data['Close'].ewm(span=26, min_periods=1).mean()
    data['MACD'] = short_ema - long_ema
    data['MACD_signal'] = data['MACD'].ewm(span=9, min_periods=1).mean()
    return data

# TradingView HTML Oluşturma
def create_tradingview_html(symbol, interval, period):
    """
    Create a TradingView HTML file dynamically with the user-specified interval and period.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>TradingView Chart: {symbol} ({period}, {interval.upper()})</title>
        <script src="https://s3.tradingview.com/tv.js"></script>
    </head>
    <body>
        <h2 style="text-align:center;">{symbol} Trend Analysis ({period}, {interval.upper()})</h2>
        <div id="chart" style="width: 800px; height: 500px; margin: auto;"></div>
        <script>
            new TradingView.widget({{
                "container_id": "chart",
                "symbol": "{symbol}",
                "interval": "{interval.upper()}",
                "theme": "light",
                "style": "1",
                "locale": "en",
                "toolbar_bg": "#f1f3f6",
                "enable_publishing": false,
                "allow_symbol_change": true,
                "autosize": true
            }});
        </script>
    </body>
    </html>
    """
    file_path = f"{symbol}_{period}_chart.html"
    with open(file_path, "w") as file:
        file.write(html_content)
    print(f"TradingView HTML created: {file_path}")
    return file_path

# Selenium ile Screenshot
def capture_tradingview_screenshot(html_path):
    """
    Capture a screenshot of the TradingView chart HTML file using Selenium.
    """
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(f"file://{os.path.abspath(html_path)}")
        time.sleep(5)  # Wait for TradingView chart to load fully

        chart_element = driver.find_element("id", "chart")
        screenshot_path = html_path.replace('.html', '_screenshot.png')
        chart_element.screenshot(screenshot_path)

        driver.quit()
        print(f"Screenshot saved as: {screenshot_path}")
        return screenshot_path
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        return None

# Ana Fonksiyon
def main():
    """
    Main function to analyze trends and create TradingView visualization.
    """
    try:
        # Kullanıcıdan giriş al
        ticker = input("Enter the ticker symbol (e.g., AAPL, TSLA, BTC-USD): ").upper()
        period = input("Enter the period (e.g., 1y, 6mo, 3mo): ")
        interval = input("Enter the interval (e.g., 1d, 1h, 15m): ")

        print("Fetching data...")
        data = yf.download(ticker, period=period, interval=interval)

        if data.empty:
            print("No data fetched. Exiting...")
            return

        print("\n--- Data Fetch Complete ---")
        print(f"Showing data for: {ticker} ({period}, {interval})")

        # TradingView HTML ve Screenshot
        print("Creating TradingView chart...")
        html_path = create_tradingview_html(ticker, interval, period)
        print("Capturing TradingView chart screenshot...")
        screenshot_path = capture_tradingview_screenshot(html_path)

        if screenshot_path:
            print(f"Chart successfully saved as: {screenshot_path}")
        else:
            print("Failed to save chart screenshot.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
