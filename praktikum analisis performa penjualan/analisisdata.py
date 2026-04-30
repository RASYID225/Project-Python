
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Menggunakan dataset contoh (bisa diganti dengan path file kaggle anda)

df = pd.read_csv('dataset.csv')
print(df.head())
df.info()
df.isnull().sum()
df = df[df['Price']>0]
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Analisis Deskriptif
print(df.describe())    

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()
print(monthly_sales)
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()

correlation = df[['Quantity', 'Price', 'Ad_Budget', 'Total_Sales']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Peta Korelasi Antar Variabel')
plt.show()

import datetime as dt

# Menentukan tanggal snapshot (hari setelah transaksi terakhir di data)
snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

# Agregasi data RFM
rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days, # Recency
    'Order_ID': 'count',                                   # Frequency
    'Total_Sales': 'sum'                                   # Monetary
})

# Rename kolom
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Memberikan skor 1-5 (Semakin tinggi semakin baik)
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1]) 
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

# Menggabungkan skor menjadi segmen RFM
rfm['RFM_Group'] = rfm.R_Score.astype(str) + rfm.F_Score.astype(str) + rfm.M_Score.astype(str)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[['Ad_Budget']] # Fitur
y = df['Total_Sales'] # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

print(f"Koefisien Iklan: {model.coef_[0]}")
print(f"Akurasi Model (R2 Score): {model.score(X_test, y_test)}")