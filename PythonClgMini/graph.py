import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data1.csv')

emotion = df["EMOTIONS"]
people = df["NO. OF PEOPLE WHO WATCHES MOVIE"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b",'#66b3ff','#ff9999','#99ff99']
explode = (0.3, 0.1, 0, 0, 0)  
plt.pie(people,labels=emotion,radius=1.3,colors=colors,autopct='%1.1f%%', shadow='True', startangle=0)
plt.tight_layout()

plt.title("Pie Chart")
plt.show()
