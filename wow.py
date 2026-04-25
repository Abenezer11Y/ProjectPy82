import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/content/Company Sales Data.csv')

plt.figure()
plt.plot(df["month_number"], df["total_profit"], color='red', linestyle=':', marker='o', mfc='black', mec='black', linewidth=3, label='Profit')
plt.title('Company Profit Per Month')
plt.xlabel("Month Number")
plt.ylabel("Profit")
plt.legend()

plt.figure()
plt.plot(df["month_number"], df["facecream"], marker='o', linewidth=3, label='Face Cream')
plt.plot(df["month_number"], df["facewash"], marker='o', linewidth=3, label='Face Wash')
plt.plot(df["month_number"], df["toothpaste"], marker='o', linewidth=3, label='Toothpaste')
plt.plot(df["month_number"], df["bathingsoap"], marker='o', linewidth=3, label='Bathing Soap')
plt.plot(df["month_number"], df["shampoo"], marker='o', linewidth=3, label='Shampoo')
plt.plot(df["month_number"], df["moisturizer"], marker='o', linewidth=3, label='Moisturizer')
plt.title('All Product Sales Data')
plt.xlabel("Month Number")
plt.ylabel("Sales Units")
plt.legend()

df.plot(x="month_number", y=["facecream", "facewash"], kind="bar", color=['red', 'blue'])
plt.title('Facewash vs Facecream Sales')
plt.xlabel("Month Number")
plt.ylabel("Sales Units")

plt.show()
