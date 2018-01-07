import pandas as pd
import matplotlib.pyplot as plt
import sys

#creating dataframe
df=pd.read_csv(sys.argv[1], header=0)
df=df.drop([0])
states=df["All India/State/Union Territory"].tolist()
rural = df["2011 - Rural - Person"].tolist()
urban = df["2011 - Urban - Persons"].tolist()
siz = 2*len(rural)+1
rurind = range(1,siz,2)
print len(rurind)
print len(states) 
urbind = range(2,siz,2)
width=0.35
#plotting first type of bars
plt.bar(rurind,rural,width,color='#ddbbaa',label="Rural")
#plotting second type of bars
plt.bar([x+width for x in rurind],urban,width,color='#ddffaa',label="Urban")

#specifying labels
plt.xticks(rurind,states,rotation="vertical")
plt.xlabel("States")
plt.ylabel("Literacy rate in 2011")
plt.title("Rural/Urban Literacy rate in 2011 (state-wise)")

#enabling legend
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
