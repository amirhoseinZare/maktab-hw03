# %%
import pandas as pd
import numpy as np

# %%
cities = np.array(["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Ahvaz"])
days = np.tile(np.arange(1, 31), len(cities))       # [1,2,...,30,1,2,...,30,...]
city_data = np.repeat(cities, 30)                   # ['Tehran','Tehran',...,'Ahvaz']
temperature = np.random.randint(15, 41, size=len(city_data))
humidity = np.random.randint(20, 81, size=len(city_data))
rainfall = np.random.randint(0, 51, size=len(city_data))
data = pd.DataFrame({
    "city": city_data,
    "day": days,
    "temperature": temperature,
    "humidity": humidity,
    "rainfall": rainfall
})

data


# %%
mean_stats = data.groupby('city')[['temperature', 'humidity', 'rainfall']].mean()
hottest_city = mean_stats["temperature"].idxmax()
coldest_city = mean_stats["temperature"].idxmin()
rainy_days = data[data["rainfall"] > 10].groupby('city')[['temperature']].count()
# rainy_days = data[data["rainfall"] > 10].groupby('city')[['temperature']].count().sort_values('temperature', ascending=False)

print('Mean stats of cities', mean_stats)
print('Hottest city', hottest_city)
print('Hottest citiy', coldest_city)
print('Rainy Days', rainy_days)

# %%
import matplotlib.pyplot as plt

isfahan_data = data[data['city'] == "Isfahan"]
# isfahan_temperatures = data[data['city'] == "Isfahan"]['temperature']
# print(isfahan_humidity)

plt.plot(isfahan_data['temperature'], isfahan_data['humidity'], marker='o', linestyle='-', color='b')

plt.title("رابطه دما و رطوبت - اصفهان (30 روز)")
plt.xlabel("دما (°C)")
plt.ylabel("رطوبت (%)")
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


