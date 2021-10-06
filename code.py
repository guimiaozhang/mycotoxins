# -*- coding: utf-8 -*-
"""
mycotoxins screening

2 different types of screenigs, each contains test name, detection limit(DL)
tp, fn, tn, fp: 0, 1, DL& name combo

if more types of tests were here, modify df.name part
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

path = ''

## explore, if sth isnull, delete, here as no, ignore
df = pd.read_csv(path, header=0)
print('Data Shape: ', df.shape)
print('Data Columns: ', list(df.columns))
print('Data contains any NAs:', df.isnull().values.any())
print('Data head: ', df.head())


## check inpout
df['wrong'] = ((df['tp'] + df['tp'] + df['fn'] + df['fp']) != 1)
print(df.loc[df['wrong'] == True])

## delete wrong
df = df.loc[df['wrong'] == False] 

## agrregate
dat = df.groupby(['name', 'DL'], as_index = False), sum()

## sensitivity = tp / tp + fn; specificity = tn / tn + fp

dat['sens'] = dat['tp'] / (dat['tp'] + dat['fn'])
dat['spec'] = dat['tn'] / (dat['tn'] + dat['fp'])
dat['precision'] = dat['tp'] / (dat['tp'] + dat['fp'])
dat['accuracy'] = (dat['tn'] + dat['tp']) / (dat['tn'] + dat['fp'] + dat['tp'] + dat['fn'])

## now we need a data.frame sensitivity, specificity, DL, name
dat1 = df[df.name == 'M1', ['sens', 'spec', 'DL']]
dat2 = df[df.name == 'B1', ['sens', 'spec', 'DL']]


def plotting(sens, spec, DL, name):
    fig, ax = plt.subplots(figsize=(10, 10))
    plt.title('Detection Limit, sensitivity, specificity')
    plt.plot(range(len(DL)), sens, marker = 'o', label = 'sensitivity' )
    plt.plot(range(len(DL)), spec, marker = 'o', label = 'specificity' )
    plt.xlabel('Detection limit')
    plt.xticks(range(len(DL)), DL)
    plt.legend()
    plt.show()
    
plotting(dat1.sens, dat1.spec, dat1.DL, 'M1')
plotting(dat2.sens, dat2.spec, dat2.DL, 'B1')

# choose the DL,you want, check the accuracy, etc
dat[dat.DL == XXX & dat.name == 'M1']
