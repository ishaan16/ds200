import pandas as pd
import matplotlib.pyplot as plt
import sys
#create dataframe
df=pd.read_csv(sys.argv[1], header=0)
#plot scatter with first column as x values and second column as y values
plt.scatter(df["Year"],df['First October'],color='#dd12dd')

#specifying labels
plt.xlabel("Year")
plt.ylabel("Population of Haryana")
plt.title("Estimated Poplation of Haryana (1961-2011)")

plt.show()
