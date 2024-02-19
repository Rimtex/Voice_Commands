"""
Для отображения графика биткоина нам понадобится библиотека `matplotlib` для построения графиков и `requests` для получения данных о цене биткоина. Установим эти библиотеки и создадим код для построения графика цены биткоина за последние 30 дней:

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

# Функция для получения цен биткоина за последние 30 дней
def get_bitcoin_prices():
    url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
    params = {'start': '2022-10-01', 'end': '2022-10-30'}
    response = requests.get(url, params=params)
    data = response.json()
    return data['bpi']

# Получаем данные о ценах биткоина
bitcoin_prices = get_bitcoin_prices()

# Разделяем даты и цены для построения графика
dates = list(bitcoin_prices.keys())
prices = list(bitcoin_prices.values())

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(dates, prices, marker='o', color='b', linestyle='-')
plt.title('Bitcoin Price Chart for the Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Отображаем график
plt.show()


"""
```

Этот код отправляет запрос к API Coindesk, чтобы получить цены биткоина за последние 30 дней, затем строит график цены биткоина по этим данным.
"""
input()