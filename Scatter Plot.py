#Pandas libary python digunakan untuk membaca file csv
import pandas as pd
import warnings ##untuk mengabaikan perintah warning pada seaborn
warnings.filterwarnings("ignore")
#Matplotlib memvisualisasikan data secara 2D atau 3D
import matplotlib.pyplot as plt
#Visualisasi data secara statistik agar tampak lebih menarik
import seaborn as sns

#Membaca file csv dan meyimpannya pada variabel belajar
belajar = pd.read_csv("Dataset/insurance.csv")
#menampilkan semua data
belajar.head()

#memvisualisasikan distribusi data dengan x (age) dan y (bmi)
sns.FacetGrid(belajar, hue="sex", size=5) .map(plt.scatter, "age", "bmi") .add_legend()

#menampilkan hasil visualisasi
plt.show()
