from sklearn.linear_model import LogisticRegression
from optbinning import BinningProcess
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd
import pickle

def log_regression_fit(X_train:np.ndarray, y_train:np.ndarray, variable_names:list, model_save_dir:str) -> None:

    file_dir = model_save_dir + 'logistic_regression_model.pkl'    
        
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

    print(binning_process.information(print_level=1))

    model_summary = binning_process.summary()

    cols_to_drop = []

    with open(file_dir, 'wb') as file:
        pickle.dump(log_reg, file)
    
    