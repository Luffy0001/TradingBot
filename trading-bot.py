# import time
# import pandas as pd
# from binance.enums import KLINE_INTERVAL_1HOUR
# from binance.client import Client
# from dotenv import load_dotenv
# import os

# # Load variables from .env file
# load_dotenv()

# # Access the variables using os.getenv()
# api_key = os.getenv("API_KEY")
# secret_api = os.getenv("SECRET_API")

# # Function to get continuous price data
# def get_continuous_price_data(client, symbol, interval=KLINE_INTERVAL_1HOUR, limit=100):
#     klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)

#     columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume',
#                'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore']

#     data = pd.DataFrame(klines, columns=columns)
#     data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

#     return data

# # Function to simulate trades
# def simulate_trades(client, symbol, virtual_balance):
#     data = get_continuous_price_data(client, symbol)
#     current_price = float(data.iloc[-1]['close'])
#     previous_hour_high = float(data.iloc[-2]['high'])

#     if current_price > previous_hour_high:
#         print(f"Condition met! Current price ({current_price}) is higher than the previous hour's high ({previous_hour_high}). Simulating a buy action.")
#         # Simulate a buy order
#         # Update virtual balance (for demonstration purposes)
#         virtual_balance['USDT'] -= 100  # Deduct 100 USDT for a buy simulation
#         virtual_balance['BTC'] += 0.001  # Simulate buying 0.001 BTC
#         action = "Buy"
#     else:
#         print(f"Condition not met. Current price ({current_price}) is lower than the previous hour's high ({previous_hour_high}). Simulating a sell action.")
#         # Simulate a sell order
#         # Update virtual balance (for demonstration purposes)
#         virtual_balance['USDT'] += 100  # Add 100 USDT for a sell simulation
#         virtual_balance['BTC'] -= 0.001  # Simulate selling 0.001 BTC
#         action = "Sell"

#     return virtual_balance, action

# # Create Binance client
# client = Client(api_key, secret_api)

# symbol = 'BTCUSDT'

# # Initial virtual balance (for demonstration purposes)
# virtual_balance = {'USDT': 10000, 'BTC': 5}  # Starting with 10000 USDT and 5 BTC

# # Simulate trades continuously for 4 hours
# simulation_duration = 4 * 60 * 60  # 4 hours in seconds
# start_time = time.time()
# while time.time() - start_time < simulation_duration:
#     print("\nSimulating a single trade...")
#     virtual_balance, action = simulate_trades(client, symbol, virtual_balance)
#     print("Virtual Balance after trade:", virtual_balance)
#     print(f"Waiting for 1 hour...")
#     time.sleep(3600)  # Delay for 1 hour (3600 seconds)

# # Calculate and display profit/loss from initial balance after 4 hours
# initial_value = 10000  # Replace this with the initial value of USDT before the trades started
# current_value = virtual_balance['USDT']
# profit_loss = current_value - initial_value

# if profit_loss > 0:
#     print(f"\nProfit after 4 hours: {profit_loss} USDT")
# elif profit_loss < 0:
#     print(f"\nLoss after 4 hours: {abs(profit_loss)} USDT")
# else:
#     print("\nNo profit or loss after 4 hours")


import time
import random

# Function to simulate market price changes
def simulate_market(initial_price, duration):
    prices = [initial_price]
    for _ in range(duration // 10):  # Simulate market changes every 10 seconds
        random_change = random.uniform(-50, 50)  # Simulate price changes between -50 and +50
        new_price = prices[-1] + random_change
        prices.append(new_price)
        time.sleep(10)  # Simulate 10 seconds wait

    return prices

# Simulate market price changes for 10 minutes
initial_price = 5000  # Initial price
duration = 10 * 60  # 10 minutes in seconds
print(f"Initial price: {initial_price}")
market_prices = simulate_market(initial_price, duration)
final_price = market_prices[-1]
print(f"Final price: {final_price}")

# Calculate and display profit or loss
initial_value = 10000  # Replace with the initial value of USDT before market changes
final_value = initial_value * (final_price / initial_price)
profit_loss = final_value - initial_value

if profit_loss > 0:
    print(f"\nProfit after market changes: {profit_loss:.2f} USDT")
elif profit_loss < 0:
    print(f"\nLoss after market changes: {abs(profit_loss):.2f} USDT")
else:
    print("\nNo profit or loss after market changes")
