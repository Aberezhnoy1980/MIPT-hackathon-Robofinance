import pandas as pd

def compress_trade_acct_type(df:pd.DataFrame):
    if(
        (df['trade_acct_type1'] == 1.0)
        or
        (df['trade_acct_type1'] == 7.0)
        or
        (df['trade_acct_type1'] == 11.0)
    ): return 'working_capital'

    elif(
        (df['trade_acct_type1'] == 2.1)
        or
        (df['trade_acct_type1'] == 2.2)
        or
        (df['trade_acct_type1'] == 2.3)
        or
        (df['trade_acct_type1'] == 2.4)
        or
        (df['trade_acct_type1'] == 2.5)
        or
        (df['trade_acct_type1'] == 2.6)
        or
        (df['trade_acct_type1'] == 2.7)
    ): return 'real_estate'

    elif(
        (df['trade_acct_type1'] == 3.0)
        or
        (df['trade_acct_type1'] == 4.1)
        or
        (df['trade_acct_type1'] == 4.2)
        or
        (df['trade_acct_type1'] == 4.3)
        or
        (df['trade_acct_type1'] == 4.4)
        or
        (df['trade_acct_type1'] == 4.5)
        or
        (df['trade_acct_type1'] == 4.6)
        or
        (df['trade_acct_type1'] == 4.7)
        or
        (df['trade_acct_type1'] == 4.8)
        or
        (df['trade_acct_type1'] == 4.9)
        or
        (df['trade_acct_type1'] == 14.0)
        or
        (df['trade_acct_type1'] == 15.0)
        or
        (df['trade_acct_type1'] == 16.0)
        or
        (df['trade_acct_type1'] == 20.0)
    ): return 'basic_needs'

    elif(
        (df['trade_acct_type1'] == 5.0)
        or
        (df['trade_acct_type1'] == 6.0)

    ): return 'high_risk'
    elif(
        (df['trade_acct_type1'] == 8.0)
        or
        (df['trade_acct_type1'] == 9.0)
        or
        (df['trade_acct_type1'] == 10.0)
        or
        (df['trade_acct_type1'] == 12.0)
        or
        (df['trade_acct_type1'] == 13.0)
    ): return 'restructured_credits'

    elif(
        (df['trade_acct_type1'] == 17.0)
        or
        (df['trade_acct_type1'] == 18.0)
    ): return 'vehicles'
    else: return 'purpose_undefined'