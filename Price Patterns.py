import numpy as np

def detect_support_resistance(data):
    # Implementation omitted for brevity
    support = np.mean(data['Low'])
    resistance = np.mean(data['High'])
    return support, resistance

def plot_support_resistance(data, support, resistance):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Close'], label='Close Price')
    plt.axhline(y=support, color='green', linestyle='--', label='Support')
    plt.axhline(y=resistance, color='red', linestyle='--', label='Resistance')
    plt.title('Support and Resistance Levels')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

# Example usage:
support, resistance = detect_support_resistance(stock_data)
plot_support_resistance(stock_data, support, resistance)
