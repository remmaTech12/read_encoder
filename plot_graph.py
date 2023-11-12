import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('rpm_data.log',sep='\s+',header=None)
data = pd.DataFrame(data)
y = data[0][400:]
x = range(len(y))
t = []
for i in x:
		i *= 0.01
		t.append(i)

plt.plot(t, y, 'r--')
plt.title("motor control; target: 100 [rpm]")
plt.xlabel("time [s]")
plt.ylabel("rotational velocity [rpm]")
plt.ylim(-120, 120)
plt.grid()
plt.show()
