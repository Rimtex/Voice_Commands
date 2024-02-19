"""
Для построения графика биткоина я воспользуюсь библиотекой matplotlib для визуализации данных и библиотекой requests для получения данных о цене биткоина с API. 

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

# Получаем данные о цене биткоина с API
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
params = {'start': '2021-01-01', 'end': '2021-12-31'}
response = requests.get(url, params=params)
data = response.json()

# Извлекаем даты и цены биткоина
dates = list(data['bpi'].keys())
prices = list(data['bpi'].values())

# Построение графика
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, color='orange', marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Bitcoin Price (USD)')
plt.title('Bitcoin Price Chart in 2021')
plt.xticks(range(0, len(dates), 30), rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


"""
```

Этот код получит данные о цене биткоина за 2021 год с API и построит график цены биткоина по дням.
"""
input()