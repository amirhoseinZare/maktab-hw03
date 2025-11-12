import numpy as np
import pandas as pd

# --- بخش 1: تولید داده با NumPy ---

cities = np.array(["Tehran", "Mashhad", "Isfahan", "Tabriz", "Shiraz", "Ahvaz"])

# برای هر شهر 30 روز (در مجموع 180 ردیف)
days = np.tile(np.arange(1, 31), len(cities))       # [1,2,...,30,1,2,...,30,...]
city_data = np.repeat(cities, 30)                   # ['Tehran','Tehran',...,'Ahvaz']

# تولید داده‌های تصادفی برای هر ردیف
temperature = np.random.randint(15, 41, size=len(city_data))
humidity = np.random.randint(20, 81, size=len(city_data))
rainfall = np.random.randint(0, 51, size=len(city_data))

# --- بخش 2: ساخت DataFrame با Pandas ---
data = pd.DataFrame({
    "City": city_data,
    "Day": days,
    "Temperature": temperature,
    "Humidity": humidity,
    "Rainfall": rainfall
})

print("📊 چند ردیف اول داده:")
print(data.head(), "\n")

# --- بخش 3: تحلیل‌های آماری ---

# 1️⃣ میانگین دما، رطوبت و بارندگی هر شهر
mean_stats = data.groupby("City")[["Temperature", "Humidity", "Rainfall"]].mean()
print("میانگین دما، رطوبت و بارندگی هر شهر:")
print(mean_stats, "\n")

# 2️⃣ گرم‌ترین و سردترین شهر
hottest_city = mean_stats["Temperature"].idxmax()
coldest_city = mean_stats["Temperature"].idxmin()
print(f"🌡️ گرم‌ترین شهر: {hottest_city} با میانگین دمای {mean_stats.loc[hottest_city, 'Temperature']:.1f}")
print(f"❄️ سردترین شهر: {coldest_city} با میانگین دمای {mean_stats.loc[coldest_city, 'Temperature']:.1f}\n")

# 3️⃣ تعداد روزهای با بارندگی بالای 10 میلی‌متر برای هر شهر
rainy_days = data[data["Rainfall"] > 10].groupby("City")["Day"].count()
print("تعداد روزهای با بارندگی بیش از 10 میلی‌متر برای هر شهر:")
print(rainy_days)
