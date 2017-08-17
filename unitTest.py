# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:59:23 2017

@author: Snowlaw
"""

# Unit Test Program
import titanicSurvival

'''
Test Import Data
'''

raw = import_raw_data('train.csv')
#print('raw\n', raw)

'''
Test Cleansing Data
'''

cleanRaw = clean_data(raw, 0)
print('cleanRaw\n', cleanRaw)

'''
Test report min max mean median mode std 
'''
print_basic_stat(cleanRaw)

'''
Test Barplot
'''
#barPlot(pd.DataFrame({'a':[1 ,3, 5, 7, 7], 'b':[2, 4, 6, 8, 8]}), ['a','b'])
col_interest = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
barPlot(cleanRaw, col_interest)

'''
Test Histplot
'''
col_interest = ['Age', 'Fare']
histPlot(cleanRaw, col_interest, 10)

'''
Test Barplot Compare
'''
colname = ['Survived', 'Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']
barPlotCompare(cleanRaw, colname)

'''
Test Histplot Compare
'''
col_interest = ['Age', 'Fare']
histPlotCompare(cleanRaw, col_interest, 10)
