import pandas as pd
import numpy as np

# split the data into Quan and Qual
def extractQuanFromDF(data, index = None, target = None, exclude_list = None):
    quan_columns = [ c for c in data.columns if data[c].dtype != "object"]

    if(index != None):
        quan_columns.remove(index)
    if(target != None):
        quan_columns.remove(target)

    if(exclude_list != None):
        for exclude in exclude_list:
            quan_columns.remove(exclude)

    df_train_quan =  pd.DataFrame(data, columns = quan_columns)

    return df_train_quan

def extractQualFromDF(data, index = None, target = None, include_list = None):
    qual_columns = [ c for c in data.columns if data[c].dtype == "object"]
    if(include_list != None):
        qual_columns +=include_list

    if(index != None):
        qual_columns.remove(index)
    if(target != None):
        qual_columns.remove(target)

    df_train_qual =  pd.DataFrame(data, columns = qual_columns)

    return df_train_qual

## get highest correlation
def get_redundant_pairs(data):
    pairs_to_drop = set()
    cols = data.columns

    for i in range(data.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))

    return pairs_to_drop

def get_top_abs_cor(data, n=5, column = None):
    if(column == None):
        au_cor = data.corr().abs().unstack()
        labels_to_drop = get_redundant_pairs(data)
        au_cor = au_cor.drop(labels = labels_to_drop).sort_values(ascending =False)
    else:
        au_cor = df.corr().abs()[column].drop(column).sort_values(ascending = False)

    return au_cor[0:n]

# get ratio of categorical
def get_ratio_categorical(data, column = None):
    s_count = data[column].value_counts()
    s_ratio = s_count.apply(lambda x : x / len(data) * 100)
    df_tmp = pd.DataFrame(index = s_count.index, columns = ["count", "ratio"])
    df_tmp["count"] = s_count
    df_tmp["ratio"] = s_ratio
    return df_tmp


## get maxinum ration of categorical
def get_max_ratio_categorical(data):
    df_count = data.copy()
    df_count["count"] = 1
    df_qual_max_cate = pd.DataFrame(columns = ["name", "max_value", "prop", "total_num"])

    for c in df_count.columns:
        s = df_count.groupby([c])["count"].agg("sum").sort_values(ascending = False)
        count = df_count[c].count()
        max_value = s.index[0]
        prop = s.values[0] / count * 100
        df_qual_max_cate.loc[len(df_qual_max_cate)] = [c, max_value, prop, count]

    return df_qual_max_cate
