import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Получаем данные о цене биткоина за последние 30 дней
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {
    'vs_currency': 'usd',
    'days': '30',
    'interval': 'daily'
}
response = requests.get(url, params=params)
data = response.json()

prices = [point[1] for point in data['prices']]
timestamps = [datetime.utcfromtimestamp(point[0]//1000).strftime('%Y-%m-%d') for point in data['prices']]

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(timestamps, prices, marker='o', color='b', linestyle='-')
plt.title('Bitcoin Price Chart for the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
