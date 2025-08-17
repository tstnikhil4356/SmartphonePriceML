import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

sns.set(style="whitegrid")
plt.figure(figsize=(14, 10))

heatmap = sns.heatmap(
    df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    linecolor='gray',
    annot_kws={"size": 8}
)

plt.title('📊 Feature Correlation Heatmap – Smartphone Price Prediction', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig("heatmap.png", dpi=300)
plt.show()


plt.figure(figsize=(8,6))
sns.boxplot(x='price_range',y='ram', data=df)
plt.title('RAM vs Price Range')
plt.savefig("RAM_vs_Price_Range.png")
plt.show()
