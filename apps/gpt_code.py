import matplotlib.pyplot as plt
import pandas as pd

# Пример данных о ценах биткоина
data = {
    'Дата': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
    'Цена': [30000, 32000, 31000, 33000, 34000]
}

# Создание DataFrame
df = pd.DataFrame(data)
df['Дата'] = pd.to_datetime(df['Дата'])

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(df['Дата'], df['Цена'], marker='o')
plt.title('График цен биткоина')
plt.xlabel('Дата')
plt.ylabel('Цена (USD)')
plt.grid(True)
plt.show()
