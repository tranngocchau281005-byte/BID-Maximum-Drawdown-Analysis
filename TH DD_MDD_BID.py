# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 12:02:03 2025

@author: Chau
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 29 10:05:53 2025

@author: Chau
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# upload file vnindex vào (nếu tải từ investing.com)
t = 'C:/Users/Chau/OneDrive - THPT Nguyễn Công Trứ/Attachments/TC định lượng/BID_MDD.csv'
df = pd.read_csv (t,sep=";")
print (df)
print (df.info())
# Đổi cột 'time' sang kiểu datetime
df["time"] = pd.to_datetime(df["time"],format='%d/%m/%Y')
df.set_index("time", inplace=True)

# Tính toán DD và MDD
p = df["close"]
# Calculate the cumulative maximum
df['Peak Value'] = p.cummax()
# Tính DD
df['Drawdown'] = df['Peak Value'] - p

mdd = df['Drawdown'].max()

df['Drawdown Percent'] = (df["Drawdown"]/df['Peak Value'])*100

mdd_percent = df["Drawdown Percent"].max()

# Vẽ đồ thị
fig, ax = plt.subplots(figsize=(8, 4))
df['close'].plot(ax=ax, label='Absolute Portfolio Values', linewidth=2)
df['Drawdown'].plot(kind='area', color='red', alpha=0.3, ax=ax, label='Drawdown')

# Hiển thị giá trị Drawdown trên đồ thị
for i, value in enumerate(df['Drawdown']):
    if value > 0:
        ax.annotate(str(value), xy=(i, value), ha='center', va='bottom')

# Thiết lập tiêu đề
ax.set_title('Absolute Portfolio Values and Drawdown')

# Hiển thị chú thích
ax.legend()

# Hiển thị đồ thị
plt.show()
