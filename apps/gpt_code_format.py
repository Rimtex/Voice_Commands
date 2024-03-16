"""
```python
"""

import matplotlib.pyplot as plt
import yfinance as yf

# Получение данных о ценах на биткоин
btc_data = yf.download('BTC-USD', '2021-01-01', '2023-03-08')

# Извлечение цен закрытия
prices = btc_data['Close']

# Создание графика
plt.plot(prices)
plt.xlabel('Дата')
plt.ylabel('Цена (USD)')
plt.title('График цен на биткоин')

# Отображение графика
plt.show()


"""
```
"""