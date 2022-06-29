import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt(fname='doPythona.txt', dtype=str, delimiter='\t', encoding='utf-8', usecols=np.arange(0, 4), skip_header=1)

znak = data[:, 0]
pl = data[:, 1]
ang = data[:, 2]
chn = data[:, 3]

pl = [int(i) for i in pl]
ang = [int(i) for i in ang]
chn = [int(i) for i in chn]


fig = plt.figure()
ax = []

for i in range(1,4):
    ax.append(fig.add_subplot(1, 3, i))
    ax[i-1].set_ylim([0, 8500])

ax[0].bar(znak, pl)
ax[1].bar(znak, ang)
ax[2].bar(znak, chn)

ax[1].set_yticklabels([])
ax[2].set_yticklabels([])

ax[0].set_title('PL')
ax[1].set_title('ANG')
ax[2].set_title('CHN')

plt.show()