import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

belajar = pd.read_csv("Dataset/insurance.csv")
belajar.head()

sns.histplot(belajar['bmi'], bins=10)
plt.xlabel('interval 10')
plt.ylabel('frekuensi')
plt.show()
