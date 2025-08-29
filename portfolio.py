stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 130,
    "MSFT": 300,
    "AMZN": 140
}
portfolio = {}
print("Available stocks:", ", ".join(stock_prices.keys()))
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if stock in portfolio:
        portfolio[stock] += quantity
    else:
        portfolio[stock] = quantity
total_investment = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total_investment += investment
    print(f"{stock} ({qty} shares @ ${price}) = ${investment}")
print("\nTotal Investment Value: $", total_investment)
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Your Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            f.write(f"{stock} ({qty} shares @ ${price}) = ${investment}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio saved to portfolio.txt")