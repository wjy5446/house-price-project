import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns

sns.set()

def dispUniQuan(data, size = (5, 5), kde = True, rug = False):
    n_data_columns = len(data.columns)
    col = 2
    row = n_data_columns // 2 if (n_data_columns % 2) == 0 else (n_data_columns // 2) + 1

    f, axes = plt.subplots(row, col, figsize = (size[0]*col, size[1]*row))

    i = 0
    j = 0

    for c in data.columns:
        s_quan = data[c]

        if(s_quan.isnull().all() == False):
            s_quan.dropna(inplace = True)

        # display the distplot
        sns.distplot(s_quan, kde = kde, rug = rug, ax = axes[i, j])

        j+=1

        if j == 2:
            i += 1
            j = 0

def dispUniQual(data, size = (5, 5)):
    n_data_columns = len(data.columns)
    col = 2
    row = n_data_columns // 2 if (n_data_columns % 2) == 0 else (n_data_columns // 2) + 1

    f, axes = plt.subplots(row, col, figsize = (size[0]*col, size[1]*row))

    i = 0
    j = 0

    for c in data.columns:

        # display the countplot
        sns.countplot(x = c, data = data, ax = axes[i, j])

        j+=1

        if j == 2:
            i += 1
            j = 0


def dispMultiQuan_target(data, target, size = (5, 5)):
    data[target.name] = target

    n_data_columns = len(data.columns)
    col = 2
    row = n_data_columns // 2 if (n_data_columns % 2) == 0 else (n_data_columns // 2) + 1

    i = 0
    j = 0

    f, axes = plt.subplots(row, col, figsize = (size[0]*col, size[1]*row))

    for c in data.columns:

        if(c == target.name):
            continue

        tmp_data = pd.DataFrame(data, columns = [c, target.name])
        if(tmp_data.isnull().all()[c] == False):
            tmp_data.dropna(inplace = True)

        # display the scattor
        axes[i, j].scatter(tmp_data[c], tmp_data[target.name])
        axes[i, j].set_xlabel(c)

        j+=1

        if j == 2:
            i += 1
            j = 0

def dispMultiQual_target(data, target, size = (5, 5)):
    data[target.name] = target

    n_data_columns = len(data.columns)
    col = 2
    row = n_data_columns // 2 if (n_data_columns % 2) == 0 else (n_data_columns // 2) + 1

    i = 0
    j = 0


    f, axes = plt.subplots(row, col, figsize = (size[0]*col, size[1]*row))

    for c in data.columns:

        if(c == target.name):
            continue

        # display the countplot
        sns.boxplot(x=c, y=target.name, data=data, ax = axes[i, j])

        j+=1

        if j == 2:
            i += 1
            j = 0

def dispQuan(data, target, size = (5, 5)):
    data[target.name] = target

    n_data_columns = len(data.columns)
    col = 2
    row = len(data.columns)

    i = 0

    f, axes = plt.subplots(row, col, figsize = (size[0]*col, size[1]*row))

    for c in data.columns:

        if(c == target.name):
            continue

        tmp_data = pd.DataFrame(data, columns = [c, target.name])
        if(tmp_data.isnull().all()[c] == False):
            tmp_data.dropna(inplace = True)

        # display the distplot
        sns.distplot(tmp_data[c], kde = True, rug = False, ax = axes[i, 0])

        # display the scattor
        axes[i, 1].scatter(tmp_data[c], tmp_data[target.name])
        axes[i, 1].set_xlabel(c)

        i+=1

def dispQual(data, target, size = (5, 5)):
    data[target.name] = target

    n_data_columns = len(data.columns)
    col = 2
    row = n_data_columns

    i = 0

    f, axes = plt.subplots(row, col, figsize = (size[0]*col, size[1]*row))

    for c in data.columns:

        if(c == target.name):
            continue

        # display the countplot
        sns.countplot(x = c, data = data, ax = axes[i, 0])
        # display the boxplot
        sns.boxplot(x=c, y=target.name, data=data, ax = axes[i, 1])

        i+=1
