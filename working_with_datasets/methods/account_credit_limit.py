import pandas as pd

def account_credit_limit(df_bki:pd.DataFrame) -> pd.DataFrame:
    df_pivot = pd.pivot_table(df_bki, values=['account_amt_credit_limit'], index=['application_id'], columns=['trade_loan_kind_code'], aggfunc='sum').reset_index()
    df_pivot.fillna(0.0,inplace=True)
    df_pivot.columns = [(c[0] + '_' + str(c[1])) if c[1] else c[0] for c in df_pivot.columns.tolist()]

    return df_pivot