"""
Для отображения графика биткоина мы можем использовать библиотеку `matplotlib` вместе с библиотекой `requests` для получения данных о цене биткоина. Давайте создадим программу, которая получает данные о цене биткоина за последние 30 дней и строит график.

```python
"""

try:
    import matplotlib.pyplot as plt
    import requests
except ImportError:
    import subprocess
    subprocess.call(['pip', 'install', 'matplotlib', 'requests'])
    import matplotlib.pyplot as plt
    import requests

# Получаем данные о цене биткоина за последние 30 дней
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
params = {
    'currency': 'USD',
    'start': '2021-12-01',
    'end': '2021-12-31'
}
response = requests.get(url, params=params)
data = response.json()

# Извлекаем даты и цены для построения графика
dates = list(data['bpi'].keys())
prices = list(data['bpi'].values())

# Строим график цены биткоина
plt.figure(figsize=(10, 6))
plt.plot(dates, prices, color='orange', marker='o', linestyle='-')
plt.title('Bitcoin Price in December 2021')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


"""
```

Этот код отправляет запрос к API CoinDesk для получения цены биткоина за декабрь 2021 года и строит график цены биткоина за этот период.
"""
input()