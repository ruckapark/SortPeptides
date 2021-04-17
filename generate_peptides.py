# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:15:42 2021

Trier peptides maxime

@author: George Ruck
"""

#import relevant libs
import pandas as pd
import numpy as np

#read csv file
def read_csv_peptides(filename):
    
    file = pd.read_csv(filename,index_col = 0)
    return file

def scan_file(df):
    return None

if __name__ == '__main__':
    
    filename = 'peptides_1.csv'
    file = read_csv_peptides(filename)
    results = pd.DataFrame(columns = ['Data','Peptide1','Peptide2','Peptide3'])
    results_abundance = pd.DataFrame(columns = ['Data','Peptide1','Peptide2','Peptide3'])
    for x,data in enumerate(file.columns):
        
        if file[data].isnull().sum() != file.shape[0]:
            temp = file[data].dropna().sort_values(ascending = False)
            
            if temp.size>2:
                results.loc[x] = {'Data':data,'Peptide1':temp.index[0],'Peptide2':temp.index[1],'Peptide3':temp.index[2]}
                results_abundance.loc[x] = {'Data':data,'Peptide1':temp.iloc[0],'Peptide2':temp.iloc[1],'Peptide3':temp.iloc[2]}
            elif temp.size > 1:
                results.loc[x] = {'Data':data,'Peptide1':temp.index[0],'Peptide2':temp.index[1],'Peptide3':np.nan}
                results_abundance.loc[x] = {'Data':data,'Peptide1':temp.iloc[0],'Peptide2':temp.iloc[1],'Peptide3':np.nan}
            else:
                results.loc[x] = {'Data':data,'Peptide1':temp.index[0],'Peptide2':np.nan,'Peptide3':np.nan}
                results_abundance.loc[x] = {'Data':data,'Peptide1':temp.iloc[0],'Peptide2':np.nan,'Peptide3':np.nan}
                
                
    results = results.set_index('Data')
    results.to_csv('{}_results.csv'.format(filename.split('.')[0]))
            
            