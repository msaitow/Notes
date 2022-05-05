#!/usr/bin/env python3
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
from scipy.optimize import curve_fit

def pol6(x,a,b,c,d,e,f,g): return a*x**6 + b*x**5 + c*x**4 + d*x**3 + e*x**2 + f*x**1 + g
y_fit = np.vectorize(pol6)

def pol2(x,a,b,c): return a*x**2 + b*x**1 + c
y_fit2 = np.vectorize(pol2)

csvname='lct_caspt2.csv'
fit6_csvname='lct_fit1.csv'
fit2_csvname='lct_fit2.csv'

df  = pd.read_csv(csvname)
df6 = pd.read_csv(fit6_csvname)
df2 = pd.read_csv(fit2_csvname)

fig = plt.figure()

ax = fig.add_subplot(111,xlabel='', ylabel='Electronic Energy (E) / Eh')
print("Before shifting -> ", df['R'])

dfR = []
for x in df['R']: dfR.append(x-1.1)

df6R = []
for x in df6['R']: df6R.append(x-1.1)

df2R = []
for x in df2['R']: df2R.append(x-1.1)

print("After shifting -> ", dfR)

p_opt,cov = curve_fit(pol6,df6R,df6['E(CASPT2)'])
print ("parameter (6th order) ->", p_opt)

p_opt2,cov2 = curve_fit(pol2,df2R,df2['E(CASPT2)'])
print ("parameter (2nd order) ->", p_opt2)

ax.plot(dfR, df['E(CASPT2)' ], marker='o', linestyle='-', markersize=5, label='MRPT2 Energy')

xpoints = np.linspace(dfR[0],dfR[-1],num=40,endpoint=True)

ax.plot(xpoints,y_fit(xpoints,p_opt[0],p_opt[1],p_opt[2],p_opt[3],p_opt[4],p_opt[5],p_opt[6]),linestyle = ':',label = r'Fitting with $E(R)=\sum_{n=0}^6 C_n R^n$')

ax.plot(xpoints,y_fit2(xpoints,p_opt2[0],p_opt2[1],p_opt2[2]), linestyle = '--', label = r'Fitting with $E(R)=\sum_{n=0}^2 C_n R^n$')

ax.grid(axis='y')
ax.legend(loc='upper right')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f'{x:.1f}'.format(x)))
#ax.set_xlabel(f"Internuclear Distance (Bohr)")
ax.set_xlabel(f"Displacement from the Equilibrium ($\Delta R=R-R_e$) / Bohr")
ax.set_xlim(df6R[0],df6R[-1])
ax.set_ylim(-109.2,-108.4)

fig.subplots_adjust(left=0.2,bottom=0.2)
pdfname = csvname.replace('.csv','.pdf')
fig.savefig(pdfname)

