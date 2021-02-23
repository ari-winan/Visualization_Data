#Pandas libary python digunakan untuk membaca file csv
import pandas as pd
#Matplotlib memvisualisasikan data secara 2D atau 3D
import matplotlib.pyplot as plt
#Visualisasi data secara statistik agar tampak lebih menarik
import seaborn as sns

#Membaca file csv dan meyimpannya pada variabel belajar
belajar = pd.read_csv("Dataset/insurance.csv")
#menampilkan semua data
belajar.head()

#memvisualisasikan distribusi data dengan interval 10
sns.histplot(belajar['bmi'], bins=10)
plt.xlabel('interval 10')
plt.ylabel('frekuensi')

#menampilkan hasil visualisasi
plt.show()