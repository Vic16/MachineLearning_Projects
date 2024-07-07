import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def plotVars(var, target, df):

    """
    This function plot an histogram and boxplot of distribution of a given variable.
    
    var: str type, name of the variable to plot
    target: str type, name of the variable target to plot
    df: Pandas DataFrame Object
    """
    
    fig, axes = plt.subplots(2, 2, figsize=(12,12))
    
    sns.histplot(ax=axes[0,0], x=str(var), data=df).set(title='Distribution of {}'.format(var))
    sns.boxplot(ax=axes[0,1], y=str(var), data=df).set(title='Boxplot of {}'.format(var))
    #sns.histplot(ax=axes[1,0], x=str(var), palette="viridis", data=df,hue=str(target)).set(title='Distribution of {} by {}'.format(var, target))
    sns.boxplot(ax=axes[1,1], y=str(var), x=str(target), palette="viridis", data=df,hue=str(target)).set(title='Distribution of {} by {}'.format(var, target))
    
    plt.show()
    print("--------------------------")
    print(df[[var, target]].groupby(target).describe().T)



if __name__ == "__main__":
    print("")