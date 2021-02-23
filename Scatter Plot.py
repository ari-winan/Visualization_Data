import pandas as pd
import warnings ##untuk mengabaikan perintah warning pada seaborn
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt
import seaborn as sns

belajar = pd.read_csv("Dataset/insurance.csv")
belajar.head()

sns.FacetGrid(belajar, hue="sex", size=5) .map(plt.scatter, "age", "bmi") .add_legend()

plt.show()
