import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig("Correaltion_heatmap.png")
plt.show()


plt.figure(figsize=(8,6))
sns.boxplot(x='price_range',y='ram', data=df)
plt.title('RAM vs Price Range')
plt.savefig("RAM_vs_Price_Range.png")
plt.show()
