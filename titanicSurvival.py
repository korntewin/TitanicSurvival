# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:40:39 2017

@author: Snowlaw
"""
# Titanic Survival

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def import_raw_data(filename):
    """
    Import raw data as Pandas DataFrame
    
    input String filename
    output dataframe df
    """
    raw = pd.read_csv(filename, index_col = 0)
    return raw

def print_basic_stat(df):
    report = pd.DataFrame(index = ['min','max','mean','median','mode','std'])
    colName = list(df.columns)
    
    for col in colName:
        if df[col].dtype != 'object':
            stat = np.round([df[col].min(), df[col].max(), df[col].mean(), df[col].median(), df[col].mode()[0], df[col].std()],2)
            report[col] = stat
    
    print(report)
    
def clean_data(df2, replace_num = 0, replace_str = 'unknown'):
    '''
    Clean Nan value from raw data
    
    Input : dataframe df
    Output : dataframe df
    '''
    df = df2.copy()
    columns = df.columns.values
    for col in columns:
        print('col', col)
        if df[col].dtype == 'object':
            df.loc[pd.isnull(df[col]), col] = replace_str
        else:
            df.loc[pd.isnull(df[col]), col] = replace_num
        
    return df

def barPlot(df, colname):
    '''
    Generate visualize histogram of columns name
    Input   df = DataFrame
            colname = list of string
    '''
    
    for col in colname:
        
        fig = plt.figure()
        fig.clf()
        ax = fig.gca()
        # set parameter of barplot
        pd.value_counts(df[col]).plot(kind = 'bar', ax = ax)
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
        ax.set_title('Barplot of '+col)
        

def histPlot(df, colname, bins):
    '''
    Generate visualize histogram of columns name
    Input   df = DataFrame
            colname = list of string
    '''
    
    for col in colname:
        
        fig = plt.figure()
        fig.clf()
        ax = fig.gca()
        
        ax.set_xlabel(col)
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of '+ col)
        ax.grid()
        
        df.hist(column = col, ax = ax)
        
def barPlotCompare(df, colname):
    '''
    Plot and compare between barplot of Survived = 0 and Survived = 1
    
    input : dataframe
    return : nothing
    '''
    
    for col in colname:
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
        # Barplot of survivied = 0
        pd.value_counts(df[col].loc[df.Survived == 0], sort = False).plot(kind = 'bar', ax = ax1)
        ax1.set_xlabel('Survived')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Barplot of ' + col + ' dead')
        
        pd.value_counts(df[col].loc[df.Survived == 1], sort = False).plot(kind = 'bar', ax= ax2)
        ax2.set_xlabel('Survived')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Barplot of ' + col + ' alive')
                
#barPlotCompare(pd.DataFrame({'Survived':[1, 0, 0, 0],'a':[10, 20, 30, 30],'b':[5, 10, 10, 15]}), ['a'])
   
def histPlotCompare(df, colname, bins):
    '''
    Plot and compare between histplot of Survived = 0 and Survived = 1
    
    input : dataframe
    return : nothing
    '''     
    
    for col in colname:
        f, (ax1, ax2) = plt.subplots(1, 2, sharey=True, sharex = True, figsize = (10, 10))
        # Barplot of survivied = 0
        df.loc[df['Survived'] == 0].hist(column = col, ax = ax1)
        ax1.set_xlabel('Survived')
        ax1.set_ylabel('Frequency')
        ax1.set_title('Histplot of ' + col + ' dead')
        
        df.loc[df['Survived'] == 1].hist(column = col, ax = ax2)
        ax2.set_xlabel('Survived')
        ax2.set_ylabel('Frequency')
        ax2.set_title('Histplot of ' + col + ' alive')
        
## GG