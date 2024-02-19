"""
```python
"""

try:
    import matplotlib.pyplot as plt
    import requests
except:
    import subprocess
    subprocess.call(['pip', 'install', 'matplotlib', 'requests'])

# Получаем данные о цене биткоина с API
url = 'https://api.coindesk.com/v1/bpi/historical/close.json'
response = requests.get(url, params={'start': '2022-01-01', 'end': '2022-12-31'})
data = response.json()

dates = list(data['bpi'].keys())
prices = list(data['bpi'].values())

# Строим график
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, color='orange', marker='o', linestyle='-')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Price Chart for 2022')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()


"""
```
"""
input()