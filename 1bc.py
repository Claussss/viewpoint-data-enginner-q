import pandas as pd
import numpy as np

name_table = {'StudentID': ['V001', 'V002','V003', 'V004'], 
              'Name': ['Abe', 'Abhay','Acelin','Adelphos']}

mark_table = {'StudentID': ['V001', 'V002','V003', 'V004'], 
              'Total_marks': [95,80,74,81]}

name_df = pd.DataFrame(data=name_table)
mark_df = pd.DataFrame(data=mark_table)

def containsE(name:str) -> bool:
    return 'e' in name

def partB(df:pd.DataFrame) -> pd.DataFrame:
    assert 'Name' in df
    
    new_df = df.copy()
    new_df['Name'] = new_df['Name'].apply(lambda name: name.upper() if containsE(name) else name.lower())
    return new_df


def partC(partB_output:pd.DataFrame,mark_df:pd.DataFrame ) -> pd.DataFrame:
    assert 'StudentID' in partB_output and 'StudentID' in mark_df
    assert 'Name' in partB_output
    assert 'Total_marks' in mark_df
    
    merged_df = pd.merge(partB_output,mark_df,on='StudentID')
    # Create a temp column 'Font_case'
    merged_df['Font_case'] = np.where(merged_df['Name'].str.isupper(), 'uppercase', 'lowercase')
    grouped_df = merged_df.groupby(['Font_case']).mean().rename(columns={'Total_marks':'Total_marks_avg'})
    return grouped_df



partB_output = partB(name_df)
partC_output = partC(partB_output,mark_df)
print(partB_output)
print(partC_output)