import pandas as pd
from .compress_trade_acc_type import compress_trade_acct_type
from .compress_loan_indicator import compress_loan_indicator



def df_categorical_compressed(df_categorical:pd.DataFrame) -> pd.DataFrame:
    df_categorical['trade_acct_type_compressed'] = df_categorical.apply(compress_trade_acct_type, axis=1)
    df_categorical['loan_indicator_compressed'] = df_categorical.apply(compress_loan_indicator, axis=1)
    df_categorical.fillna({'paymnt_condition_terms_frequency':99.0}, inplace=True)

    df_categorical.drop(columns=['trade_acct_type1', 'loan_indicator'], axis=1, inplace=True)

    columns_for_indicator_variables = [x for x in df_categorical.columns if x != 'application_id']

    df_categorical = pd.get_dummies(df_categorical, columns=columns_for_indicator_variables, dtype=int, dummy_na=False)

    df_categorical_groupped = df_categorical.groupby(['application_id'], as_index=False).sum()
    
    return df_categorical_groupped