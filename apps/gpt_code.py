import matplotlib.pyplot as plt
import requests

# Получаем исторические данные о курсе биткоина
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
response = requests.get(url)
data = response.json()
prices = data['bpi']

# Извлекаем даты и цены
dates = list(prices.keys())
values = list(prices.values())

# Строим график
plt.figure(figsize=(12, 6))
plt.plot(dates, values, color='orange', marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price (USD)')
plt.title('Bitcoin Price Chart')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Отображаем график
plt.show()
