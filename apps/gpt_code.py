"""
Для создания графика биткоина нам потребуется использовать библиотеку matplotlib в Python. Если у вас нет этой библиотеки, вы можете установить ее с помощью pip:

```bash
pip install matplotlib
```

Далее приведен пример кода, который строит график цены биткоина за последний месяц с использованием данных из API CoinGecko:

```python
"""

import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Получаем данные о цене биткоина за последний месяц
url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
params = {
    'vs_currency': 'usd',
    'days': '30',
    'interval': 'daily'
}
response = requests.get(url, params=params)
data = response.json()

prices = [entry[1] for entry in data['prices']]
timestamps = [datetime.utcfromtimestamp(entry[0] / 1000).strftime('%Y-%m-%d') for entry in data['prices']]

# Строим график
plt.figure(figsize=(12, 6))
plt.plot(timestamps, prices, marker='o', color='b')
plt.title('Bitcoin Price Chart for the Last Month')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()


"""
```

Этот код отправляет запрос к API CoinGecko, чтобы получить цену биткоина за последний месяц, затем строит график с использованием библиотеки matplotlib. 
Вы можете запустить этот код в своей среде разработки Python и посмотреть график цены биткоина за последний месяц.
"""