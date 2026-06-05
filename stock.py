# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 135
}

total_investment = 0

# Number of different stocks
n = int(input("Enter the number of stocks you own: "))

for i in range(n):
    stock_name = input("\nEnter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Investment in {stock_name}: ${investment}")
    else:
        print(f"{stock_name} is not available in the price list.")

print("\n----- Portfolio Summary -----")
print(f"Total Investment Value: ${total_investment}")

# Optional: Save result to a text file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}\n")

    print("Portfolio summary saved to 'portfolio_summary.txt'")