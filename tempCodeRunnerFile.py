import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

belajar = pd.read_csv("Dataset/Index.csv")
belajar.head()

plt.hist(belajar['max'], bins=10)
plt.xlabel('interval')
plt.ylabel('frekuensi')
plt.show()

