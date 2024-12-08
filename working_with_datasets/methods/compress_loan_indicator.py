import pandas as pd
import numpy as np

def compress_loan_indicator(df:pd.DataFrame):
    if(
        (df['loan_indicator'] == 1)
    ): return 'proper_loan_closure'

    elif(
        (df['loan_indicator'] == 2)
        or
        (df['loan_indicator'] == 4)
        or
        (df['loan_indicator'] == 7)
        or
        (df['loan_indicator'] == 8)
        or
        (df['loan_indicator'] == 13)
    ): return 'forced_loan_closure'

    elif(
        (df['loan_indicator'] == 3)
        or
        (df['loan_indicator'] == 9)
        or
        (df['loan_indicator'] == 11)
    ): return 'mutual_agreement'

    elif(
        (df['loan_indicator'] == 5)
        or
        (df['loan_indicator'] == 6)
        or
        (df['loan_indicator'] == 11)
        or
        (df['loan_indicator'] == 12)
        or
        (df['loan_indicator'] == 14)
        or
        (df['loan_indicator'] == 15)
    ): return 'unfulfilled_loan'
    elif(df['loan_indicator'] == 10): 
        return 'novation'
    elif(df['loan_indicator'] == 99): 
        return 'other'
    else: return np.nan