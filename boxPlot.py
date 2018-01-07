import pandas as pd
import matplotlib.pyplot as plt
import sys
df=pd.read_csv(sys.argv[1], header=0)
df.set_index("Sub-division",inplace=True)
del df["Percentage change w.r.t Normal Rainfall in 2011"]
del df["Percentage change w.r.t Normal Rainfall in 2010"]
del df["Normal Rainfall 2011 (in millimetre)"]
del df["Normal Rainfall 2010 (in millimetre)"]
states = list(df.index.values)
dft = df.transpose()
plotmap=[]
for item in states:
    plotmap.append(dft[item].dropna().tolist())
print plotmap
plt.boxplot(plotmap)
siz = len(states)
plt.xticks(range(1,siz+1),states,rotation='vertical')
plt.xlabel("Sub-divisions")
plt.ylabel("Rainfall (2002-2011)")
plt.title("Annual rainfall in different sub-divisions from 2002 to 2011")

plt.legend()
plt.show()
