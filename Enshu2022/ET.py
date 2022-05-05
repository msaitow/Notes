#!/usr/bin/env python3
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

csvname='ET.csv'
#data = pd.read_csv(csvname)
df = pd.read_csv(csvname)
#df = data.iloc[0:21]
#print(df)
#print(df.head())

#ax.plot( x,y1,'rs:',label='line1')
#ax.plot(y2,color='C0',marker='^',linestyle='-',label='line2')

fig = plt.figure()
#fig = plt.figure(figsize=(3.6,2.4))
ax = fig.add_subplot(111,xlabel='', ylabel='Computational Timings (sec.)')
print(df['N'])
ax.plot(df['N'], df['Boys' ], marker='x', linestyle='-', label='FB-LVMO')
ax.plot(df['N'], df['newPMNR' ], marker='o', linestyle='--', label='PM-LVMO')
ax.plot(df['N'], df['newPAO'], marker='^', linestyle=':', label='PAO')
#ax.plot(df['N'], df['newPMNR'], marker='v', linestyle='-.', label='newPM-LVMO')
ax.grid(axis='y')
ax.legend()
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
ax.set_xlabel(f"Number of carbon atoms in the side chain")
#ax.set_ylim(0,110000)
ax.set_xticks(np.arange(10,160,10))
ax.set_xticklabels([10,"",30,"",50,"",70,"",90,"",110,"",130,"",150])
###plt.setp(ax.get_xticklabels(),  ha="right")

fig.subplots_adjust(left=0.2,bottom=0.2)
pdfname = csvname.replace('.csv','.pdf')
fig.savefig(pdfname)
#fig.savefig('ET_small.pdf')
