"""
Для построения графика биткоина я воспользуюсь библиотекой `matplotlib` в Python. Для начала необходимо установить эту библиотеку, если она еще не установлена. Для этого можно использовать следующую команду:

```bash
pip install matplotlib
```

Затем я напишу код, который загрузит исторические данные о курсе биткоина и построит график. Вот пример кода:

```python
"""

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


"""
```

Этот код загружает исторические данные о курсе биткоина с веб-сервиса CoinDesk, извлекает даты и цены, а затем строит график с помощью библиотеки `matplotlib`.

Пожалуйста, убедись, что у тебя установлена библиотека `matplotlib`, и запусти этот код в среде, поддерживающей выполнение Python кода.
"""