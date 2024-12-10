from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from optbinning import BinningProcess
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd
import pickle

def log_regression_fit(final_df:pd.DataFrame, model_save_dir:str) -> (list, pd.DataFrame): # type: ignore

    variable_names = [x for x in final_df.columns if x != 'target']
    file_dir = model_save_dir + 'logistic_regression_model.pkl'    

    data = final_df[variable_names]
    target = final_df['target']
    
    X_train, _, y_train, _ = train_test_split(data.values, target.values, random_state=42, test_size=0.3)

    binning_process = BinningProcess(
    variable_names, max_n_bins=6, 
    max_n_prebins=6,
    min_bin_size=0.05
    )

    log_reg = Pipeline(
    steps=[
        ('binning_process', binning_process),
        ('log_reg_classification', LogisticRegression(random_state=42, max_iter=1000, penalty='l2', solver='saga'))
    ]
    )

    log_reg.fit(X_train, y_train)

    model_summary = binning_process.summary()

    cols_to_drop = []

    for name in model_summary['name']:
        if (
            (model_summary.loc[model_summary['name'] == name]['iv'].values[0] <= 0.01) 
            or 
            (model_summary.loc[model_summary['name'] == name]['gini'].values[0] <= 0.03)
        ):
            cols_to_drop.append(name)

    if(len(cols_to_drop) > 0):
        final_data_df = final_df.drop(columns=cols_to_drop)   
        variable_names = [x for x in final_data_df.columns if x != 'target']

        data = final_data_df[variable_names]
        target = final_data_df['target']

        X_train, _, y_train, _ = train_test_split(data.values, target.values, random_state=42, test_size=0.3)

        binning_process = BinningProcess(
        variable_names, max_n_bins=6, 
        max_n_prebins=6,
        min_bin_size=0.05
        )

        log_reg = Pipeline(
        steps=[
            ('binning_process', binning_process),
            ('log_reg_classification', LogisticRegression(random_state=42, max_iter=1000))
        ]
        )

        log_reg.fit(X_train, y_train)
        model_summary = binning_process.summary()

        with open(file_dir, 'wb') as file:
            pickle.dump(log_reg, file)

    else:
        with open(file_dir, 'wb') as file:
            pickle.dump(log_reg, file)

    for name in model_summary['name']:
        optb = binning_process.get_binned_variable(name)
        print('------------------------')
        print(f'Variable name: {name}')
        print('------------------------')
        print(optb.binning_table.build())        
        print('************************')
        # optb.binning_table.plot(metric="event_rate")

    model_summary.sort_values(by=['iv', 'gini'], ascending=False, inplace=True)

    model_summary_clean = model_summary[~model_summary['name'].isin(cols_to_drop)]

    return cols_to_drop, model_summary_clean
    
    