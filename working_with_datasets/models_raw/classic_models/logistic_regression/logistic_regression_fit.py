from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from optbinning import BinningProcess
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd
import pickle

def log_regression_fit(final_df:pd.DataFrame, model_save_dir:str) -> list:

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
        ('log_reg_classification', LogisticRegression(random_state=42, max_iter=1000))
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

    with open(file_dir, 'wb') as file:
        pickle.dump(log_reg, file)

    return cols_to_drop
    
    