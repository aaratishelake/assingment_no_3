import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("datafile.csv")
m_df=df.fillna(0)#m_df means modified dataset in which nan value replace with 0
print(m_df)
df1=m_df["State/UTs"]
df2=m_df["All Schools 2012-13 (Functional Computers)"]
plt.title("percentage of primary school with computer")
plt.xlabel("states")
plt.ylabel("percentage")
plt.rcParams["figure.figsize"] = (100,6)
plt.plot(df1,df2)
plt.show()
m_df.plot.bar()
plt.show()
m_df.plot.hist()
plt.show()
m_df.plot.box()
plt.show()
