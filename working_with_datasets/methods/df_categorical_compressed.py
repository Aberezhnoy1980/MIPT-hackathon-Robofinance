import pandas as pd
from .compress_trade_acc_type import compress_trade_acct_type
from .compress_loan_indicator import compress_loan_indicator

def df_categorical_compressed(df_categorical:pd.DataFrame) -> pd.DataFrame:
    df_categorical['trade_acct_type_compressed'] = df_categorical.apply(compress_trade_acct_type, axis=1)
    df_categorical['loan_indicator_compressed'] = df_categorical.apply(compress_loan_indicator, axis=1)
    df_categorical.fillna({'paymnt_condition_terms_frequency':99.0}, inplace=True)
    df_categorical.drop(columns=['trade_acct_type1', 'loan_indicator'], axis=1, inplace=True)
    return df_categorical