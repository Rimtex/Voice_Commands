import matplotlib.pyplot as plt
import pandas as pd

# Пример данных курса биткоина
data = {
    'Дата': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05'],
    'Курс': [27000, 27500, 28000, 27800, 28500]
}

df = pd.DataFrame(data)
df['Дата'] = pd.to_datetime(df['Дата'])

plt.figure(figsize=(10, 5))
plt.plot(df['Дата'], df['Курс'], marker='o', linestyle='-', color='b')
plt.title('Курс биткоина')
plt.xlabel('Дата')
plt.ylabel('Курс (USD)')
plt.grid(True)
plt.show()
